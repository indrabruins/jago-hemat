# Jago Hemat — Merchant Partner Kit

Outreach materials for signing up bakeries, supermarkets, and restaurants in Indonesia as Jago Hemat merchant partners.

---

## 📁 Files

```
merchant-kit/
├── README.md                  ← You are here
├── merchant_one_pager.html    ← Mobile-first merchant landing page
├── merchant_tracker.py        ← Flask tracker app (port 5005)
├── merchant_tracker.db        ← SQLite database (created on first run)
└── whatsapp_templates.md       ← 4 WhatsApp message templates (Indonesian)
```

---

## 🚀 Quick Start

```bash
cd ~/work/jago-hemat/merchant-kit

# 1. Install dependencies
pip install flask

# 2. Start the tracker
python merchant_tracker.py

# 3. Serve the one-pager (any static server works)
python -m http.server 5006
# Then open: http://localhost:5006/merchant_one_pager.html
```

---

## 📄 Merchant One-Pager (`merchant_one_pager.html`)

Single-page mobile-first HTML. No external dependencies except Google Fonts.

**Serve options:**
```bash
# Option A: Python simple server
cd ~/work/jago-hemat/merchant-kit
python -m http.server 5006

# Option B: Use the existing Jago Hemat domain
# Upload to jagohemat.com/merchant or similar path

# Option C: Netlify drop
# Drag-and-drop the folder at https://app.netlify.com/drop
```

**Key content:**
- Hero: "Jual Lebih Banyak, Rugi Lebih Sedikit"
- Stats: Rp 8-15jt recovery/bulan, 50-80% diskon, gratis daftar
- 4-step how-it-works: Register → List → Konsumen Beli → Get Paid
- Case study (placeholder — update with real merchant)
- FAQ: 5 common questions
- WhatsApp CTA button

**WhatsApp CTA link** (placeholder — replace with real number):
```
https://wa.me/6280000000000?text=Halo%2C%20saya%20tertarik%20menjadi%20partner%20Jago%20Hemat
```

---

## 📊 Merchant Tracker (Flask on port 5005)

```bash
python merchant_tracker.py
```

Starts on `http://localhost:5005`.

### Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/health` | Health check |
| `POST` | `/merchant` | Add a new merchant prospect |
| `GET` | `/merchant/<id>` | Get merchant by ID |
| `PUT` | `/merchant/<id>` | Update merchant info |
| `POST` | `/merchant/<id>/status` | Update merchant status |
| `GET` | `/merchants` | List merchants (with filters) |
| `GET` | `/stats` | Dashboard stats |
| `GET` | `/export` | CSV export |

### Add a merchant prospect

```bash
curl -X POST http://localhost:5005/merchant \
  -H "Content-Type: application/json" \
  -d '{
    "business_name": "Toko Roti Bahagia",
    "business_type": "Bakery",
    "contact_name": "Budi Santoso",
    "whatsapp": "6281234567890",
    "city": "Bandung",
    "source": "Google Maps search"
  }'
```

### Update merchant status

```bash
curl -X POST http://localhost:5005/merchant/1/status \
  -H "Content-Type: application/json" \
  -d '{"status": "interested"}'
```

Valid statuses: `pending`, `contacted`, `interested`, `signed_up`, `rejected`, `inactive`

### List merchants with filters

```bash
# Only interested prospects
curl "http://localhost:5005/merchants?status=interested"

# Search by name
curl "http://localhost:5005/merchants?q=toko%20roti"

# Filter by city
curl "http://localhost:5005/merchants?city=Surabaya"
```

### Dashboard stats

```bash
curl http://localhost:5005/stats | python -m json.tool
```

### Export CSV

```bash
curl http://localhost:5005/export -o merchants_export.csv
```

---

## 💬 WhatsApp Templates (`whatsapp_templates.md`)

4 Indonesian-language WhatsApp templates included:

| # | Template | Use When |
|---|---|---|
| 1 | Cold Intro | First contact |
| 2 | Follow-Up | 2-3 days after no response |
| 3 | Referral Ask | For happy signed-up merchants |
| 4 | Reminder | For interested but not-yet-signed merchants |

### Quick send via WhatsApp Click-to-Chat

Replace `{{placeholders}}` then open:
```
https://wa.me/6280000000000?text=[encoded message]
```

### Best Practices
- **Jam kirim:** 09:00-17:00 WIB, weekdays
- **Max 1 pesan per merchant per 3 hari** — don't spam
- **Bahasa informal** — sesuai budaya chat Indonesia
- **Lampirkan one-pager** sebagai forward di pesan pertama kalau bisa
- **Follow up max 2x** — kalau tidak ada respons, stop dan catat "no response"

---

## 🔑 What to Update Before Launch

| Item | File | Current Value | Change To |
|---|---|---|---|
| WhatsApp Business number | `merchant_one_pager.html` | `6280000000000` | Real Jago Hemat number |
| WhatsApp number (4 templates) | `whatsapp_templates.md` | `6280000000000` | Real number |
| Case study merchant name | `merchant_one_pager.html` | `[Nama Partner]` | Real merchant |
| Case study since year | `merchant_one_pager.html` | `[Tahun]` | Real year |
| Referral bonus | `whatsapp_templates.md` | `[Contoh: Voucher Rp 100.000]` | Actual offer |

---

## 🔄 Typical Outreach Workflow

```
1. Research merchants
   → Find bakery/supermarket/restaurant contacts
   → Add via: POST /merchant

2. Send WhatsApp cold intro (Template 1)
   → Include one-pager link

3. Day 2-3: Follow up (Template 2) if no reply

4. Day 4-5: Reminder (Template 4) if interested but not signed up

5. After sign-up: Send Referral Ask (Template 3)
   → Offer referral bonus to grow network

6. Ongoing: Monitor /stats, update statuses
```

---

## ⚙️ Integration Notes

### Google Places for Prospect Research
To find merchants to contact:
```bash
# 1. Get API key at console.cloud.google.com
# 2. Save to: ~/.openclaw/credentials/google-places-api-key.txt
# 3. Use the KOI outreach system's prospect_finder.py:
cd ~/work/koihappiness/merchant_outreach
python prospect_finder.py --query "bakery Surabaya" --output jago_prospects.csv
```

### For the merchant tracker, port 5005:
If behind a firewall and need external access for mobile WhatsApp tracking, consider using ngrok:
```bash
ngrok http 5005
```

---

## 🛡️ Data & Privacy

- All data stored locally in `merchant_tracker.db` (SQLite)
- No external API calls to third parties
- WhatsApp numbers stored for outreach purposes only
- Comply with Indonesian data protection laws (UU PDP) — do not share exported CSV with third parties
