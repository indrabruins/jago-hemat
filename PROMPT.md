# PROMPT.md - Jago Hemat MVP

## Objective
Build a FastAPI backend for Jago Hemat - a surplus/inventory marketplace.

## Core Features

### 1. Item Listing API
- POST /api/items - Create listing with image, description, price, quantity
- GET /api/items - List available items with filters
- GET /api/items/{id} - Get single item details
- DELETE /api/items/{id} - Remove listing

### 2. User/Business Management
- POST /api/auth/register - Business registration
- POST /api/auth/login - JWT authentication

### 3. AI Features
- POST /api/ai/price-suggestion - AI suggests optimal price based on market data
- POST /api/ai/match - AI matches items to potential buyers

### 4. PostgreSQL Schema
Use SQLite for local dev, migrate to PostgreSQL for production.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    company_name VARCHAR(255),
    password_hash VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    quantity INTEGER DEFAULT 1,
    category VARCHAR(100),
    status VARCHAR(50) DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Exit Conditions
- All CRUD endpoints working
- Basic auth implemented
- SQLite database initialized
- Tests passing
- MISSION_ACCOMPLISHED when complete
