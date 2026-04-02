# Jago Hemat v3 — Audit Report (Apr 1, 2026)

## CRITICAL ISSUES

### 1. Dead onClick Alert Stubs (18 instances)
These replace with real functionality or remove entirely:
- Line 220: "Download Impact Card — Siap Share ke WhatsApp" → alert stub
- Line 295: "ESG Report — Download PDF" → alert stub
- Footer links: About Us, Blog, Careers, Contact → alert stubs
- Merchant footer: Dashboard, ESG Report → alert stubs

### 2. Hero Image
CURRENT: `assets/hero-illustration-preview.png` (flat illustration, generated)
SHOULD BE: Real Unsplash Indonesian food photography:
- hero-1: warm Indonesian food spread (https://images.unsplash.com/photo-1504674900247-0877df9cc836)
- hero-2: bakery display (https://images.unsplash.com/photo-1509440159596-0249088772ff)
- hero-3: fresh produce market (https://images.unsplash.com/photo-1488459716781-31db52582fe9)
Use food photography with warm tones, not illustration.

### 3. How It Works Icons → Real Photos
Step icons (SVGs) should be replaced with actual food photos:
- Step 1: Someone browsing app / food menu → real photo
- Step 2: Surprise bag / boxed food → real photo
- Step 3: Happy person picking up food → real photo

### 4. Deals Section
- All deal cards use Unsplash food images — OK for now
- Consider adding Jago Hemat branding watermark

## CALCULATOR STATUS
Already functional ✅ — IDs match JS:
- `wasteKg` input → updateROI() 
- `pricePerKg` input → updateROI()
- Form submit → opens WhatsApp with pre-filled message
- The only issue: inputs need live validation (no negative numbers)

## COPY IMPROVEMENTS NEEDED
1. Hero headline "Selamatkan Bumi. Rinse." → weak tagline
2. All alerts need real functionality or removal
3. Add WhatsApp CTA to merchant form

## PRIORITY
P0: Replace dead alerts with real functionality
P0: Hero photo swap (illustration → real food photo)
P1: How It Works real photos
P1: WhatsApp merchant form real CTA
