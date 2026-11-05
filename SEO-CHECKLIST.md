# Qestimation – ranking checklist

What is already done on the site (technical + on-page) and what must be done off the site to rank for
"construction estimating services", "quantity takeoff services" and city terms such as
"construction estimating Brisbane".

## Done on the site
- 20 indexable pages: home, services, work samples, blog index, 6 articles, 5 city landing pages, contact, refund, privacy, terms, Sydney Build
- Unique title + meta description per page, canonical, hreflang en-AU, robots, Open Graph, Twitter cards
- Schema.org JSON-LD: LocalBusiness/ProfessionalService, WebSite, Service, FAQPage (home + each city), BlogPosting, BreadcrumbList, CollectionPage, ImageGallery, Event
- Internal linking: nav, footer service-area row, city cards and latest posts on home, related posts, contextual links inside articles
- Speed: hero backgrounds and photos converted to WebP (1.4 MB → 0.7 MB), logo PNGs shrunk 3x, hero image preloaded, lazy loading, cache-busted assets
- `sitemap.xml`, `robots.txt` (AI crawlers allowed), `llms.txt`, web manifest
- HTTPS enforced on qestimation.com, www redirects to root

## Do this week (you)
1. **Replace placeholders** in `_src/build.py` and rebuild: PHONE, EMAIL, ADDRESS, SAME_AS. Google will not trust a LocalBusiness with a fake address and phone, and a Google Business Profile must match the site exactly.
2. **Google Search Console** – https://search.google.com/search-console → Add property → Domain `qestimation.com` → verify by DNS TXT record at GoDaddy (or give me the HTML-tag token and I set `GSC_VERIFICATION`). Then Sitemaps → submit `https://qestimation.com/sitemap.xml`, and use URL Inspection → Request indexing on the home page, services page and each city page.
3. **Bing Webmaster Tools** – https://www.bing.com/webmasters → import from Search Console (one click). Bing powers Copilot and DuckDuckGo.
4. **Google Business Profile** – https://business.google.com → create "Qestimation", category *Construction estimating service* (secondary: *Quantity surveyor*), real address or service-area business, same phone and website. Add logo, 5+ photos, services list and the FAQ answers. This is the single biggest lever for "estimating services near me" and the map pack.
5. **Social profiles** – create the Facebook, LinkedIn and Instagram pages that `SAME_AS` points to, with the same name, logo, description and website link.
6. **Replace borrowed content** – the Sydney Build photos and sample PDFs belong to the source company. Google's duplicate-image detection and a DMCA complaint can both hurt the site. Swap in your own.

## Do this month
7. **Citations / directories** (consistent name, address, phone): Yellow Pages AU, TrueLocal, Hotfrog, Localsearch, StartLocal, Yelp AU, Houzz AU, hipages, Oneflare, ServiceSeeking, ProductReview, Cylex, Brownbook, AussieWeb. Aim for 15–20 in the first month.
8. **Reviews** – ask every finished client for a Google review. 10 reviews with keywords in them ("estimating", "takeoff") move local rankings more than any on-page change.
9. **Backlinks** – realistic sources for an estimating firm: Master Builders / HIA member directories, supplier partner pages, guest articles on construction blogs, Sydney Build / expo exhibitor listings, local chamber of commerce, sponsorship of a trade event, answering questions on Whirlpool / Reddit r/AusProperty with a link where relevant.
10. **Publish 2 articles a month** – add them to `_src/content.py`, rebuild, push. Target long-tail questions: "how to estimate a house build cost", "plasterboard takeoff", "estimating software vs outsourcing", "cost to build per square metre 2026 Brisbane".
11. **Google Analytics 4** – create a property and I will add the tag.

## Expectations
- Indexed within 1–2 weeks of Search Console submission.
- Brand term ("Qestimation") ranks #1 within days.
- City terms ("construction estimating Brisbane") page 1 in roughly 2–4 months with a Business Profile, reviews and 15+ citations.
- National terms ("construction estimating services Australia") are competitive; expect 4–8 months and steady content + links.

## Monthly rebuild & deploy
```bash
python -I _src/build.py
git add -A && git commit -m "Content update" && git push
```
