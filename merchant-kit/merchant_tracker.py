#!/usr/bin/env python3
"""
Jago Hemat — Merchant Outreach Tracker
Flask app on port 5005 with SQLite backend.

Tracks: business name, contact person, WhatsApp, status (contacted/interested/signed up)
Endpoints:
  GET  /health           — Health check
  POST /merchant          — Add/update a merchant prospect
  GET  /merchant/<id>    — Get merchant by ID
  GET  /merchants         — List all merchants (with filters)
  POST /merchant/<id>/status — Update merchant status
  GET  /stats            — Dashboard stats
  GET  /export           — CSV export
"""

import csv
import os
import sqlite3
import json
from datetime import datetime
from flask import Flask, request, jsonify, Response, g

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "merchant_tracker.db")

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

# ── Database helpers ──────────────────────────────────────────────────────────

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS merchants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            business_name   TEXT NOT NULL,
            business_type   TEXT DEFAULT '',
            contact_name    TEXT DEFAULT '',
            whatsapp        TEXT DEFAULT '',
            email           TEXT DEFAULT '',
            address         TEXT DEFAULT '',
            city            TEXT DEFAULT 'Indonesia',
            status          TEXT DEFAULT 'pending',
            notes           TEXT DEFAULT '',
            source          TEXT DEFAULT '',
            created_at      TEXT DEFAULT (datetime('now')),
            updated_at      TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()

# ── Routes ───────────────────────────────────────────────────────────────────

@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "jago-hemat-merchant-tracker"})


@app.route("/merchant", methods=["POST"])
def add_merchant():
    """Add a new merchant prospect."""
    data = request.get_json() or {}
    required = ["business_name"]
    for field in required:
        if not data.get(field):
            return jsonify({"error": f"'{field}' is required"}), 400

    db = get_db()
    now = datetime.utcnow().isoformat()
    db.execute("""
        INSERT INTO merchants
        (business_name, business_type, contact_name, whatsapp, email,
         address, city, status, notes, source)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("business_name"),
        data.get("business_type", ""),
        data.get("contact_name", ""),
        data.get("whatsapp", ""),
        data.get("email", ""),
        data.get("address", ""),
        data.get("city", "Indonesia"),
        data.get("status", "pending"),
        data.get("notes", ""),
        data.get("source", ""),
    ))
    merchant_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
    db.commit()

    return jsonify({"success": True, "id": merchant_id, "status": "pending"}), 201


@app.route("/merchant/<int:merchant_id>", methods=["GET"])
def get_merchant(merchant_id):
    db = get_db()
    row = db.execute("SELECT * FROM merchants WHERE id = ?", (merchant_id,)).fetchone()
    if not row:
        return jsonify({"error": "Merchant not found"}), 404
    return jsonify(dict(row))


@app.route("/merchant/<int:merchant_id>", methods=["PUT", "POST"])
def update_merchant(merchant_id):
    """Update a merchant's info or status."""
    data = request.get_json() or {}
    db = get_db()
    now = datetime.utcnow().isoformat()

    # Build dynamic update
    allowed = [
        "business_name", "business_type", "contact_name", "whatsapp",
        "email", "address", "city", "status", "notes", "source"
    ]
    set_clause = ", ".join(f"{k} = ?" for k in allowed if k in data)
    if set_clause:
        set_clause += ", updated_at = ?"
        values = [data[k] for k in allowed if k in data] + [now, merchant_id]
        db.execute(f"UPDATE merchants SET {set_clause} WHERE id = ?", values)
        db.commit()

    row = db.execute("SELECT * FROM merchants WHERE id = ?", (merchant_id,)).fetchone()
    return jsonify({"success": True, "merchant": dict(row)})


@app.route("/merchant/<int:merchant_id>/status", methods=["POST"])
def update_status(merchant_id):
    """Update only the status field."""
    data = request.get_json() or {}
    status = data.get("status")
    valid = ("pending", "contacted", "interested", "signed_up", "rejected", "inactive")
    if status not in valid:
        return jsonify({"error": f"status must be one of: {valid}"}), 400

    db = get_db()
    now = datetime.utcnow().isoformat()
    db.execute(
        "UPDATE merchants SET status = ?, updated_at = ? WHERE id = ?",
        (status, now, merchant_id)
    )
    db.commit()
    return jsonify({"success": True, "id": merchant_id, "status": status})


@app.route("/merchants", methods=["GET"])
def list_merchants():
    """
    List all merchants.
    Query params:
      status    — filter by status (comma-separated)
      city      — filter by city
      q         — search in business_name / contact_name
      page      — page number (default 1)
      per_page  — items per page (default 50)
    """
    db = get_db()
    filters = []
    values = []

    if request.args.get("status"):
        statuses = request.args["status"].split(",")
        placeholders = ",".join("?" * len(statuses))
        filters.append(f"status IN ({placeholders})")
        values.extend(statuses)

    if request.args.get("city"):
        filters.append("city LIKE ?")
        values.append("%" + request.args["city"] + "%")

    if request.args.get("q"):
        q = "%" + request.args["q"] + "%"
        filters.append("(business_name LIKE ? OR contact_name LIKE ?)")
        values.extend([q, q])

    where = " AND ".join(filters) if filters else "1=1"
    page = max(1, int(request.args.get("page", 1)))
    per_page = min(100, int(request.args.get("per_page", 50)))
    offset = (page - 1) * per_page

    total = db.execute(f"SELECT COUNT(*) FROM merchants WHERE {where}", values).fetchone()[0]
    rows = db.execute(
        f"SELECT * FROM merchants WHERE {where} ORDER BY updated_at DESC LIMIT ? OFFSET ?",
        values + [per_page, offset]
    ).fetchall()

    return jsonify({
        "total": total,
        "page": page,
        "per_page": per_page,
        "merchants": [dict(r) for r in rows],
    })


@app.route("/stats", methods=["GET"])
def stats():
    """Dashboard stats."""
    db = get_db()

    total = db.execute("SELECT COUNT(*) FROM merchants").fetchone()[0]

    by_status = {}
    for row in db.execute("SELECT status, COUNT(*) as cnt FROM merchants GROUP BY status"):
        by_status[row["status"]] = row["cnt"]

    by_type = {}
    for row in db.execute("SELECT business_type, COUNT(*) as cnt FROM merchants WHERE business_type != '' GROUP BY business_type"):
        by_type[row["business_type"]] = row["cnt"]

    recent = db.execute(
        "SELECT COUNT(*) FROM merchants WHERE created_at > datetime('now', '-7 days')"
    ).fetchone()[0]

    # Conversion funnel
    funnel = {
        "pending":    by_status.get("pending", 0),
        "contacted":  by_status.get("contacted", 0),
        "interested": by_status.get("interested", 0),
        "signed_up":  by_status.get("signed_up", 0),
    }

    return jsonify({
        "total": total,
        "funnel": funnel,
        "by_status": by_status,
        "by_type": by_type,
        "added_last_7_days": recent,
        "conversion_rate_pct": round(
            by_status.get("signed_up", 0) / total * 100, 1
        ) if total else 0,
        "generated_at": datetime.utcnow().isoformat(),
    })


@app.route("/export")
def export_csv():
    """Export all merchants as CSV."""
    db = get_db()
    rows = db.execute("SELECT * FROM merchants ORDER BY id").fetchall()
    fieldnames = [
        "id", "business_name", "business_type", "contact_name", "whatsapp",
        "email", "address", "city", "status", "notes", "source",
        "created_at", "updated_at"
    ]
    output = __import__("io").StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for r in rows:
        writer.writerow({k: r.get(k, "") for k in fieldnames})

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=jago_hemat_merchants.csv"},
    )


# ── Init ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    print("[Jago Hemat Merchant Tracker] Starting on http://localhost:5005")
    app.run(host="0.0.0.0", port=5005, debug=False)
