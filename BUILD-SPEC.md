# Jago Hemat — Full Website Build Spec
**For: Claude Code | CEO: Kit | Date: 2026-03-29**

---

## MISSION
Build a world-class dual-theme (dark + light), bilingual (EN + ID) landing page for Jago Hemat — an Indonesian food waste/surplus grocery marketplace. The site must be a conversion machine: compelling users to download the app and merchants to sign up.

---

## BRAND CONTEXT

**Product:** Jago Hemat — users buy 50-80% off surplus food from partner stores. Available on Play Store + App Store.
**Tagline (EN):** "Great Food. Smart Savings. Better Planet."
**Tagline (ID):** "Makanan Enak. Harga Hemat. Bumi Lebih Baik."
**Brand colors:** Emerald #10B981, Cyan #06B6D4, Amber #F59E0B

---

## FILES

### Reference Designs (READ THESE FIRST)
```
~/.openclaw/workspace/jago-designs/dark/   ← 5 screens
~/.openclaw/workspace/jago-designs/light/  ← 5 screens
```

### Assets to use
```
~/work/jago-hemat/assets/logo.png
~/work/jago-hemat/assets/hero-illustration.png
~/work/jago-hemat/assets/phone-mockup.png
~/work/jago-hemat/assets/category-icons.png
~/work/jago-hemat/assets/impact-card.png
~/work/jago-hemat/assets/how-it-works.png
```

### Output
```
~/work/jago-hemat/index.html   ← REPLACE the existing landing.html
```

---

## DESIGN SYSTEM

### CSS Variables (Dark Theme — default)
```
--bg: #0D0D0F
--card: #1A1A1E
--surface: #252529
--accent: #10B981
--accent2: #06B6D4
--warning: #F59E0B
--text: #FFFFFF
--text-muted: #9CA3AF
--border: rgba(255,255,255,0.08)
--gradient: linear-gradient(135deg, #10B981, #06B6D4)
--radius: 16px
--radius-sm: 10px
```

### CSS Variables (Light Theme)
```
--bg: #FAFAF9
--card: #FFFFFF
--surface: #F3F4F6
--accent: #10B981
--accent2: #059669
--warning: #D97706
--text: #111827
--text-muted: #6B7280
--border: rgba(0,0,0,0.08)
--gradient: linear-gradient(135deg, #10B981, #06B6D4)
```

### Typography
- Headings: Poppins 600, 700, 800 (Google Fonts)
- Body: Inter 400, 500, 600 (Google Fonts)

---

## SECTIONS (in order)

### 1. STICKY NAV
- Logo left (from assets/logo.png — use `<img>` tag)
- Nav links: "How It Works" | "Deals" | "Impact" | "For Business"
- Language toggle: [EN | ID] pill buttons
- Theme toggle: 🌙 dark / ☀️ light
- CTA button right: "Download App" (gradient green)
- Mobile: hamburger → full-screen drawer
- Behavior: transparent at top, solid + backdrop-blur on scroll

### 2. HERO (DARK, 100vh)
- Full viewport height, dark bg
- Headline: "Great Food. Smart Savings. Better Planet." (gradient text)
- Subhead: "Jago Hemat rescues surplus food from top restaurants & stores — up to 80% off. Good for you, good for the planet."
- Store locator: input field + "Find Deals →" button
- Dual badges: "Google Play" + "App Store" buttons (real download links or jagohemat.com/app)
- Live counter badge: "🔥 847 meals available near you" (animated)
- Hero image on right: use hero-illustration.png or phone-mockup.png
- Floating badges: "Up to 80% off" | "100% Safe" | "200+ Stores"
- Background: animated green particles (CSS keyframes)
- Animated grid overlay (subtle)

### 3. SOCIAL PROOF BAR (DARK)
- Scrolling marquee: "⭐ 4.8 App Store" | "🏆 Top 10 Food App 2025" | "500K+ Meals Saved"
- Stats row: "500K+" | "200+" | "Rp 1.2B+" — large animated number counters
- Partner logos scrolling strip (use emoji or placeholder boxes if no logos)

### 4. HOW IT WORKS (LIGHT)
- Section label: "Bagaimana Cara Kerjanya?" / "How It Works"
- 3-step horizontal flow with numbered circles (1, 2, 3) and connecting animated lines
- Step 1: "Temukan Promo Terdekat" / "Find Nearby Deals" — map icon
- Step 2: "Pesan Tas Makanan" / "Reserve Your Bag" — shopping bag icon
- Step 3: "Ambil & Nikmati" / "Pick Up & Enjoy" — smile/person icon
- Trust badges: "100% Aman" | "Toko Terverifikasi" | "Garansi 30 Hari"
- Animated arrow connectors between steps
- CTA: "Mulai Sekarang →" / "Get Started →"

### 5. FEATURED DEALS (LIGHT)
- Section header: "🔥 Promo Tersedia Sekarang" / "🔥 Deals Near You Right Now"
- Filter tabs: Semua | Restoran | Bakery | Grocery | Minimarket
- 6 deal cards in responsive grid (3 col desktop, 2 tablet, 1 mobile)
- Each card:
  - Store image placeholder (emerald gradient with icon)
  - Store name + category badge
  - "Original price" struck through + Jago Hemat price (green, bold)
  - "X tas tersisa" / "X bags left" badge (amber)
  - Countdown timer ("Berakhir dalam 2j 34m") — live JS countdown
  - Hover: lift + glow effect
- CTA below grid: "Lihat Semua Promo →" / "See All Deals →"

### 6. IMPACT DASHBOARD (DARK)
- Full-width dark section
- Large animated counters (count-up on scroll):
  - "1,247,839" → "meals rescued"
  - "Rp 3.4B+" → "saved by users"
  - "892 tons" → "CO₂ avoided"
- Personal impact prompt: "Lihat dampak Anda →" / "See your impact →"
- Impact card image (from assets/impact-card.png)
- "Share your impact" button → generates shareable text for WhatsApp

### 7. WHY JAGO HEMAT (LIGHT)
- Bento grid comparing: Jago Hemat vs GrabMart vs GoFood vs Self-checkout
- Value props in cards:
  - "Harga Lebih Murah" / "Up to 80% off"
  - "Makanan Aman & Segar" / "Safe & fresh"
  - "Mudah & Cepat" / "Quick & easy"
  - "Dampak Lingkungan" / "Planet-positive"
- Each with icon, title, short description

### 8. TESTIMONIALS (DARK)
- Auto-scrolling carousel (4 cards)
- Real names, real Indonesian cities:
  - "Emma Chen — Jaksel, Jakarta" | "Budi Santoso — Bandung" | "Rina Wijaya — Surabaya" | "Andi Pratama — Bali"
- Star ratings + verified badges
- Specific quotes with metrics: "Saved Rp 400K in 2 weeks"
- Navigation: prev/next arrows + dot indicators

### 9. FOR BUSINESS OWNERS (LIGHT)
- Split layout: left = copy, right = sign-up form
- Headline: "Ubah Sisa Menu Jadi Penghasilan" / "Turn Surplus Into Revenue"
- Subhead: "Jago Hemat membantu toko Anda menjual makanan berlebih — tanpa effort, tanpa biaya di awal."
- Merchant form fields: Nama Toko, Email, WhatsApp, Jenis Toko (dropdown)
- Submit button: "Daftar Sekarang — Gratis!" (links to WhatsApp: wa.me/62...)
- ROI mini-calculator: input "Rata-rata makanan terbuang per hari (kg)" → output "Potensi kehilangan: Rp X/bulan"
- Trust: "5-Menit Setup" | "Tanpa Komitmen" | "Garansi 30 Hari"
- Testimonial: merchant quote

### 10. APP DOWNLOAD CTA (DARK)
- Full-width conversion section
- Phone mockup on left (from assets/phone-mockup.png)
- "Join 100,000+ smart shoppers" social proof
- App Store + Google Play download buttons (prominent, styled)
- Pulsing green CTA button: "Download Gratis Sekarang"
- Floating green glow animation behind phone

### 11. FAQ (LIGHT)
- Accordion with 8 questions
- FAQ #1 (highlighted): "Apakah makanan tetap aman dimakan?" — answer: "Absolutely. Semua makanan yang dijual melalui Jago Hemat masih dalam masa berlaku dan telah diverifikasi aman untuk dikonsumsi oleh tim kami. Label tanggal kadaluarsa selalu dicantumkan."
- Other questions:
  - "Bagaimana cara mengambil pesanan?" → Pickup process explanation
  - "Bagaimana jika saya tidak puas?" → Refund policy
  - "Berapa banyak yang bisa saya hemat?" → Savings explanation
  - "Apakah Jago Hemat tersedia di kota saya?" → City availability
  - "Bagaimana cara toko bergabung?" → Merchant signup
  - "Apakah ada biaya tersembunyi?" → No hidden fees

### 12. FOOTER
- Logo + tagline
- Links: About | How It Works | For Business | Privacy | Terms
- App Store + Google Play badges
- Social: Instagram | TikTok | WhatsApp
- Contact: hello@jagohemat.com
- Location: Jakarta, Indonesia
- © 2026 Jago Hemat. All rights reserved.

---

## DYNAMIC FEATURES (all JS)

### Language Toggle (EN ↔ ID)
- `<html data-lang="en">` default
- All text elements: `data-lang-en="..." data-lang-id="..."`
- JS: swap visible text instantly on toggle click, no reload
- 127+ translated elements

### Theme Toggle (Dark ↔ Light)
- `<html data-theme="dark">` default
- JS: swap `data-theme` on html element
- CSS: `:root[data-theme="dark"]` and `:root[data-theme="light"]` blocks
- Instant swap, no reload

### Animated Counters
- IntersectionObserver triggers count-up animation when in viewport
- Duration: 2 seconds, ease-out cubic
- Format: locale-appropriate (1,247,839 with commas)

### Scroll Reveal
- `.reveal` class elements fade + slide up on scroll into view
- IntersectionObserver with staggered delay

### Deal Card Countdown Timers
- Each deal card has `data-expires="ISO-DATE"` attribute
- JS calculates time remaining and updates every second
- Format: "Berakhir dalam Xj Xm"

### FAQ Accordion
- Click question → toggle answer with smooth max-height transition
- Only one open at a time
- Plus icon rotates to X on open

### Testimonial Carousel
- Auto-advances every 5 seconds
- Manual: prev/next arrows + dot navigation
- Pauses on hover
- Touch/swipe support (optional but nice)

### Sticky Nav
- Transparent at scroll=0
- `background: rgba(13,13,15,0.85); backdrop-filter: blur(20px)` when scrolled
- Smooth transition

### Mobile Drawer
- Hamburger icon → full-screen overlay drawer
- Links + language/theme toggles inside
- Close on link click or X button

### Particles (Hero background)
- 30 particles, CSS keyframe animation
- Random positions, sizes (2-5px), colors (#10B981 or #06B6D4)
- Float from bottom to top, loop infinitely

---

## DEPLOYMENT
- Save as: `~/work/jago-hemat/index.html`
- Replace existing `landing.html` (can keep as reference, just don't link to it)
- The file must be fully self-contained (all CSS + JS inline)

---

## QUALITY CHECKLIST
- [ ] Dark + light theme toggle works instantly
- [ ] EN ↔ ID language toggle works instantly (all 127+ elements)
- [ ] All 12 sections present and visually distinct
- [ ] Mobile responsive (test at 375px, 768px, 1440px)
- [ ] No dead UI elements — every button has a handler
- [ ] Countdown timers update live
- [ ] Counter animations trigger on scroll
- [ ] Carousel auto-advances and responds to navigation
- [ ] FAQ accordion: smooth, only one open at a time
- [ ] No console errors
- [ ] Images load from relative paths (assets/)
- [ ] Google Fonts load from https://fonts.googleapis.com
- [ ] Page is visually impressive — this must beat Too Good To Go's website
