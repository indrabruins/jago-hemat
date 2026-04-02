# Jago Hemat v3 — Light Theme Build

## Mission
Create a **light theme variant** of the existing v3 dark landing page (`index.html`).
The dark version is fully functional — replicate it exactly, flip the theme.

## Files
- **Source (dark):** `index.html` + `style.css` (current working dark version)
- **Output:** `index.light.html` + `style.light.css` (new light variant)
- **Assets dir:** `assets/` (existing logos, icons — reuse everything)

## Theme Switching Strategy
The dark version uses `data-theme="dark"` on `<html>` with CSS custom properties.
Create a parallel `style.light.css` that sets `[data-theme="light"]` variables.
The light HTML file should default to `data-theme="light"` and include the theme-toggle JS logic from the original.

## What to Change

### 1. CSS Variables (light overrides)
Map each `--dark-*` variable to its light equivalent:

```
--bg-primary:   #FFFFFF
--bg-secondary: #F8FAF5        (warm off-white, slight green tint)
--bg-card:      #FFFFFF
--bg-section-alt: #F4F6F0      (very light sage)
--text-primary: #1A1A1A
--text-secondary: #555555
--text-muted:   #999999
--border:       rgba(0,0,0,0.08)
```

### 2. Light-specific overrides (not just variable flips)
- **Navbar:** `.nav.scrolled` → `background: rgba(255,255,255,0.96)` + `box-shadow: 0 2px 24px rgba(0,0,0,0.10)`
- **Cards:** Subtle `box-shadow: 0 2px 12px rgba(0,0,0,0.06)` instead of dark borders
- **Hero:** `background: #FFFFFF` with a warm `#F8FAF5` accent section
- **Merchant dark ESG panel:** Convert to light — green gradient on white card
- **Referral section:** Light background `#F8FAF5` with green text instead of dark
- **Footer:** `background: #1A1A1A` (stay dark for contrast)
- **Buttons:** `btn-ghost` dark-theme → in light mode use `background:rgba(0,0,0,0.06)` + `border:1px solid rgba(0,0,0,0.12)`

### 3. HTML Changes
- `<html lang="id" data-theme="light">` (default to light)
- Toggle button: light starts with moon icon → switches to `data-theme="dark"`
- Use same JS logic, just swap initial theme state

### 4. Preserved Features (must work exactly)
- Theme toggle (light ↔ dark)
- EN/ID language toggle
- Scroll reveal animations
- Deal countdown timers
- FAQ accordion
- Merchant form + ROI calculator
- Referral progress bar
- Social proof toast
- Sticky CTA bar
- All responsive breakpoints
- Deal card tilt on hover

## Quality Checklist
- [ ] Page loads without JS errors
- [ ] Theme toggle works: light → dark → light
- [ ] Language toggle works: ID → EN → ID
- [ ] All 6 deal cards render with countdown timers
- [ ] FAQ accordion opens/closes
- [ ] Merchant ROI calculator updates live
- [ ] Scroll animations trigger (reveal on scroll)
- [ ] Navbar scroll state changes correctly
- [ ] Mobile drawer opens/closes
- [ ] Sticky CTA appears after scrolling past hero
- [ ] All Unsplash images load (not broken)
- [ ] Responsive at 900px, 640px, 380px breakpoints

## Reference
Jagohemat.com/en/ content for accuracy:
- 20.93M tons/year Indonesia food waste (UNEP 2021)
- 44% of wasted food still fit for consumption
- 61-125 juta Indonesians lose edible food/year
- Core value props: up to 80% off, quality food, extensive partner network
