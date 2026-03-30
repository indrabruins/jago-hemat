# RFC-001: Jago Hemat Website Redesign
**Status:** ACTIVE | **CEO:** Kit | **Date:** 2026-03-29

---

## 1. Problem Statement

jagohemat.com (live) lacks urgency, social proof, conversion hooks, and modern design. Competitors (Too Good To Go, Flashfood) are winning on UX and social proof. Jago Hemat's site must become a conversion machine — compelling users to download the app and merchants to sign up.

---

## 2. Product Vision

**"The food deal app that feels like finding buried treasure."**

- Emotion: excitement, discovery, mission, savings
- Aesthetic: premium food photography + eco-conscious design language
- Dual themes: **Dark** (premium/mission feel) + **Light** (fresh/grocery feel)
- Bilingual: EN + ID (language toggle in nav)

---

## 3. Themes

### Dark Theme (Primary — used for hero/impact sections)
```
--bg: #0D0D0F
--card: #1A1A1E
--surface: #252529
--accent: #10B981 (emerald green — the Jago Hemat brand color)
--accent-secondary: #06B6D4 (cyan for contrast)
--warning: #F59E0B (amber for urgency/scarcity)
--text: #FFFFFF
--text-muted: #9CA3AF
--text-dark: #6B7280
--border: rgba(255,255,255,0.08)
--gradient: linear-gradient(135deg, #10B981, #06B6D4)
```

### Light Theme (secondary — used for deal cards/food sections)
```
--bg: #FAFAF9
--card: #FFFFFF
--surface: #F3F4F6
--accent: #10B981
--accent-secondary: #059669
--warning: #D97706
--text: #111827
--text-muted: #6B7280
--text-dark: #9CA3AF
--border: rgba(0,0,0,0.08)
--gradient: linear-gradient(135deg, #10B981, #06B6D4)
```

---

## 4. Typography

- **Headings:** Poppins (600, 700, 800) — warm, friendly, modern
- **Body:** Inter (400, 500, 600) — clean, readable
- **Accent/Numbers:** Poppins (800) for impact stats

---

## 5. Sections (Consumer-First)

### Section 1: Sticky Nav
- Logo (preserve — from jagohemat.com)
- Links: How It Works | Deals | Impact | For Business
- Language toggle: EN | ID
- Theme toggle: 🌙 | ☀️
- CTA: "Download App" (primary green button)
- Mobile: hamburger drawer

### Section 2: Hero (Dark Background)
- **Above fold — 100vh**
- Headline: *"Makanan Enak, Harga Hemat."* / *"Great Food, Smart Savings."*
- Subhead: *"Jago Hemat rescues surplus food from top restaurants & stores — up to 80% off. Good for you, good for the planet."*
- **Store locator input** (ZIP/kelurahan) — real-time nearby deals
- CTA buttons: Google Play + App Store (BOTH, prominently)
- **Live counter:** "X meals available near you right now" (animated)
- Hero image: collage of food items, person picking up bag, store atmosphere
- Floating badges: "Up to 80% off", "Save the planet", "Fresh & safe"
- Background: subtle animated particles (green + amber)

### Section 3: Social Proof Bar (Dark)
- Animated scrolling logos of partner stores (if available)
- Stats row: "500K+ meals saved" | "200+ partner stores" | "Rp 1.2B+ saved by users"
- Scrolling marquee: "⭐ 4.8 App Store rating" | "🏆 Top 10 Food App 2025"

### Section 4: How It Works (Light Background)
- 3-step horizontal flow with icons + illustrations
- Step 1: "Find nearby deals" (map + phone illustration)
- Step 2: "Reserve your bag" (bag + checkmark illustration)
- Step 3: "Pick up & enjoy" (person with bag + smile illustration)
- Animated arrow connectors between steps
- Trust badges: "100% safe" | "Verified stores" | "Easy refund"

### Section 5: Featured Deals (Light Background)
- "🔥 Near You Right Now" — urgency grid
- 4-6 deal cards showing: store photo, food type, original price strikethrough, Jago Hemat price, "X bags left" badge, countdown timer
- Filter tabs: All | Restaurants | Bakeries | Groceries | Convenience
- "Load more" / infinite scroll
- Each card links to app (deep link)

### Section 6: Impact Dashboard (Dark Background)
- Full-width emotional section
- Large animated counters: "1,247,839 meals rescued" | "Rp 3.4B saved" | "892 tons CO₂ avoided"
- Personal impact prompt: "See your impact →" (logged-in feel)
- Shareable impact card: "I saved X meals with Jago Hemat"
- Map showing countries/cities covered

### Section 7: Why Jago Hemat (Light Background)
- Bento grid comparing: Jago Hemat vs other options
- Cards: App Store rating comparison, price comparison, store count comparison
- Customer quote: "Best Rp 25K I ever spent" style

### Section 8: Testimonials (Dark Background)
- 4-5 carousel cards
- Real names, Jaksel/Surabaya/Bandung locations, profile photos
- Specific metrics: "Saved Rp 400K in 2 weeks", "Found amazing bakery near me"
- Star ratings + verified badges

### Section 9: For Business Owners (Light Background)
- **Separate audience section** — split design
- Left: Merchant value prop ("Turn surplus into revenue")
- Right: Sign-up form (business name, email, WhatsApp, store type)
- ROI calculator: "Calculate your monthly waste loss →" (input: avg daily waste kg × price/kg)
- Merchant testimonials from small business owners
- "5-minute setup" badge

### Section 10: App Download CTA (Dark Background)
- Full-width conversion section
- Phone mockup showing the app
- QR code for both stores
- "Join 100K+ smart shoppers" social proof
- Pulsing green CTA button

### Section 11: FAQ (Light Background)
- Accordion, 6-8 questions:
  - "Is the food safe to eat?" ← #1 objection, answer prominently
  - "What types of food are available?"
  - "How do I pick up my order?"
  - "Can merchants sign up?"
  - "What's your refund policy?"
  - "How much can I save?"
  - "Do you deliver or is it pickup only?"
  - "Is Jago Hemat available in my city?"

### Section 12: Footer
- Logo + tagline
- Links: About, How It Works, For Business, Privacy, Terms
- Download: App Store + Google Play badges
- Social: Instagram, TikTok, WhatsApp
- Contact: hello@jagohemat.com
- Legal: © 2026 Jago Hemat

---

## 6. Dynamic Features

| Feature | Description |
|---------|-------------|
| Language toggle | EN / ID — all text swaps instantly, no reload |
| Theme toggle | Dark / Light — CSS variable swap, no reload |
| Animated counters | Count-up on scroll for impact stats |
| Urgency badges | "X bags left" on deal cards, live-feel |
| Countdown timers | On flash deals |
| Marquee | Scrolling partner logos + social proof |
| Scroll reveal | Staggered entrance animations |
| Deal card hover | Lift + glow effect |
| Store locator | ZIP/kelurahan input → nearby deals |
| FAQ accordion | Smooth expand/collapse |
| Testimonial carousel | Auto-advance + manual swipe |
| Mobile drawer | Hamburger nav for mobile |
| Sticky header | Transparent → solid on scroll |

---

## 7. Graphics to Generate

| Asset | Description |
|-------|-------------|
| Hero collage | Flat illustration of food bags, phone with app, store |
| Step 1 icon | Map + location pin |
| Step 2 icon | Shopping bag with heart |
| Step 3 icon | Person happy with grocery bag |
| Food category icons | Restaurant, bakery, grocery, convenience (4 icons) |
| Impact icons | Meal rescue, CO₂ leaf, coin stack |
| Deal card illustrations | Placeholder food images (AI-generated realistic) |
| Phone mockup | App UI on phone frame |
| App Store badge | Styled download button |
| Google Play badge | Styled download button |
| Impact share card | Social-media-ready impact summary card |

---

## 8. Technical Approach

- **Single HTML file** (index.html) with JS for all interactivity
- **No framework** — vanilla HTML/CSS/JS
- **Tailwind CSS** via CDN
- **Lucide Icons** via CDN
- **Poppins + Inter** fonts via Google Fonts
- **Language toggle:** `data-lang-en` / `data-lang-id` attributes + JS swap
- **Theme toggle:** `data-theme="dark"` / `data-theme="light"` on `<html>` + CSS variables
- **Form submissions:** WhatsApp/email link (no backend needed)
- **Deep links:** `jagohemat://` protocol + App Store redirect fallback

---

## 9. Content Strategy — EN/ID

### Hero Headline
- EN: "Great Food. Smart Savings. Better Planet."
- ID: "Makanan Enak. Harga Hemat. Bumi Lebih Baik."

### Subhead
- EN: "Jago Hemat rescues surplus food from top restaurants & stores — up to 80% off. Good for you, good for the planet."
- ID: "Jago Hemat menyelamatkan makanan berlebih dari restoran & toko terbaik — hingga 80% lebih murah. Baik untuk Anda, baik untuk bumi."

### CTA
- EN: "Find Deals Near You →"
- ID: "Cari Promo Terdekat →"

---

## 10. Mobile-First Breakpoints

- Mobile: < 640px (1 column, stacked)
- Tablet: 640px – 1024px (2 columns where applicable)
- Desktop: > 1024px (full layout)

---

## 11. Performance

- Lazy load images
- No external JS dependencies (except Tailwind CDN)
- Intersection Observer for all scroll animations
- Debounced theme/language toggles
- Target: < 3s load on 4G

---

## 12. Git / Deployment

- Repo: `~/work/jago-hemat/`
- GitHub Pages or Vercel deploy from `index.html`
- Assets in `assets/` folder
- Note: `landing.html` (old) to be replaced with `index.html`

---

## 13. Milestones

- [x] RFC written
- [ ] Assets generated (logo placement + new graphics)
- [ ] Design: Dark theme screens via Stitch
- [ ] Design: Light theme screens via Stitch
- [ ] Code: Full `index.html` with all features (Claude Code)
- [ ] QA + browser test
- [ ] Deploy to jagohemat.com
