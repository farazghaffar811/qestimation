# Qestimation website

Static HTML/CSS/JS site for **Qestimation** (construction estimating services), built as a clone of the layout of biddingenterprise.com.au with the Qestimation logo, navy/copper brand colours, scroll animations and full SEO / AEO / GEO markup.

## Pages
| File | Purpose |
|---|---|
| `index.html` | Home: hero, CTA band, 4 service cards, animated counters, recent works, value-added services, testimonial slider, partner marquee, About facts, FAQ, final CTA |
| `services.html` | Quantity takeoff, cost & budget estimating, cost controls + rebar cost-estimator widget |
| `work-samples.html` | 11 trade estimate samples (PDF viewer + download) |
| `refund-policy.html` | Refund policy, payment options, service disclaimer |
| `sydney-build.html` | Sydney Build Expo photo gallery with lightbox |
| `get-quote.html` | Contact details, quote form with file upload, map, estimator widget |
| `sitemap.xml`, `robots.txt`, `llms.txt`, `site.webmanifest` | SEO / AI-crawler files |

## Before going live – replace the placeholders
All business details live at the top of `_src/build.py`:

- `DOMAIN` – live domain (used for canonical URLs, Open Graph, sitemap, JSON-LD)
- `PHONE`, `PHONE_INTL`, `EMAIL`
- `ADDRESS` – street, city, state, postcode
- `SAME_AS` – real social profile URLs
- `FORM_ENDPOINT` – e.g. a Formspree/Basin/Netlify endpoint. Empty = the form opens the visitor's email client (mailto) instead.

Then regenerate the pages:

```bash
python -I _src/build.py
```

Other content to swap for your own:
- `assets/gallery/*.jpeg` – these are the source company's expo photos (their stand and phone number are visible). Replace with Qestimation photos, then rebuild (thumbnails: see `_src/build.py` notes / regenerate with Pillow).
- `assets/samples/*.pdf` – source company's sample estimates; replace with Qestimation samples (keep the same filenames or edit `SAMPLES` in `build.py`).
- Partner logos in `assets/img/thumbnail_image00*.png|jpg`, `logo-3.png`.
- Testimonial names/quotes, counter numbers and the "Sydney Build" event dates in `build.py`.

## SEO / AEO / GEO included
- Unique title, meta description, keywords, canonical, hreflang (en-AU), robots, geo meta, Open Graph + Twitter cards (OG image `assets/img/og-image.jpg`)
- JSON-LD: ProfessionalService/LocalBusiness/Organization (NAP, hours, areaServed, offer catalog), WebSite, WebPage/CollectionPage/ContactPage/ImageGallery, Service ×4, BreadcrumbList, FAQPage, Event, DigitalDocument per sample
- AEO: FAQ section with direct answers, speakable selectors, "About / key facts" block
- GEO: `llms.txt`, AI crawlers allowed in `robots.txt`, entity-rich plain-language summaries
- Semantic landmarks, alt text on every image, lazy loading, width/height on images, skip link, reduced-motion support

## Local preview
```bash
python -m http.server 8765 --directory qestimation
```
Then open http://localhost:8765/

## Deploy
Upload everything except `_src/` to any static host (cPanel public_html, Netlify, Vercel, GitHub Pages, Cloudflare Pages). Point the domain, then submit `sitemap.xml` in Google Search Console and Bing Webmaster Tools.
