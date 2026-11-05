# Generates the static Qestimation site (HTML pages + SEO files) into the parent folder.
# Run:  python -I _src/build.py   (from the qestimation folder)
import os, json, html, datetime, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://qestimation.com"
BRAND = "Qestimation"
PHONE = "07 3000 0000"                      # TODO: real phone number
PHONE_INTL = "+61730000000"
EMAIL = "estimates@qestimation.com"         # TODO: real email
ADDRESS = {"street": "Level 1, 123 Example Street", "city": "Brisbane", "region": "QLD", "postal": "4000", "country": "AU"}
FORM_ENDPOINT = ""                          # e.g. https://formspree.io/f/xxxx — empty = mailto fallback
TODAY = datetime.date.today().isoformat()
VER = datetime.datetime.now().strftime("%Y%m%d%H%M")
SAME_AS = ["https://www.facebook.com/qestimation", "https://www.linkedin.com/company/qestimation", "https://www.instagram.com/qestimation"]

PAGES = [
    ("index.html", "Home", "/"),
    ("services.html", "Services", "/services.html"),
    ("work-samples.html", "Work Samples", "/work-samples.html"),
    ("refund-policy.html", "Refund Policy", "/refund-policy.html"),
    ("sydney-build.html", "Sydney Build", "/sydney-build.html"),
    ("get-quote.html", "Contact Us", "/get-quote.html"),
]

def e(s): return html.escape(s, quote=True)

def jsonld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, indent=1) + '</script>'

ORG = {
    "@type": ["ProfessionalService", "LocalBusiness", "Organization"],
    "@id": DOMAIN + "/#organization",
    "name": BRAND,
    "alternateName": "Qestimation Construction Estimating Services",
    "url": DOMAIN + "/",
    "logo": {"@type": "ImageObject", "url": DOMAIN + "/assets/img/logo.png", "width": 860, "height": 309},
    "image": DOMAIN + "/assets/img/og-image.jpg",
    "description": "Qestimation provides construction cost estimating, quantity takeoff, budget estimating and cost control services for developers, general contractors, subcontractors and architects across Australia.",
    "telephone": PHONE_INTL,
    "email": EMAIL,
    "priceRange": "$$",
    "address": {"@type": "PostalAddress", "streetAddress": ADDRESS["street"], "addressLocality": ADDRESS["city"], "addressRegion": ADDRESS["region"], "postalCode": ADDRESS["postal"], "addressCountry": ADDRESS["country"]},
    "areaServed": [{"@type": "Country", "name": "Australia"}, {"@type": "City", "name": "Brisbane"}, {"@type": "City", "name": "Sydney"}, {"@type": "City", "name": "Melbourne"}, {"@type": "City", "name": "Gold Coast"}],
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"}],
    "sameAs": SAME_AS,
    "knowsAbout": ["construction cost estimating", "quantity takeoff", "material takeoff", "bid estimating", "budget estimating", "cost control", "pre-construction services"],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Construction Estimating Services", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Cost Estimation", "url": DOMAIN + "/services.html#cost-estimation"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Material / Quantity Takeoff", "url": DOMAIN + "/services.html#quantity-takeoff"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Cost Controls", "url": DOMAIN + "/services.html#cost-controls"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Budget Estimating", "url": DOMAIN + "/services.html#budget-estimating"}},
    ]},
}
WEBSITE = {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": BRAND, "publisher": {"@id": DOMAIN + "/#organization"}, "inLanguage": "en-AU"}

def breadcrumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u} for i, (n, u) in enumerate(items)]}

def head(title, desc, path, extra_ld=None, og_type="website", keywords=""):
    url = DOMAIN + path
    graph = [ORG, WEBSITE] + (extra_ld or [])
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{f'<meta name="keywords" content="{e(keywords)}">' if keywords else ''}
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-au" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="author" content="{BRAND}">
<meta name="geo.region" content="AU-{ADDRESS['region']}">
<meta name="geo.placename" content="{ADDRESS['city']}">
<meta name="theme-color" content="#1c2646">
<meta property="og:locale" content="en_AU">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{BRAND} construction estimating services logo">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{DOMAIN}/assets/img/og-image.jpg">
<link rel="icon" type="image/png" sizes="64x64" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer">
<link rel="stylesheet" href="assets/css/style.css?v={VER}">
{jsonld({"@context": "https://schema.org", "@graph": graph})}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="preloader" aria-hidden="true"><img src="assets/img/logo-mark.png" alt=""></div>
"""

def header(active):
    ACT = ' class="active" aria-current="page"'
    links = "".join(f'<a href="{f}"{ACT if f == active else ""}>{e(n)}</a>' for f, n, _ in PAGES if f != "get-quote.html")
    return f"""<div class="topbar"><div class="container">
  <a href="tel:{PHONE_INTL}"><i class="fa-solid fa-phone"></i> {PHONE}</a><span class="sep">|</span>
  <a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope"></i> {EMAIL}</a>
</div></div>
<header class="header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="{BRAND} home"><img src="assets/img/logo.png" alt="{BRAND} – Construction Estimating Services" width="860" height="309"></a>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
    <nav class="nav" id="nav" aria-label="Main">
      {links}
      <a href="get-quote.html" class="btn btn-primary{" active" if active == "get-quote.html" else ""}">Contact Us</a>
    </nav>
  </div>
</header>
<main id="main">
"""

def cta_block():
    return f"""<section class="cta" style="background-image:url(assets/img/about-call-to-action-57862405.jpg)" aria-labelledby="cta-h">
  <div class="container">
    <div data-reveal="left">
      <h2 id="cta-h">Let’s Start Your Project Today!</h2>
      <p>Our qualified and professional estimators will accurately detail the material takeoffs and cost estimates for your upcoming building projects.</p>
    </div>
    <div class="cta__side" data-reveal="right" data-delay="150">
      <a href="get-quote.html" class="btn btn-primary"><i class="fa-solid fa-file-invoice-dollar"></i> Get A Free Quote</a>
      <small>Only takes a few seconds!</small>
    </div>
  </div>
</section>
"""

def partners_block(title="Trusted Partners"):
    logos = ["thumbnail_image001-1.png", "logo-3.png", "thumbnail_image001.jpg", "thumbnail_image002.jpg", "thumbnail_image001-1.jpg", "thumbnail_image001.png"]
    names = ["EPPX Construction", "Acorn Electrical Specialists", "Keystone Contracting", "Arvani Building Works", "Hallmark Builders", "All Phase"]
    items = "".join(f'<div class="partner"><img src="assets/img/{l}" alt="{e(n)}" loading="lazy" width="200" height="90"></div>' for l, n in zip(logos, names))
    return f"""<section class="section partners" aria-labelledby="partners-h">
  <div class="container">
    <div class="section-title" data-reveal="up"><h2 id="partners-h">{e(title)}</h2></div>
    <div class="marquee" data-reveal="zoom"><div class="marquee__track">{items}{items}</div></div>
  </div>
</section>
"""

def footer():
    links = "".join(f'<li><i class="fa-solid fa-angle-right"></i><a href="{f}">{e(n)}</a></li>' for f, n, _ in PAGES)
    return f"""</main>
<footer class="footer">
  <div class="container footer__top">
    <div data-reveal="up">
      <img class="flogo" src="assets/img/logo-white.png" alt="{BRAND}" width="860" height="309" loading="lazy">
      <p>{BRAND} is an Australian construction estimating company delivering accurate cost estimates, quantity takeoffs and budget forecasts so builders can bid with confidence and win more work.</p>
      <div class="social" aria-label="Social media">
        <a href="{SAME_AS[0]}" aria-label="Facebook" rel="noopener"><i class="fa-brands fa-facebook-f"></i></a>
        <a href="{SAME_AS[1]}" aria-label="LinkedIn" rel="noopener"><i class="fa-brands fa-linkedin-in"></i></a>
        <a href="{SAME_AS[2]}" aria-label="Instagram" rel="noopener"><i class="fa-brands fa-instagram"></i></a>
      </div>
    </div>
    <div data-reveal="up" data-delay="100"><h4>Quick Links</h4><ul>{links}</ul></div>
    <div data-reveal="up" data-delay="200"><h4>Services</h4><ul>
      <li><i class="fa-solid fa-angle-right"></i><a href="services.html#cost-estimation">Cost Estimation</a></li>
      <li><i class="fa-solid fa-angle-right"></i><a href="services.html#quantity-takeoff">Quantity &amp; Material Takeoff</a></li>
      <li><i class="fa-solid fa-angle-right"></i><a href="services.html#cost-controls">Cost Controls</a></li>
      <li><i class="fa-solid fa-angle-right"></i><a href="services.html#budget-estimating">Budget Estimating</a></li>
      <li><i class="fa-solid fa-angle-right"></i><a href="work-samples.html">Trade Estimate Samples</a></li>
    </ul></div>
    <div data-reveal="up" data-delay="300"><h4>Contact</h4><ul>
      <li><i class="fa-solid fa-location-dot"></i><span>{e(ADDRESS['street'])}, {e(ADDRESS['city'])} {ADDRESS['region']} {ADDRESS['postal']}, Australia</span></li>
      <li><i class="fa-solid fa-phone"></i><a href="tel:{PHONE_INTL}">{PHONE}</a></li>
      <li><i class="fa-solid fa-envelope"></i><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><i class="fa-regular fa-clock"></i><span>Mon – Fri, 8:00am – 6:00pm AEST</span></li>
    </ul></div>
  </div>
  <div class="footer__bottom"><div class="container">
    Copyright © 2015–<span class="year">{datetime.date.today().year}</span> <a href="index.html">{BRAND}</a> | All Rights Reserved | <a href="refund-policy.html">Refund Policy</a> | <a href="refund-policy.html#disclaimer">Service Disclaimer</a>
  </div></div>
</footer>
<a href="#" class="to-top" aria-label="Back to top"><i class="fa-solid fa-chevron-up"></i></a>
<a href="tel:{PHONE_INTL}" class="float-call" aria-label="Call {BRAND}"><i class="fa-solid fa-phone"></i></a>
<script src="assets/js/main.js?v={VER}" defer></script>
</body>
</html>
"""

def band():
    return """<section class="band" aria-label="Call to action">
  <div class="container">
    <h2 data-reveal="up">Do You Have A Construction Project We Can Help With?</h2>
    <a href="get-quote.html" class="btn btn-dark" data-reveal="up" data-delay="120">Get a free quote</a>
  </div>
</section>
"""

def inner_hero(title, sub, crumb, bg=None):
    style = f' style="background-image:url(assets/img/{bg})"' if bg else ""
    cls = "hero hero--inner" if bg else "hero hero--plain"
    bgdiv = f'<div class="hero__bg"{style}></div>' if bg else ""
    return f"""<section class="{cls}">
  {bgdiv}
  <div class="container hero__inner">
    <nav class="breadcrumb" aria-label="Breadcrumb" data-reveal="down"><a href="index.html">Home</a><span>/</span><span>{e(crumb)}</span></nav>
    <h1 data-reveal="up">{title}</h1>
    {f'<p data-reveal="up" data-delay="150">{sub}</p>' if sub else ''}
  </div>
</section>
"""

def estimator():
    return """<aside class="estimator" aria-labelledby="est-h">
  <div class="estimator__head" id="est-h"><i class="fa-solid fa-calculator"></i> Cost Estimator</div>
  <div class="estimator__body">
    <h5>Slab dimensions</h5>
    <div class="row"><label for="es-len">Length</label><span><input id="es-len" type="number" min="0" step="0.1" value="10"> <span class="unit">m</span></span></div>
    <div class="row"><label for="es-wid">Width</label><span><input id="es-wid" type="number" min="0" step="0.1" value="8"> <span class="unit">m</span></span></div>
    <h5>Spacings</h5>
    <div class="row"><label for="es-spacing">Rebar spacing (grid)</label><span><input id="es-spacing" type="number" min="1" step="1" value="40"> <span class="unit">cm</span></span></div>
    <h5>At the supplier</h5>
    <div class="row"><label for="es-wire">Wire mass</label><span><input id="es-wire" type="number" min="0" step="0.01" value="0.89"> <span class="unit">kg/m</span></span></div>
    <div class="row"><label for="es-barlen">Length of a single rebar</label><span><input id="es-barlen" type="number" min="0" step="0.5" value="6"> <span class="unit">m</span></span></div>
    <div class="row"><label for="es-price">Price of a single rebar</label><span><input id="es-price" type="number" min="0" step="0.5" value="12"> <span class="unit">$</span></span></div>
    <h5>Results</h5>
    <div class="result">
      <div class="row"><span>Rebar along length</span><strong id="es-r-len">—</strong></div>
      <div class="row"><span>Rebar along width</span><strong id="es-r-wid">—</strong></div>
      <div class="row"><span>Total rebar</span><strong id="es-r-total">—</strong></div>
      <div class="row"><span>Bars to order</span><strong id="es-r-bars">—</strong></div>
      <div class="row"><span>Estimated cost</span><strong class="total" id="es-r-cost">—</strong></div>
    </div>
    <small>Indicative only. For a certified takeoff and priced estimate, <a href="get-quote.html">request a free quote</a>.</small>
  </div>
</aside>
"""

FAQ = [
    ("What is a construction cost estimate?", "A construction cost estimate is a detailed forecast of what a building project will cost, covering materials, labour, equipment, overheads and contingencies. Qestimation prepares conceptual, bid and budget estimates so developers and contractors know the real number before committing."),
    ("How accurate are Qestimation estimates?", "Our estimates are typically within 1% of final construction costs. We price every item from current supplier and subcontractor rates for the project’s location and cross-check quantities with colour-coded marked plans."),
    ("How fast can I get a quote or estimate?", "A free quote is usually returned within 24 hours of receiving your drawings. Most trade takeoffs are delivered in 2–5 business days depending on project size, and rush turnaround is available."),
    ("Which file formats can I send?", "We accept PDF, DWG, DXF, Revit/BIM exports, scanned plans and photos. Upload them through the quote form or email them to our estimating team."),
    ("Who uses Qestimation?", "Developers, general contractors, subcontractors, architects, quantity surveyors and owner-builders across Australia use Qestimation for quantity takeoffs, bid estimates, budget estimates and on-site cost control."),
    ("What trades do you estimate?", "Site work, concrete, masonry, structural and miscellaneous metals, lumber and framing, drywall, flooring, painting, exterior finishes, plumbing, electrical, HVAC and more. See our work samples for real examples."),
    ("Do you offer refunds?", "We do not issue refunds; instead we offer exchanges and revisions until the deliverable meets the agreed scope. Full details are on our Refund Policy page."),
]

# ---------------------------------------------------------------- HOME
def build_home():
    title = "Qestimation | Construction Estimating Services Australia – Cost Estimates & Quantity Takeoffs"
    desc = "Qestimation delivers accurate construction cost estimates, material & quantity takeoffs, budget estimates and cost control for developers, contractors, subcontractors and architects. Free quote within 24 hours."
    ld = [
        {"@type": "WebPage", "@id": DOMAIN + "/#webpage", "url": DOMAIN + "/", "name": title, "description": desc, "isPartOf": {"@id": DOMAIN + "/#website"}, "about": {"@id": DOMAIN + "/#organization"}, "inLanguage": "en-AU", "dateModified": TODAY,
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#hero-h", "#intro-p", ".fact"]}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
        breadcrumbs([("Home", "/")]),
    ]
    services = [
        ("fa-regular fa-clipboard", "Cost Estimation", "We provide building cost estimates such as conceptual cost estimates, bid estimates and detailed trade pricing.", "services.html#cost-estimation"),
        ("fa-regular fa-pen-to-square", "Material Takeoff", "We specialise in preparing material takeoffs and material lists for every construction trade.", "services.html#quantity-takeoff"),
        ("fa-regular fa-hourglass-half", "Cost Controls", "Our cost control services are conducted on site during the construction stage to keep budgets on track.", "services.html#cost-controls"),
        ("fa-regular fa-credit-card", "Budget Estimate", "Our estimators develop accurate budgets based on years of experience in the field.", "services.html#budget-estimating"),
    ]
    cards = "".join(f"""<article class="card" data-reveal="up" data-delay="{i*120}">
        <div class="card__icon"><i class="{ic}"></i></div>
        <h3>{e(t)}</h3><p>{e(d)}</p>
        <a class="link" href="{u}">Get a quote <i class="fa-solid fa-arrow-right-long"></i></a>
      </article>""" for i, (ic, t, d, u) in enumerate(services))
    counters = [("fa-solid fa-suitcase", 340, "+", "Pipeline Projects"), ("fa-regular fa-building", 4328, "+", "Completed Projects"), ("fa-solid fa-users", 32, "", "Trained Professionals"), ("fa-solid fa-globe", 400, "+", "Years Combined Experience")]
    cnt = "".join(f'<div class="counter" data-reveal="zoom" data-delay="{i*120}"><i class="{ic}"></i><span class="num" data-count="{n}" data-suffix="{s}">0</span><span class="label">{e(l)}</span></div>' for i, (ic, n, s, l) in enumerate(counters))
    works = [("sample-2.jpg", "Mixed-Use Residential Development", "Concrete, masonry &amp; finishes takeoff"), ("sample-1.jpg", "Beachfront High-Rise Towers", "Full bid estimate"), ("sample-3.jpg", "Heritage Commercial Refurbishment", "Budget estimate &amp; cost control")]
    wk = "".join(f'<a class="work" href="work-samples.html" data-reveal="up" data-delay="{i*140}"><img src="assets/img/{im}" alt="{e(t)} – construction estimate sample by {BRAND}" loading="lazy" width="500" height="500"><div class="work__cap"><h3>{t}</h3><span>{s}</span></div></a>' for i, (im, t, s) in enumerate(works))
    values = [("Summary-Tab.jpg", "Executive Takeoff Summary", "A one-page summary of every quantity and cost so you can review the whole bid in minutes."), ("Color-Coded-Plans.jpg", "Color Coded Marked Plans", "Every item we count is highlighted on your drawings, making audits and site hand-over simple."), ("Existing-Conditions.jpg", "3D Cut/Fill Grading Models", "Earthwork volumes modelled in 3D for accurate cut, fill and site-work pricing.")]
    vals = "".join(f'<div class="value" data-reveal="flip" data-delay="{i*140}"><figure><img src="assets/img/{im}" alt="{e(t)} – {BRAND} value added service" loading="lazy" width="800" height="600"></figure><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (im, t, d) in enumerate(values))
    testis = [("home-testimonial-113165296.jpg", "“Our showroom came in under the budget Qestimation set and the takeoff matched the final order list almost line for line. Never regretted choosing them.”", "Harry Smith", "Director, Fit-out Contractor"),
              ("home-testimonial-84268399.jpg", "“Your service is very prompt; the day after the site visit we had the design estimate in our inbox. Much appreciated.”", "John Doe", "Project Manager, Residential Developer"),
              ("home-testimonial-113165296.jpg", "“Colour-coded plans and the executive summary made our tender review painless. We won the bid with a margin we trusted.”", "Sarah Lee", "Estimating Lead, General Contractor")]
    ts = "".join(f'<div class="slide{" active" if i == 0 else ""}"><img class="avatar" src="assets/img/{im}" alt="{e(n)}" width="74" height="74" loading="lazy"><blockquote>{q}</blockquote><cite>{e(n)}<small>{e(r)}</small></cite></div>' for i, (im, q, n, r) in enumerate(testis))
    faq = "".join(f'<details{" open" if i == 0 else ""} data-reveal="up" data-delay="{i*60}"><summary>{e(q)}</summary><div class="answer"><p>{e(a)}</p></div></details>' for i, (q, a) in enumerate(FAQ))
    body = f"""<section class="hero" aria-labelledby="hero-h">
  <div class="hero__bg" style="background-image:url(assets/img/bg-slide1-2.jpg)" role="img" aria-label="Construction site with engineer reviewing plans"></div>
  <div class="container hero__inner">
    <h1 id="hero-h" data-reveal="down">Construction Estimation Services</h1>
    <p data-reveal="up" data-delay="200">We provide construction estimating services for Developers, General Contractors, Subcontractors and Architects — accurate quantity takeoffs and cost estimates delivered fast.</p>
    <div class="btns" data-reveal="up" data-delay="400">
      <a href="work-samples.html" class="btn btn-outline">Explore Samples</a>
      <a href="get-quote.html" class="btn btn-primary">Get a Quote Today</a>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true"></div>
</section>
{band()}
<section class="section section--light has-curve" aria-labelledby="intro-h">
  <div class="container">
    <div class="section-title intro" data-reveal="up">
      <h2 id="intro-h">Construction is tough.<strong>We make pre-construction easy</strong></h2>
      <div class="divider"></div>
      <p id="intro-p">We can’t help you build, but we can make sure your pre-construction process is a breeze. {BRAND} is a construction estimating company that turns your drawings into priced, audit-ready quantity takeoffs and cost estimates.</p>
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>
<section class="counters" style="background-image:url(assets/img/slider3.jpg)" aria-label="Company statistics">
  <div class="container"><div class="counters__grid">{cnt}</div></div>
  <div class="curve-bottom"></div>
</section>
<section class="section" aria-labelledby="works-h">
  <div class="container">
    <div class="section-title" data-reveal="up">
      <h2 id="works-h">Recent Works</h2>
      <p>From Space Launch Complexes, K-12 Academies and Mixed-Use Developments to Essential Service Facilities, Fine Arts Complexes and Community Parks, our experience is diverse. We encourage you to take a deep dive into our portfolio – we’re proud of it.</p>
    </div>
    <div class="works">{wk}</div>
    <div class="sep-line"></div>
    <a href="work-samples.html" class="btn btn-primary btn-block" data-reveal="up">View All Samples</a>
  </div>
</section>
<section class="section section--light" aria-labelledby="value-h">
  <div class="container">
    <div class="section-title" data-reveal="up">
      <h2 id="value-h">Value Added Services At No Additional Cost</h2>
      <p>Our nuanced process reduces the subjectivity of construction cost estimating – boiling it down to a science.</p>
    </div>
    <div class="values">{vals}</div>
  </div>
</section>
<section class="testimonials" style="background-image:url(assets/img/bg-testimonials_f.jpg)" aria-labelledby="testi-h">
  <div class="container">
    <div class="section-title" data-reveal="up"><h2 id="testi-h">What Our Customers Say!</h2></div>
    <div class="slider" data-reveal="zoom">{ts}</div>
    <div class="dots" role="tablist" aria-label="Testimonials"></div>
  </div>
</section>
{partners_block()}
<section class="section section--light" aria-labelledby="about-h">
  <div class="container">
    <div class="section-title" data-reveal="up">
      <h2 id="about-h">About {BRAND}</h2>
      <p><strong>{BRAND}</strong> is an Australian construction estimating service. We prepare quantity takeoffs, bid estimates, budget estimates and on-site cost controls for developers, general contractors, subcontractors and architects, with accuracy typically within 1% of final construction cost.</p>
    </div>
    <div class="facts">
      <div class="fact" data-reveal="up"><strong>What we do</strong>Construction cost estimating, material &amp; quantity takeoffs, budget estimates, cost control.</div>
      <div class="fact" data-reveal="up" data-delay="100"><strong>Who we serve</strong>Developers, general contractors, subcontractors, architects and owner-builders across Australia.</div>
      <div class="fact" data-reveal="up" data-delay="200"><strong>Turnaround</strong>Free quote within 24 hours; most trade takeoffs in 2–5 business days.</div>
      <div class="fact" data-reveal="up" data-delay="300"><strong>Deliverables</strong>Executive takeoff summary, colour-coded marked plans, 3D cut/fill models, priced Excel estimate.</div>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="faq-h">
  <div class="container">
    <div class="section-title" data-reveal="up"><h2 id="faq-h">Frequently Asked Questions</h2><p>Straight answers about construction estimating, turnaround and how we work.</p></div>
    <div class="faq">{faq}</div>
  </div>
</section>
{cta_block()}
"""
    return head(title, desc, "/", ld, keywords="construction estimating services, construction cost estimator, quantity takeoff services, material takeoff, bid estimating, budget estimate, cost control, construction estimating Australia, Brisbane estimator") + header("index.html") + body + footer()

# ---------------------------------------------------------------- SERVICES
def build_services():
    title = "Construction Estimating Services | Quantity Takeoff, Cost & Budget Estimating – Qestimation"
    desc = "Qestimation's construction estimating services: quantity takeoff & pricing, cost & budget estimating, bid estimates and on-site cost control. Accuracy typically within 1% of final construction cost."
    ld = [{"@type": "WebPage", "url": DOMAIN + "/services.html", "name": title, "description": desc, "isPartOf": {"@id": DOMAIN + "/#website"}, "inLanguage": "en-AU", "dateModified": TODAY},
          breadcrumbs([("Home", "/"), ("Services", "/services.html")])]
    for sid, name, d in [("quantity-takeoff", "Quantity Takeoff & Pricing", "Detailed material quantity takeoffs with current local pricing for every construction trade."),
                         ("cost-estimation", "Cost Estimation", "Conceptual, schematic and bid cost estimates for construction projects."),
                         ("budget-estimating", "Cost & Budget Estimating", "Budget forecasts that decide whether a project proceeds and keep it on budget once it starts."),
                         ("cost-controls", "Cost Controls", "On-site cost monitoring, variation tracking and progress claim support during construction.")]:
        ld.append({"@type": "Service", "@id": DOMAIN + "/services.html#" + sid, "name": name, "description": d, "provider": {"@id": DOMAIN + "/#organization"}, "areaServed": "Australia", "serviceType": "Construction estimating", "url": DOMAIN + "/services.html#" + sid})
    body = inner_hero("Construction Estimating Services", "Estimating projects shouldn’t be hard. Our team of seasoned estimators will estimate the cost of your project with a high degree of accuracy. We use a top-of-the-line cost database to calculate the costs on your job based on its location. The accuracy is typically within 1% of final construction costs.", "Services", "services-banner-1.jpg") + band() + f"""
<section class="section" aria-label="Services detail">
  <div class="container with-sidebar">
    <div>
      <article class="service-row" id="quantity-takeoff">
        <div class="service-row__img" data-reveal="left"><img src="assets/img/qunatity-offs-1.jpg" alt="Estimator performing a quantity takeoff from construction drawings" loading="lazy" width="1000" height="1000"></div>
        <div data-reveal="right">
          <h2>Quantity Takeoff &amp; Pricing</h2>
          <p>As a professional involved in architecture, engineering and construction (AEC), you’re likely familiar with quantity takeoffs. The term has been around a long time in the building industry, and it reflects an important part of the planning process. Quantity takeoff requires a highly specialised skill set to do data management correctly.</p>
          <p>This crucial step in a project’s early stage can make or break success. Improper quantity takeoffs can underestimate or overestimate construction costs, causing inefficiency in the entire construction chain.</p>
          <p>It can be detrimental to any job when required material amounts and realistic pricing values are overlooked or duplicated. The key to successful construction data collection is thoroughness and accuracy – and that is exactly what {BRAND} delivers.</p>
          <ul class="check-list">
            <li><i class="fa-solid fa-circle-check"></i>Trade-by-trade material lists in Excel with colour-coded marked plans</li>
            <li><i class="fa-solid fa-circle-check"></i>Priced with current supplier and subcontractor rates for your location</li>
            <li><i class="fa-solid fa-circle-check"></i>Delivered in 2–5 business days, rush service available</li>
          </ul>
        </div>
      </article>
      <article class="service-row" id="cost-estimation">
        <div class="service-row__img" data-reveal="right"><img src="assets/img/cost-estimation.jpg" alt="Construction cost estimate spreadsheet with calculator and blueprints" loading="lazy" width="1000" height="1000"></div>
        <div data-reveal="left">
          <h2>Cost &amp; Budget Estimating</h2>
          <p>Cost estimation in project management is the process of forecasting the financial and other resources needed to complete a project within a defined scope. Cost estimation accounts for each element required for the project – from materials to labour – and calculates a total amount that determines a project’s budget.</p>
          <p>An initial cost estimate can determine whether an organisation greenlights a project, and if the project moves forward, the estimate can be a factor in defining the project’s scope. If the cost estimation comes in too high, an organisation may decide to pare down the project to fit what they can afford (it is also required to begin securing funding for the project). Once the project is in motion, the cost estimate is used to manage all of its affiliated costs in order to keep the project on budget.</p>
          <ul class="check-list">
            <li><i class="fa-solid fa-circle-check"></i>Conceptual, schematic, design-development and bid estimates</li>
            <li><i class="fa-solid fa-circle-check"></i>Budget estimates for feasibility and finance applications</li>
            <li><i class="fa-solid fa-circle-check"></i>Executive summary so decision makers see the number in one page</li>
          </ul>
        </div>
      </article>
      <article class="service-row" id="budget-estimating">
        <div class="service-row__img" data-reveal="left"><img src="assets/img/Summary-Tab.jpg" alt="Executive takeoff summary sheet produced by Qestimation" loading="lazy" width="800" height="545"></div>
        <div data-reveal="right">
          <h2>Budget Estimating</h2>
          <p>Our estimators develop accurate budgets based on years of experience in the field. A {BRAND} budget estimate tells you early what a design will realistically cost to build, where the risk sits and which scope items drive the number – before you commit to tender.</p>
          <ul class="check-list">
            <li><i class="fa-solid fa-circle-check"></i>Elemental and trade breakdowns with allowances and contingencies</li>
            <li><i class="fa-solid fa-circle-check"></i>Value-engineering options to bring scope back to budget</li>
            <li><i class="fa-solid fa-circle-check"></i>Updated at each design milestone</li>
          </ul>
        </div>
      </article>
      <article class="service-row" id="cost-controls">
        <div class="service-row__img" data-reveal="right"><img src="assets/img/Color-Coded-Plans.jpg" alt="Colour-coded marked plans used for on-site cost control" loading="lazy" width="800" height="571"></div>
        <div data-reveal="left">
          <h2>Cost Controls</h2>
          <p>Our cost control services are conducted on site during the construction stage. We track committed and forecast costs against the estimate, assess variations, verify progress claims and report monthly so there are no surprises at completion.</p>
          <ul class="check-list">
            <li><i class="fa-solid fa-circle-check"></i>Variation and claim assessment</li>
            <li><i class="fa-solid fa-circle-check"></i>Cost-to-complete forecasting and cash-flow reporting</li>
            <li><i class="fa-solid fa-circle-check"></i>Procurement and subcontractor quotation reviews</li>
          </ul>
        </div>
      </article>
    </div>
    <div class="sidebar" data-reveal="up">{estimator()}</div>
  </div>
</section>
""" + cta_block()
    return head(title, desc, "/services.html", ld, keywords="quantity takeoff services, construction cost estimating, budget estimating, cost control construction, bid estimate Australia") + header("services.html") + body + footer()

# ---------------------------------------------------------------- WORK SAMPLES
SAMPLES = [
    ("site-work", "fa-solid fa-mountain", "Site Work", "Site-Work-Sample.pdf", "Earthworks, cut/fill, excavation, paving and site services quantities."),
    ("concrete", "fa-solid fa-cubes", "Concrete Estimates", "Concrete-Estimate-Sample.pdf", "Footings, slabs, columns, beams, formwork and reinforcement priced per element."),
    ("masonry", "fa-solid fa-building", "Masonry Estimates", "Masonry-Estimate-Sample.pdf", "Block and brick counts, mortar, grout, lintels and reinforcement."),
    ("metal", "fa-solid fa-industry", "Metal Takeoffs", "Metal-Takeoffs-Sample.pdf", "Structural steel tonnage, decking, misc. metals and connections."),
    ("lumber", "fa-solid fa-tree", "Lumber Takeoffs", "Lumber-Takeoffs-Sample.pdf", "Framing lumber order list with studs, plates, joists, rafters and sheathing."),
    ("drywall", "fa-solid fa-layer-group", "Drywall Estimates", "Drywall-Estimates-Sample.pdf", "Board area, framing, insulation, finishing levels and accessories."),
    ("flooring", "fa-solid fa-table-cells", "Flooring Estimates", "Flooring-Estimates-Sample.pdf", "Tile, carpet, vinyl and timber flooring areas with waste factors."),
    ("painting", "fa-solid fa-paint-roller", "Painting Estimates", "Painting-Estimates-Sample.pdf", "Wall, ceiling and trim areas by coating system and number of coats."),
    ("exterior", "fa-solid fa-house-chimney", "Exterior Finishes Estimates", "Exterior-Finishes-Estimates-Sample.pdf", "Cladding, render, roofing, flashing and external trims."),
    ("plumbing", "fa-solid fa-faucet-drip", "Plumbing Estimates", "Plumbing-Estimates-Sample.pdf", "Fixtures, pipework by size, fittings, drainage and hot water."),
    ("electrical", "fa-solid fa-bolt", "Electric Work Estimates", "Electric-Work-Estimates-Sample.pdf", "Lighting, power, switchboards, cabling and containment counts."),
]
def build_work():
    title = "Construction Estimate Work Samples | Concrete, Masonry, Electrical & More – Qestimation"
    desc = "Download real Qestimation estimate samples: site work, concrete, masonry, metal, lumber, drywall, flooring, painting, exterior finishes, plumbing and electrical takeoffs."
    ld = [{"@type": "CollectionPage", "url": DOMAIN + "/work-samples.html", "name": title, "description": desc, "isPartOf": {"@id": DOMAIN + "/#website"}, "inLanguage": "en-AU", "dateModified": TODAY,
           "hasPart": [{"@type": "DigitalDocument", "name": n + " Sample", "url": DOMAIN + "/assets/samples/" + f, "encodingFormat": "application/pdf", "description": d} for _, _, n, f, d in SAMPLES]},
          breadcrumbs([("Home", "/"), ("Work Samples", "/work-samples.html")])]
    nav = "".join(f'<button type="button" data-tab="{sid}" role="tab"><i class="{ic}"></i>{e(n)}</button>' for sid, ic, n, _, _ in SAMPLES)
    panels = "".join(f"""<section class="samples__panel" id="{sid}" role="tabpanel">
      <h2>{e(n)}</h2><p>{e(d)}</p>
      <div class="pdf-actions"><a class="btn btn-primary" href="assets/samples/{f}" target="_blank" rel="noopener"><i class="fa-solid fa-up-right-from-square"></i> Open sample</a><a class="btn btn-navy" href="assets/samples/{f}" download><i class="fa-solid fa-download"></i> Download PDF</a></div>
      <iframe class="pdf-frame" {'src' if i == 0 else 'data-src'}="assets/samples/{f}#view=FitH" title="{e(n)} sample PDF" loading="lazy"></iframe>
    </section>""" for i, (sid, ic, n, f, d) in enumerate(SAMPLES))
    body = inner_hero("Work Samples", "Real deliverables from recent projects. Every sample includes quantities, pricing and colour-coded plan references.", "Work Samples") + band() + f"""
<section class="section" aria-label="Sample estimates by trade">
  <div class="container samples">
    <nav class="samples__nav" role="tablist" aria-label="Trades" data-reveal="left">{nav}</nav>
    <div data-reveal="right">{panels}</div>
  </div>
</section>
""" + cta_block()
    return head(title, desc, "/work-samples.html", ld, keywords="construction estimate sample, concrete estimate sample, electrical estimate sample, quantity takeoff example") + header("work-samples.html") + body + footer()

# ---------------------------------------------------------------- REFUND POLICY
def build_refund():
    title = "Refund Policy & Service Disclaimer – Qestimation"
    desc = "Qestimation refund policy: we do not issue refunds, we offer exchanges and revisions. We never collect card details – invoices are paid directly by the client. Accepted payment options listed."
    ld = [{"@type": "WebPage", "url": DOMAIN + "/refund-policy.html", "name": title, "description": desc, "isPartOf": {"@id": DOMAIN + "/#website"}, "inLanguage": "en-AU", "dateModified": TODAY},
          breadcrumbs([("Home", "/"), ("Refund Policy", "/refund-policy.html")])]
    pays = "".join(f'<img src="assets/img/{f}" alt="{e(n)} accepted" loading="lazy" width="200" height="130">' for f, n in [("square-up.jpg", "Square payments"), ("amex.jpg", "American Express"), ("master-card.png", "Mastercard"), ("visa.png", "Visa"), ("all_local_bank_transfers.jpg", "Local bank transfer")])
    body = inner_hero("Refund Policy", "", "Refund Policy") + band() + f"""
<section class="section" aria-labelledby="rp-h">
  <div class="container prose">
    <h2 id="rp-h" data-reveal="up">Refund Policy</h2>
    <p data-reveal="up">We always strive to provide our clients maximum satisfaction and value-for-money services. However, please note that <strong>{BRAND} does not issue refunds. We offer exchanges only</strong> – if a deliverable does not meet the agreed scope we will revise or re-issue it until it does.</p>
    <div class="callout" data-reveal="up"><p><strong>Payment security.</strong> We do not take credit card or payment-related details. None of our staff are allowed or authorised to collect card or payment details from clients. We send an invoice and clients process the payment themselves through the options below.</p></div>
    <h2 data-reveal="up">Payment Options</h2>
    <div class="pay-logos" data-reveal="zoom">{pays}</div>
    <h2 id="disclaimer" data-reveal="up" style="margin-top:50px">Service Disclaimer</h2>
    <p data-reveal="up">Estimates and takeoffs are prepared from the drawings and information supplied by the client and reflect market pricing at the date of issue. Quantities are measured to industry-standard methods; pricing is indicative until confirmed by supplier and subcontractor quotations. {BRAND} is not responsible for changes in scope, site conditions, design revisions or market movements after delivery.</p>
  </div>
</section>
""" + partners_block() + cta_block()
    return head(title, desc, "/refund-policy.html", ld) + header("refund-policy.html") + body + footer()

# ---------------------------------------------------------------- SYDNEY BUILD
def build_sydney():
    files = sorted(glob.glob(os.path.join(ROOT, "assets", "gallery", "*.jpeg")), key=lambda p: int(os.path.basename(p).split(".")[0]))
    title = "Sydney Build Expo Gallery – Qestimation at Australia’s Largest Construction Show"
    desc = f"Photos from the Qestimation team at Sydney Build Expo, Australia's largest construction and design show. {len(files)} images from the stand, seminars and networking."
    ld = [{"@type": "ImageGallery", "url": DOMAIN + "/sydney-build.html", "name": title, "description": desc, "isPartOf": {"@id": DOMAIN + "/#website"}, "inLanguage": "en-AU", "dateModified": TODAY,
           "image": [DOMAIN + "/assets/gallery/" + os.path.basename(f) for f in files[:20]]},
          {"@type": "Event", "name": "Sydney Build Expo", "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "location": {"@type": "Place", "name": "ICC Sydney", "address": {"@type": "PostalAddress", "addressLocality": "Sydney", "addressRegion": "NSW", "addressCountry": "AU"}}, "organizer": {"@type": "Organization", "name": "Sydney Build Expo"}, "performer": {"@id": DOMAIN + "/#organization"}, "startDate": "2022-05-05", "endDate": "2022-05-06", "description": f"{BRAND} exhibited at Sydney Build Expo."},
          breadcrumbs([("Home", "/"), ("Sydney Build", "/sydney-build.html")])]
    gal = "".join(f'<a href="assets/gallery/{os.path.basename(f)}" data-reveal="zoom" data-delay="{(i%4)*80}"><img src="assets/gallery/thumbs/{os.path.basename(f)}" alt="{BRAND} team at Sydney Build Expo – photo {i+1}" loading="lazy" width="400" height="300"></a>' for i, f in enumerate(files))
    body = inner_hero("Sydney Build", f"{BRAND} at Sydney Build Expo – Australia’s largest construction, architecture and infrastructure show. Meet the team, see our stand and the conversations that start great projects.", "Sydney Build") + f"""
<section class="section" aria-label="Sydney Build photo gallery">
  <div class="container">
    <div class="section-title" data-reveal="up"><h2>Event Gallery</h2><p>{len(files)} photos from the expo floor. Click any image to view full size.</p></div>
    <div class="gallery">{gal}</div>
  </div>
</section>
""" + cta_block()
    return head(title, desc, "/sydney-build.html", ld, keywords="Sydney Build Expo, construction expo Australia, Qestimation events") + header("sydney-build.html") + body + footer()

# ---------------------------------------------------------------- CONTACT
def build_quote():
    title = "Get a Free Construction Estimate Quote | Contact Qestimation"
    desc = "Upload your blueprints and get a free quotation from Qestimation's experienced estimators within 24 hours. Call, email or use the online form."
    ld = [{"@type": "ContactPage", "url": DOMAIN + "/get-quote.html", "name": title, "description": desc, "isPartOf": {"@id": DOMAIN + "/#website"}, "inLanguage": "en-AU", "dateModified": TODAY, "mainEntity": {"@id": DOMAIN + "/#organization"}},
          breadcrumbs([("Home", "/"), ("Contact Us", "/get-quote.html")])]
    q = f"{ADDRESS['street']}, {ADDRESS['city']} {ADDRESS['region']} {ADDRESS['postal']}, Australia".replace(" ", "+")
    body = inner_hero("Get a Free Quote", "", "Contact Us") + f"""
<section class="section" aria-labelledby="contact-h">
  <div class="container with-sidebar">
    <div>
      <div class="section-title" data-reveal="up"><h2 id="contact-h">Talk To Us – We’re Here To Help</h2></div>
      <div class="info-boxes">
        <div class="info-box" data-reveal="up"><i class="fa-solid fa-house"></i><p>{e(ADDRESS['street'])},<br>{e(ADDRESS['city'])} {ADDRESS['region']} {ADDRESS['postal']}, Australia</p></div>
        <div class="info-box" data-reveal="up" data-delay="120"><i class="fa-solid fa-phone"></i><p><a href="tel:{PHONE_INTL}">{PHONE}</a></p></div>
        <div class="info-box" data-reveal="up" data-delay="240"><i class="fa-solid fa-envelope"></i><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
      </div>
      <p class="text-center" data-reveal="up">Upload your blueprint &amp; get an absolutely free quotation from our experienced engineers.</p>
      <form id="quote-form" class="form" data-endpoint="{FORM_ENDPOINT}" data-email="{EMAIL}" novalidate data-reveal="up" enctype="multipart/form-data" method="post">
        <div><label for="f-name">Your Name *</label><input id="f-name" name="name" type="text" required autocomplete="name"></div>
        <div><label for="f-email">Email Address *</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
        <div><label for="f-phone">Phone Number</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
        <div><label for="f-subject">Subject</label><input id="f-subject" name="subject" type="text" placeholder="e.g. Concrete takeoff – 12 unit townhouse"></div>
        <div class="full"><label>Upload Project Files (PDF, DWG, images)</label><label class="file"><i class="fa-solid fa-cloud-arrow-up"></i><span>Choose PDF / DWG / images</span><input type="file" name="files" multiple accept=".pdf,.dwg,.dxf,.zip,image/*"></label></div>
        <div class="full"><label for="f-msg">A Brief Information About Project *</label><textarea id="f-msg" name="message" required placeholder="Project type, location, trades you need estimated, deadline…"></textarea></div>
        <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="display:none">
        <div class="form-msg" role="status" aria-live="polite"></div>
        <div class="full"><button type="submit" class="btn btn-primary"><i class="fa-solid fa-paper-plane"></i> Get Free Quote</button></div>
        <p class="form-note">By submitting you agree to be contacted about your enquiry. We never share your drawings with third parties.</p>
      </form>
    </div>
    <div class="sidebar" data-reveal="up">{estimator()}</div>
  </div>
  <div class="container map" data-reveal="zoom"><iframe src="https://www.google.com/maps?q={q}&output=embed" title="Map showing {BRAND} office location" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</section>
"""
    return head(title, desc, "/get-quote.html", ld, keywords="free construction estimate quote, construction estimator contact, upload blueprints for estimate") + header("get-quote.html") + body + footer()

# ---------------------------------------------------------------- SEO FILES
def build_seo_files():
    urls = "".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{TODAY}</lastmod><changefreq>{'weekly' if u == '/' else 'monthly'}</changefreq><priority>{'1.0' if u == '/' else '0.8'}</priority></url>\n" for _, _, u in PAGES)
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'
    robots = f"User-agent: *\nAllow: /\nDisallow: /_src/\n\n# AI crawlers welcome\nUser-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n"
    llms = f"""# {BRAND}

> {BRAND} is an Australian construction estimating company. We prepare quantity takeoffs, bid estimates, budget estimates and on-site cost controls for developers, general contractors, subcontractors and architects. Accuracy is typically within 1% of final construction cost. Free quotes are returned within 24 hours.

## Key facts
- Services: cost estimation, material/quantity takeoff, budget estimating, cost controls
- Trades covered: site work, concrete, masonry, metals, lumber/framing, drywall, flooring, painting, exterior finishes, plumbing, electrical
- Deliverables: executive takeoff summary, colour-coded marked plans, 3D cut/fill grading models, priced Excel estimate
- Turnaround: quote in 24 h; most takeoffs in 2–5 business days
- Location: {ADDRESS['city']}, {ADDRESS['region']}, Australia (serving all of Australia)
- Contact: {PHONE} · {EMAIL}
- Refunds: no refunds, exchanges/revisions only; no card details are ever collected

## Pages
- [Home]({DOMAIN}/): overview, services, statistics, testimonials, FAQ
- [Services]({DOMAIN}/services.html): quantity takeoff & pricing, cost & budget estimating, cost controls
- [Work Samples]({DOMAIN}/work-samples.html): downloadable PDF estimate samples by trade
- [Refund Policy]({DOMAIN}/refund-policy.html): refund policy, payment options, service disclaimer
- [Sydney Build]({DOMAIN}/sydney-build.html): photo gallery from Sydney Build Expo
- [Contact / Get Quote]({DOMAIN}/get-quote.html): quote form, phone, email, map

## FAQ
""" + "".join(f"- **{q}** {a}\n" for q, a in FAQ)
    manifest = json.dumps({"name": BRAND, "short_name": BRAND, "start_url": "/", "display": "standalone", "background_color": "#ffffff", "theme_color": "#1c2646",
                           "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1)
    return {"sitemap.xml": sitemap, "robots.txt": robots, "llms.txt": llms, "site.webmanifest": manifest}

def main():
    out = {"index.html": build_home(), "services.html": build_services(), "work-samples.html": build_work(), "refund-policy.html": build_refund(), "sydney-build.html": build_sydney(), "get-quote.html": build_quote()}
    out.update(build_seo_files())
    for name, content in out.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(content)
        print("wrote", name, len(content))

if __name__ == "__main__":
    main()
