# Jago Hemat v3 — UX Audit Report

**Date:** 2026-03-31
**Auditor:** Senior UI/UX + Front-end Architecture Audit
**Files:** `index.html`, `style.css`
**Live:** http://localhost:7894/
**Design direction:** Premium Eco-Commerce — dark/charcoal + emerald green (#01875f) + urgency orange (#FF8642), Nunito font

---

## EXECUTIVE SUMMARY

The v3 landing page is visually impressive and structurally sound. The CSS architecture is excellent, animations are polished, and content is fully in Indonesian with no lorem ipsum. However, **the EN/ID language toggle is a stub** (toggles a button label but translates zero text), **several CTAs are dead `href="#"` links**, and the **deal countdown timers reset on every page load** rather than counting down to real expiry times.

**Overall Quality: 🟡 Should Fix before launch**
Critical issues: 3 | Should Fix: ~10 | Nice-to-Have: ~6

---

## A. COMPLETENESS CHECK

### ✅ What's Present (Good)
- All sections have real, well-written Indonesian content — no lorem ipsum anywhere
- Hero stats are compelling and specific (14.7 JT ton, 44% edible, 80% savings)
- Deal cards have real merchant names, realistic prices, and contextual Unsplash images
- Testimonials are believable with location + tenure metadata + savings amounts
- FAQ has 8 comprehensive questions with full, natural answers
- Merchant form has all required fields, WhatsApp integration, ROI calculator
- All navigation anchor links are valid (`#how`, `#deals`, `#impact`, `#merchant`, `#testimonials`, `#download`, `#merchant-form`)
- Footer has realistic nav structure, social links, brand info
- All Unsplash image URLs appear valid and contextually appropriate

### 🔴 Critical — Dead CTA Links

**1. App Store + Google Play buttons (Download section)**
```html
<!-- BROKEN — both href="#" -->
<a href="#" class="store-btn">
  <div class="store-btn-icon">&#63749;</div>
  <div class="store-btn-text"><span>Download on the</span><strong>App Store</strong></div>
</a>
<a href="#" class="store-btn">
  <div class="store-btn-icon">&#127934;</div>
  <div class="store-btn-text"><span>Get it on</span><strong>Google Play</strong></div>
</a>
```
**Fix:** Replace `href="#"` with real App Store / Play Store URLs, or use placeholder `href="https://play.google.com/store/apps/details?id=com.jagohemat.app"` and `href="https://apps.apple.com/app/jago-hemat"` (verify actual IDs).

**2. Merchant CTA ("Daftar Gratis — 5 Menit Saja")**
```html
<!-- BROKEN — href="#" in .merchant section -->
<a href="#" class="btn btn-primary btn-lg">&#128222; Daftar Gratis — 5 Menit Saja</a>
```
**Also broken:**
```html
<a href="#" class="btn btn-ghost">&#128196; Download Sample Report</a>
```
**Fix:** Both should link to `#merchant-form` (the form section below).

**3. "Bagikan Impact Card" (Impact section)**
```html
<!-- BROKEN — href="#" -->
<a href="#" class="btn btn-ghost">&#128247; Bagikan Impact Card</a>
```
**Fix:** Implement Web Share API or canvas-based shareable card, or link to `#impact`.

**4. Footer placeholder links** — many `href="#"` links in footer:
```html
<li><a href="#">Dashboard</a></li>
<li><a href="#">ESG Report</a></li>
<li><a href="#">Tentang Kami</a></li>
<li><a href="#">Blog</a></li>
<li><a href="#">Karir</a></li>
```
Acceptable as pre-launch placeholders; flag for before public launch.

### 🔴 Critical — Hero Badge Animation Targets Non-existent Element

```javascript
// JS tries to animate #heroBadge — but the HTML has .hero-eyebrow, NOT #heroBadge
var badgeEl = document.getElementById("heroBadge");
if (badgeEl) {  // ← silently does nothing, badge never rotates
  var bi = 0;
  setInterval(function() {
    bi = (bi + 1) % badges.length;
    badgeEl.style.opacity = "0";
    setTimeout(function() {
      badgeEl.innerHTML = badges[bi];
      badgeEl.style.opacity = "1";
    }, 200);
  }, 3500);
```

The HTML shows `<div class="hero-eyebrow reveal">` with a static `<span class="badge badge-orange">` inside — there is no `#heroBadge` element. The feature silently fails.

**Fix:** Add `id="heroBadge"` to the `<span class="badge badge-orange">` element, OR remove the dead JS block entirely.

### 🟡 Should Fix — Deal Discount % Inconsistent with Fill Bar

```javascript
// In deal card HTML generation:
'<span class="deal-sold">-'+Math.round(100-((d.left/10)*100))+'%</span>'
```

The `left/10` formula gives discount based on assumed stock (3 left = 70% off), but the `fill` data field is independent (e.g., `left:3, fill:85` means the bar says 85% sold but discount shows 70%). These should be consistent.

**Fix:** Derive discount percentage from actual price comparison:
```javascript
var origNum = parseInt(d.orig.replace(/[^0-9]/g, ''));
var priceNum = parseInt(d.price.replace(/[^0-9]/g, ''));
var discountPct = Math.round(100 - (priceNum / origNum * 100));
```

---

## B. UI/UX AUDIT

### ✅ Strengths
- **Visual hierarchy is strong** — hero title clamp(36–72px), bold orange/green CTAs, scannable stats
- **Color system is cohesive** — dark bg + emerald + orange urgency well-executed throughout
- **Cards have premium feel** — border + shadow + hover transforms
- **Trust signals** prominently placed (4.8 stars, 500K downloads, 10JT+ kg saved)
- **Section tags** provide clear wayfinding (emoji + label, consistent)
- **FAQ accordion** well-designed with green accent on featured item
- **Sticky CTA bar** appears at right scroll depth (after 60% of hero)
- **Whitelabel branding** — emoji logo fallback (🥊) works when image missing
- **`clamp()` used extensively** for fluid typography and spacing — excellent

### 🟡 Should Fix — Mobile

**Floating controls overlap sticky CTA on mobile** — At `bottom:24px; right:24px`, the 48×48px floating control buttons compete with the sticky CTA bar on phones. At ≤640px: reduce floating controls to 40×40px, or hide lang/theme (keep only scroll-to-top).

**Hero image CLS risk** — `height: clamp(280px, 45vw, 480px)` doesn't lock aspect ratio. Add `aspect-ratio: 4/3;` to prevent layout shift on slow loads.

### 🟢 Nice-to-Have
- Countdown timers show `--:--` before JS runs — consider inline SSR render of initial time
- "Bagikan Impact Card" should generate a shareable image (canvas API)
- App Store badges could use official SVG badge assets

---

## C. ANIMATION AUDIT

### Every Animation Listed

| # | Animation | Element | Trigger | Quality |
|---|-----------|---------|---------|---------|
| 1 | Fade + slide up | `.reveal` | IntersectionObserver (0.12) | ✅ Enhance |
| 2 | Scale in | `.reveal-scale` | IntersectionObserver | ✅ Enhance |
| 3 | Stagger delays 1–7 | CSS transition-delay | On reveal | ✅ Enhance |
| 4 | Pulse dot | `.pulse-dot` | CSS infinite | ✅ Enhance |
| 5 | Floating cards | `.float-card-1, -2` | CSS keyframe `floatCard` | ✅ Enhance |
| 6 | Scroll indicator dot | `.scroll-indicator-dot` | CSS keyframe | ✅ Enhance |
| 7 | Counter animation | `.impact-val`, `.ibs-val`, `.esg-stat-val` | IntersectionObserver | ✅ Enhance |
| 8 | Parallax hero bg | `.hero-bg` | Scroll (0.3×) | 🟡 Neutral |
| 9 | Referral bg parallax | `.referral::before` | CSS `var(--scroll-y)` | 🟡 Neutral |
| 10 | Scroll progress bar | `#scrollProgress` | Scroll | ✅ Enhance |
| 11 | Nav glass morphism | `.nav` → `.nav.scrolled` | Scroll >40px | ✅ Enhance |
| 12 | Sticky CTA slide up | `.sticky-cta` | Scroll >60% hero | ✅ Enhance |
| 13 | Nav active state | `.nav-links a` | IntersectionObserver | 🟡 Neutral |
| 14 | Deal card 3D tilt | `.deal-card` | Mousemove | 🟡 Neutral |
| 15 | Deal card hover | `.deal-card:hover` | CSS transform | ✅ Enhance |
| 16 | Deal stagger reveal | `.deal-card` | setTimeout 100ms | ✅ Enhance |
| 17 | Marquee | `.testi-track` | CSS 30s loop | ✅ Enhance |
| 18 | Button shine sweep | `.btn-orange::after` | CSS hover | ✅ Enhance |
| 19 | FAQ icon rotate | `.faq-icon` | CSS transition | ✅ Enhance |
| 20 | How-step hover lift | `.how-step:hover` | CSS transform | ✅ Enhance |

**Animation Quality Rating: 8/10** — Well-crafted overall. Two bugs bring it from 9/10.

### 🔴 Broken — Hero Badge Rotator

`document.getElementById("heroBadge")` returns `null`. Dead JS. See Section A.

### 🔴 Broken — Deal Discount Inconsistency

Fill bar and discount % use different data sources. See Section A.

### 🟡 CLS Risks

- **Hero image** — `height: clamp(280px, 45vw, 480px)` without aspect-ratio lock → potential CLS on load
- **Font loading** — `display=swap` on Google Fonts → no CLS ✅
- **No layout shift on scroll reveals** — all use opacity + transform ✅

---

## D. ARCHITECTURE AUDIT

### JS Structure Overview

Single `<script>` block (~250 lines) with:
1. **First IIFE** — deals, timers, nav scroll, drawer, theme, language, smooth scroll, hero badge
2. **Global functions** — `toggleFaq`, `updateROI`, `submitMerchantForm`
3. **Second IIFE (PREMIUM INTERACTIONS)** — scroll progress, sticky CTA, nav active, referral fill, deal tilt, enhanced counter, parallax, scroll reveal

### 🟡 Redundancy — `animateCounter` Defined Twice

```javascript
// First IIFE (first definition — dead code):
function animateCounter(el,target,suffix,duration){ /* basic */ }

// Second IIFE (overwrites first — keep this):
function animateCounter(el, target, suffix, duration) { /* enhanced, handles Rp prefix + decimals */ }
```

**Fix:** Delete the first definition entirely.

### 🟡 Redundancy — Parallax Set Up Twice (Identical)

```javascript
// First IIFE:
window.addEventListener('scroll', function(){
  var heroBg = document.querySelector('.hero-bg');
  if (heroBg) heroBg.style.transform = 'translateY(' + (sy * 0.3) + 'px)';
  document.documentElement.style.setProperty('--scroll-y', sy + 'px');
}, {passive:true});

// Second IIFE (duplicate — remove):
window.addEventListener('scroll', function() {
  var heroBg = document.querySelector('.hero-bg');
  if (heroBg) heroBg.style.transform = 'translateY(' + (sy * 0.3) + 'px)';
  document.documentElement.style.setProperty('--scroll-y', sy + 'px');
}, {passive:true});
```

Both fire on every scroll tick doing identical work. **Fix:** Remove the first one.

### 🟡 Redundancy — `revealObs` IntersectionObserver Set Up Twice

First IIFE creates `revealObs`, observes `.reveal/.reveal-scale` + deal cards. Second IIFE creates a second `revealObs` (same variable name via `var` hoisting) and re-observes all `.reveal/.reveal-scale`. The second one shadows the first. These should be merged.

### 🟡 Redundancy — `counterObs` IntersectionObserver Set Up Twice

Same pattern as above. Keep the second (enhanced) version, remove the first.

### ✅ CSS Architecture — Excellent

- **CSS Custom Properties** for all design tokens ✅
- **No `!important` abuse** — only acceptable implicit use via `[data-theme]` cascade ✅
- **`clamp()` used extensively** for fluid typography/spacing ✅
- **Dark/light theme via `[data-theme]`** — clean and maintainable ✅
- **Logical CSS ordering**: reset → tokens → layout → components → utilities → responsive ✅

### ✅ IntersectionObserver — Scroll Reveal (Correct)

```javascript
var revealObs = new IntersectionObserver(function(entries) {
  entries.forEach(function(e) {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObs.unobserve(e.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
```
Correct — unobserves after reveal (performance), reasonable threshold, bottom buffer. ✅

### 🟡 Accessibility Issues

**Contrast — dark mode muted text:**
```css
[data-theme=dark]{ --text-muted:#888 }
```
`#888` on `#0D0D0F` = ~4.5:1, which is **at the boundary of WCAG AA**. Small text like `.hero-stat-lbl`, `.deal-merchant`, `.lb-score` may fail for small sizes. **Fix:** Change to `#999` or `#aaa`.

**FAQ keyboard accessibility (broken):**
```html
<!-- onclick on div — not keyboard accessible, no ARIA -->
<div class="faq-q" onclick="toggleFaq(this)">
```
No `role="button"`, no `tabindex="0"`, no `aria-expanded`, no `aria-controls`.

**Fix:**
```html
<div class="faq-q" role="button" tabindex="0" aria-expanded="false"
     onclick="toggleFaq(this)"
     onkeydown="if(event.key==='Enter'||event.key===' '){toggleFaq(this);event.preventDefault()}">
```

**Theme/language toggles missing ARIA:**
```html
<button class="icon-btn" id="themeToggle" title="Ganti Tema">&#9790;</button>
<button class="icon-btn" id="langToggle" title="Ganti Bahasa">&#127760;</button>
```
Add `aria-label` (dynamic) and `aria-pressed` state updated by JS.

**No skip-to-content link** — a page this long should have one for keyboard users.

### 🟢 Performance Notes

- All scroll listeners use `{ passive: true }` ✅
- Hero image should have `loading="eager"` + `fetchpriority="high"` (it's above the fold)
- Deal card images injected via JS should have `loading="lazy"` added in template string
- CSS transitions on hover use GPU-accelerated properties (transform, opacity) ✅

---

## E. EN/ID TOGGLE IMPLEMENTATION AUDIT

### 🔴 Critical — Toggle Does Nothing

```javascript
var langs = {id:"EN", en:"ID"};

function setLang(l) {
  lang = l;
  localStorage.setItem("jh-lang", l);
  document.getElementById("langToggle").textContent = langs[l];
  var fcLang = document.getElementById("fcLang");
  if (fcLang) fcLang.textContent = langs[l];
}
```

**Percentage translated: 0%**

Every visible string is hardcoded Indonesian. The toggle only changes the button label. The floating control also updates. Nothing else.

### 🟡 Recommended Implementation Approaches (ranked)

**Option 1 — `data-i18n` attributes + JSON dictionary (Recommended)**
```html
<span data-i18n="hero.title">Indonesia #1 Food Waste di ASEAN...</span>
```
```javascript
var translations = {
  id: { "hero.title": "Indonesia #1 Food Waste di ASEAN...", "hero.sub": "..." },
  en: { "hero.title": "Indonesia <span class='hl-y'>#1 Food Waste</span> in ASEAN...",
        "hero.sub": "14.7 million tons of food wasted every year..." }
};
function translate(lang) {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    el.innerHTML = translations[lang][el.dataset.i18n];
  });
}
```
**Pros:** Clean separation, easy maintenance, SEO-friendly, scalable
**Cons:** Requires tagging ~60–80 elements
**Effort:** ~2–3 hours

**Option 2 — Google Translate widget**
Drop in the official Google Translate widget. Free, instant, full coverage.
**Pros:** Zero dev effort
**Cons:** Ugly widget, poor UX, SEO duplicate content
**Effort:** 10 minutes

**Option 3 — Separate static files (en/index.html, id/index.html)**
Build-time generation of two HTML files.
**Pros:** Best SEO, full control
**Cons:** Maintenance doubles
**Effort:** Requires build pipeline

### Recommendation

Use **Option 1** for a landing page this size. The effort (~2–3h) is reasonable and gives full EN translations that can be refined. Key strings to translate: hero title/subtitle, CTAs, deal section header, impact stats labels, merchant value props, testimonials, FAQ questions and answers.

**Minimum action for launch:** Hide `#langToggle` and `#fcLang` with `display:none` until translations are ready. Don't show a feature that doesn't work.

---

## PRIORITIZED ACTION LIST — Top 10

### 🔴 Critical (Fix before any launch)

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| 1 | **Dead app store links** | `#download .store-btn` | Replace `href="#"` with real App Store + Play Store URLs |
| 2 | **Dead merchant CTAs** | `.merchant` section | Change `href="#"` → `href="#merchant-form"` for both buttons |
| 3 | **Hero badge animation dead** | JS block `// ===== HERO BADGE ANIMATION =====` | Add `id="heroBadge"` to `<span class="badge badge-orange">` OR delete dead JS |
| 4 | **Deal discount % inconsistent** | JS deal card HTML generation | Derive discount from price math, not `left` count. Match fill bar to discount %. |
| 5 | **EN/ID toggle does nothing** | `#langToggle`, `#fcLang` | Hide toggle (`display:none`) until Option 1 `data-i18n` is implemented |

### 🟡 Should Fix (Fix before marketing push)

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| 6 | **Duplicate JS functions** | Two IIFEs in `<script>` | Remove first `animateCounter`, first parallax listener, merge revealObs/counterObs |
| 7 | **FAQ not keyboard accessible** | `.faq-q` divs | Add `role="button" tabindex="0" aria-expanded` + keyboard handler |
| 8 | **Toggle buttons missing ARIA** | `#themeToggle`, `#langToggle` | Add dynamic `aria-label` and `aria-pressed` |
| 9 | **Dark mode muted contrast** | CSS `[data-theme=dark]{--text-muted:#888}` | Change to `#999` or `#aaa` |
| 10 | **Hero image CLS risk** | `.hero-img-wrap img { height: clamp(...) }` | Add `aspect-ratio: 4/3` to lock dimensions |

### 🟢 Nice-to-Have (Polish pass)

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| 11 | "Bagikan Impact Card" dead | `.impact-big .btn-ghost` | Implement Web Share API or canvas card |
| 12 | Floating controls on mobile | `.floating-controls` | At ≤640px, reduce size or hide lang/theme |
| 13 | Hero image eager load | `.hero-img-wrap img` | Add `loading="eager" fetchpriority="high"` |
| 14 | Deal images lazy load | JS template string | Add `loading="lazy"` to img elements |
| 15 | No skip-to-content link | `<body>` | Add `<a class="sr-only" href="#hero">Skip to content</a>` |
| 16 | Nav active lacks ARIA | `.nav-links a.active` | Add `aria-current="page"` |

---

## APPENDIX — Quick Fix Snippets

### Fix 1: Hero Badge Element ID
```html
<!-- Find: -->
<span class="badge badge-orange">&#127942; Indonesia #1 Food Waste in ASEAN</span>
<!-- Change to: -->
<span id="heroBadge" class="badge badge-orange">&#127942; Indonesia #1 Food Waste in ASEAN</span>
```

### Fix 2: FAQ Keyboard Accessible Version of `toggleFaq`
```javascript
function toggleFaq(el) {
  const item = el.closest(".faq-item");
  const isOpen = item.classList.toggle("open");
  el.setAttribute("aria-expanded", isOpen);
}
```
Then update each `.faq-q` div:
```html
<div class="faq-q" role="button" tabindex="0" aria-expanded="false"
     onclick="toggleFaq(this)"
     onkeydown="if(event.key==='Enter'||event.key===' '){toggleFaq(this);event.preventDefault()}">
```

### Fix 3: Hide Language Toggle Until Translations Exist
```css
#langToggle, #fcLang { display: none; }
```

### Fix 4: Hero Image CLS Fix
```css
.hero-img-wrap img {
  /* Replace: */
  height: clamp(280px, 45vw, 480px);
  /* With: */
  aspect-ratio: 4 / 3;
  height: auto;
  max-height: 480px;
  width: 100%;
  object-fit: cover;
}
```

### Fix 5: Dark Mode Muted Text Contrast
```css
/* In [data-theme=dark] block, change: */
--text-muted:#888;
/* To: */
--text-muted:#aaa;
```

---

*Audit completed: 2026-03-31*
