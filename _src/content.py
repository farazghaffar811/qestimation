# Content for the SEO pages: city landing pages and blog articles.
# Edit freely; build.py renders these into HTML.

CITIES = [
    {
        "slug": "brisbane", "name": "Brisbane", "state": "QLD", "region": "South East Queensland",
        "suburbs": "Brisbane CBD, Fortitude Valley, South Brisbane, Logan, Ipswich, Redlands and Moreton Bay",
        "intro": "Brisbane is in the middle of its biggest construction cycle in a generation, with Olympic infrastructure, Cross River Rail precincts and a wave of mid-rise residential driving demand for fast, accurate pre-construction numbers.",
        "market": "Queensland builders are pricing under the QBCC trust account regime and tight subcontractor availability. Labour rates in Brisbane have climbed faster than the national average, so a takeoff priced on last year's rates will lose money. Our Brisbane estimates use current South East Queensland supplier and subcontractor pricing.",
        "projects": "apartment towers in Newstead and Woolloongabba, industrial sheds in Yatala and Larapinta, school upgrades under the QLD Department of Education program, townhouse developments in Logan and Ipswich, and fit-outs in the CBD",
        "lat": -27.4698, "lng": 153.0251,
    },
    {
        "slug": "sydney", "name": "Sydney", "state": "NSW", "region": "Greater Sydney",
        "suburbs": "Sydney CBD, Parramatta, Western Sydney, the Northern Beaches, Sutherland Shire and the Hills District",
        "intro": "Sydney is Australia's most competitive tendering market. Margins are thin, head contractors demand itemised breakdowns, and the Western Sydney Aerotropolis has created a pipeline of civil and industrial work that rewards contractors who can price quickly.",
        "market": "NSW projects carry Design and Building Practitioners Act obligations and Security of Payment timelines that make early cost certainty essential. Sydney material and labour rates are the highest in the country, and we price every Sydney takeoff against current metropolitan rates rather than national averages.",
        "projects": "high-rise residential in Parramatta and Macquarie Park, warehouse and logistics builds in Kemps Creek and Eastern Creek, hospital and school upgrades, heritage refurbishments in the inner city, and commercial fit-outs across the CBD",
        "lat": -33.8688, "lng": 151.2093,
    },
    {
        "slug": "melbourne", "name": "Melbourne", "state": "VIC", "region": "Greater Melbourne",
        "suburbs": "Melbourne CBD, Docklands, the inner north, the south-east growth corridor, Geelong and the western suburbs",
        "intro": "Melbourne's Big Build, the growth corridors in the west and south-east, and a strong townhouse and medium-density market keep Victorian contractors busy and keep estimators under pressure to turn drawings into numbers fast.",
        "market": "Victorian builders work under Domestic Building Contracts Act limits on variations, so getting the number right before contract signing matters more than anywhere else. We price Melbourne takeoffs against current Victorian supplier quotes and EBA-influenced labour rates on commercial work.",
        "projects": "townhouse and apartment developments in Brunswick, Footscray and Box Hill, industrial estates in Truganina and Dandenong South, aged-care and childcare facilities, school capital works and retail refurbishments",
        "lat": -37.8136, "lng": 144.9631,
    },
    {
        "slug": "gold-coast", "name": "Gold Coast", "state": "QLD", "region": "Gold Coast and Northern NSW",
        "suburbs": "Southport, Surfers Paradise, Broadbeach, Robina, Coomera, Burleigh and Tweed Heads",
        "intro": "The Gold Coast combines high-rise beachfront towers with fast-growing northern suburbs and a light-rail corridor, giving local builders a mix of luxury residential, hospitality and civil work that each needs its own estimating approach.",
        "market": "Coastal projects carry wind-rating, corrosion and flood-level requirements that change material selections and costs. Our Gold Coast estimates account for cyclone-rated fixings, marine-grade finishes and the premium that comes with constrained beachfront sites.",
        "projects": "beachfront apartment towers, Coomera and Pimpama housing estates, hospitality fit-outs in Broadbeach and Burleigh, aged-care developments, and light-rail precinct commercial buildings",
        "lat": -28.0167, "lng": 153.4000,
    },
    {
        "slug": "perth", "name": "Perth", "state": "WA", "region": "Perth and Western Australia",
        "suburbs": "Perth CBD, Joondalup, Rockingham, Mandurah, the eastern suburbs and regional WA mining towns",
        "intro": "Perth's residential market is running at record lead times while resources projects pull skilled labour north. Estimating in Western Australia means pricing scarcity as carefully as quantities.",
        "market": "WA builders face the longest material lead times in the country and labour costs inflated by the mining sector. Our Perth takeoffs flag long-lead items early and price against current Western Australian supplier quotes so your tender survives the gap between pricing and procurement.",
        "projects": "single and double-storey housing across the northern and southern corridors, apartment projects in the CBD and Subiaco, industrial facilities in Kwinana and Henderson, school and health upgrades, and regional mining-town accommodation",
        "lat": -31.9523, "lng": 115.8613,
    },
]

# Each article: slug, title (H1 + <title>), meta description, focus keyword, reading time, sections [(h2, [paragraphs or lists])]
ARTICLES = [
    {
        "slug": "what-is-a-quantity-takeoff",
        "title": "What Is a Quantity Takeoff? A Plain-English Guide for Builders",
        "desc": "A quantity takeoff lists every material a project needs, measured from the drawings. How takeoffs work, what they include and the mistakes to avoid.",
        "keyword": "quantity takeoff",
        "date": "2026-11-03",
        "summary": "A quantity takeoff is the measured list of materials and labour items a project needs, taken directly from the drawings. It is the foundation of every reliable construction estimate.",
        "sections": [
            ("Quantity takeoff, defined", [
                "A quantity takeoff (QTO), also called a material takeoff, is the process of measuring every item a construction project requires straight from the plans and specifications: cubic metres of concrete, square metres of plasterboard, lineal metres of pipe, numbers of doors, fixtures and fittings. The output is a structured list of quantities, grouped by trade, that an estimator then prices.",
                "The word takeoff comes from the practice of 'taking off' dimensions from the drawings. Today that work is done on screen in tools such as Bluebeam, PlanSwift and CostX, but the discipline is unchanged: count and measure everything once, accurately, and record where each quantity came from.",
            ]),
            ("What a takeoff actually includes", [
                "A complete takeoff goes well beyond the obvious materials. For a concrete slab, for example, the list covers the concrete volume by strength grade, reinforcing mesh and bar by size, bar chairs, vapour barrier, edge formwork, waste factors, pump hire and curing compound.",
                ["Quantities by trade: site work, concrete, masonry, structural steel, framing, roofing, plasterboard, finishes, plumbing, electrical and mechanical",
                 "Units that match how the trade buys: tonnes of steel, sheets of plasterboard, lineal metres of skirting",
                 "Waste and lap allowances appropriate to each material",
                 "Location references so every number can be traced back to a drawing and grid line",
                 "A summary sheet totalling each trade for pricing"],
            ]),
            ("Why takeoff accuracy decides your margin", [
                "Studies of tender outcomes consistently show that most cost blowouts trace back to quantities that were missed or double counted, not to unit rates. A rate that is 5% out on one trade is survivable. A missed lift pit, an unmeasured retaining wall or a plasterboard area counted once instead of both sides is not.",
                "Accurate quantities also sharpen your subcontractor comparisons. When you issue a measured bill to three plumbers, their prices become comparable line by line, and the outlier who missed something is obvious before you sign.",
            ]),
            ("Common takeoff mistakes", [
                ["Scaling from PDFs that were not plotted at the stated scale (always calibrate from a known dimension)",
                 "Measuring floor areas once and forgetting that walls, ceilings and floors each need their own quantity",
                 "Ignoring revisions: a takeoff from superseded drawings is worse than no takeoff",
                 "Applying one blanket waste percentage to every material",
                 "Forgetting temporary works, scaffolding, cranage and site establishment"],
            ]),
            ("Doing it in-house versus outsourcing", [
                "A detailed takeoff for a mid-size commercial project takes an experienced estimator two to five days. For a contractor pricing six tenders a month that is a full-time role, and the work arrives in bursts that rarely match staff capacity.",
                "Outsourced estimating firms like Qestimation absorb those peaks. You send the drawings, we return a trade-by-trade takeoff with colour-coded marked plans and a priced summary, usually within two to five business days. Learn more about our quantity takeoff and pricing service or request a free quote.",
            ]),
        ],
    },
    {
        "slug": "construction-estimate-cost-australia",
        "title": "How Much Does a Construction Estimate Cost in Australia?",
        "desc": "What construction estimators charge in Australia per project, trade and hour, what moves the price, and how to get value from an outsourced estimate.",
        "keyword": "construction estimate cost",
        "date": "2026-11-01",
        "summary": "Outsourced construction estimates in Australia typically cost between a few hundred dollars for a single-trade takeoff and a low four-figure sum for a full commercial bid, far less than the margin lost on one mispriced tender.",
        "sections": [
            ("Typical price ranges", [
                "Estimating fees depend on scope, project size and turnaround. As a guide for the Australian market: a single-trade takeoff on a residential project (for example, framing or plasterboard for a house) starts in the low hundreds of dollars. A full multi-trade takeoff and priced estimate for a new home or small commercial fit-out sits in the high hundreds to low thousands. Large commercial, industrial or multi-residential bids are quoted individually and can run into several thousand dollars.",
                "Most firms, Qestimation included, quote a fixed fee per project after reviewing the drawings, so you know the cost before committing. Hourly rates for ad-hoc estimating support usually sit between $80 and $150 per hour.",
            ]),
            ("What moves the price up or down", [
                ["Number of trades: a concrete-only takeoff is far quicker than pricing all 30 trades of a commercial building",
                 "Drawing quality: clear, dimensioned CAD plans are faster than scanned sketches",
                 "Level of detail: a budget estimate from concept drawings is cheaper than a fully measured bid estimate",
                 "Turnaround: 24 to 48 hour rush service carries a premium",
                 "Pricing requirement: quantities only, or quantities plus current local unit rates and subcontractor allowances"],
            ]),
            ("How estimating fees compare with the alternatives", [
                "An in-house estimator in Australia costs $90,000 to $140,000 a year plus software, super and overheads, and still cannot flex with tender volume. A single missed item on a $2 million project can cost more than a year of outsourced estimating. Viewed that way, an estimate is not an expense but insurance on your margin.",
            ]),
            ("Getting value from an outsourced estimate", [
                ["Send complete drawing sets, specifications and any geotechnical or survey reports",
                 "Say what you need: quantities only, priced estimate or full tender submission",
                 "Ask for colour-coded marked plans so you can audit the measurement",
                 "Request an executive summary that lets you review the whole bid in one page",
                 "Confirm turnaround and revision policy before you start"],
                "Qestimation provides all of these as standard. See our value-added deliverables on the services page, or upload your drawings for a free, fixed-price quote.",
            ]),
        ],
    },
    {
        "slug": "bid-estimate-vs-budget-estimate",
        "title": "Bid Estimate vs Budget Estimate: Which One Does Your Project Need?",
        "desc": "Budget estimates test feasibility early; bid estimates price a tender to the dollar. The difference, expected accuracy and when to commission each.",
        "keyword": "bid estimate vs budget estimate",
        "date": "2026-10-28",
        "summary": "A budget estimate forecasts cost from early design to test feasibility, usually within 10 to 20 percent. A bid estimate is a fully measured, priced tender figure accurate to a few percent.",
        "sections": [
            ("Two estimates, two jobs", [
                "Developers and builders often ask for 'an estimate' when they need very different things. A budget (or conceptual) estimate answers the question 'can we afford to build this?' A bid estimate answers 'exactly what will we charge to build it?' Confusing the two leads to either an over-engineered feasibility study or a tender priced from guesswork.",
            ]),
            ("Budget estimating explained", [
                "Budget estimates are prepared from concept or schematic drawings, often before engineering is complete. Estimators use elemental rates (cost per square metre of floor area, per metre of external wall, per fixture) drawn from comparable projects, adjusted for location, site conditions and finish level. Expected accuracy is plus or minus 10 to 20 percent, and the estimate includes design contingency to cover what is not yet drawn.",
                "Use a budget estimate for feasibility studies, finance applications, early value engineering and setting a cost plan the design team must work within.",
            ]),
            ("Bid estimating explained", [
                "A bid estimate is built from a full quantity takeoff of construction-issue drawings. Every trade is measured, priced with current supplier and subcontractor rates, and loaded with preliminaries, overheads, margin and risk allowances. Accuracy is typically within 1 to 5 percent of final cost on a well-documented project.",
                "Use a bid estimate when you are submitting a tender, signing a fixed-price contract or finalising a construction loan draw-down schedule.",
            ]),
            ("Which to commission, and when", [
                ["Site acquisition or feasibility: budget estimate",
                 "Development approval and finance: budget estimate, refreshed at each design milestone",
                 "Tender or contract signing: bid estimate",
                 "During construction: cost controls to track the bid estimate against actuals"],
                "Qestimation delivers both. Our budget estimating service supports feasibility and design development, and our cost estimation service produces tender-ready bid figures with colour-coded takeoffs you can audit line by line.",
            ]),
        ],
    },
    {
        "slug": "win-more-construction-tenders",
        "title": "How to Win More Construction Tenders Without Cutting Your Margin",
        "desc": "Tender strategy for Australian contractors: accurate takeoffs, comparable subcontractor quotes, explicit risk pricing and bids clients trust.",
        "keyword": "win construction tenders",
        "date": "2026-10-24",
        "summary": "Contractors win more tenders by pricing from accurate quantities, comparing subcontractors line by line, pricing risk explicitly and presenting a bid the client can trust, not by shaving margin.",
        "sections": [
            ("Stop competing on margin", [
                "The lowest bid wins the job and often loses the money. Contractors with the best long-run win rates are rarely the cheapest; they are the most consistent. They price from measured quantities every time, so they never carry hidden fat that makes them uncompetitive, and they never leave out scope that turns a win into a loss.",
            ]),
            ("Price from quantities, not history", [
                "Square-metre rates from your last project are a sanity check, not a bid. Every project has a different structure-to-finish ratio, site condition and specification. A measured takeoff lets you price what is actually drawn and spot the expensive details (transfer slabs, acoustic walls, feature facades) that a rate-per-metre approach hides.",
            ]),
            ("Make subcontractor quotes comparable", [
                "Issue each trade a measured bill of quantities with your tender package. Quotes then come back against the same scope, and you can see immediately who has missed the lift pit or excluded the fire collars. Three comparable quotes beat eight incomparable ones.",
            ]),
            ("Price risk explicitly", [
                ["Separate contingency from margin so you can defend each in negotiation",
                 "Flag long-lead items and price escalation where delivery runs past six months",
                 "Qualify assumptions clearly: ground conditions, authority fees, latent conditions",
                 "Use the drawing register to list exactly which revisions the price is based on"],
            ]),
            ("Present a bid the client can trust", [
                "Clients and quantity surveyors reward transparency. A one-page executive summary, a trade-by-trade breakdown and marked-up plans showing what was measured tell the assessor your number is real. Qestimation's deliverables are designed for exactly this: see our work samples for the format, then upload your tender drawings for a fixed-price quote.",
            ]),
        ],
    },
    {
        "slug": "concrete-takeoff-guide",
        "title": "Concrete Takeoff Guide: Measuring Slabs, Footings and Reinforcement Correctly",
        "desc": "Step-by-step concrete takeoff: slab and footing volumes, mesh and bar, formwork, waste factors and the items estimators most often miss.",
        "keyword": "concrete takeoff",
        "date": "2026-10-20",
        "summary": "A concrete takeoff measures concrete volume by element and grade, reinforcement by mesh sheets and bar tonnage, formwork by face area, and adds pumping, finishing and curing items that are easy to miss.",
        "sections": [
            ("Break the structure into elements", [
                "Measure concrete by element, never as one lump: strip and pad footings, piers, ground slab, suspended slabs, columns, beams, walls, stairs and kerbs. Each element has a different strength grade, pour sequence, formwork cost and reinforcement ratio, and your concreter will price them separately.",
            ]),
            ("Concrete volume", [
                ["Slabs: area multiplied by thickness, plus thickenings, set-downs and edge beams measured separately",
                 "Footings: length multiplied by width multiplied by depth, from the structural schedule not the architectural plan",
                 "Columns and walls: cross-section multiplied by height between structural levels",
                 "Deduct voids larger than about 0.5 cubic metres; ignore small penetrations",
                 "Add 5 to 10 percent waste for slabs on ground, less for formed elements"],
            ]),
            ("Reinforcement", [
                "Mesh is measured in sheets after allowing for laps (typically one square plus 25 millimetres each way). Bar is measured by diameter and converted to tonnes using standard mass per metre, with laps, hooks and cogs added. Do not forget trench mesh in footings, bar chairs, tie wire and starter bars for walls and columns.",
            ]),
            ("Formwork and finishing", [
                "Formwork is measured by contact area: slab edges by lineal metre and depth, columns and walls by face area, soffits by plan area. Add finishing items separately: steel trowel or burnished finish, broom finish, curing compound, saw cuts and joint sealant, vapour barrier under slabs and termite protection where required.",
            ]),
            ("Items that get missed", [
                ["Concrete pump hire and line pump versus boom pump",
                 "Testing (slump and cylinders) required by the specification",
                 "Set-downs for wet areas and tiles",
                 "Blinding concrete under footings",
                 "Out-of-hours pours and traffic management on tight sites"],
                "Qestimation's concrete estimates cover every item above with colour-coded plans showing exactly what was measured. Download a concrete estimate sample from our work samples page, or send your structural drawings for a free quote.",
            ]),
        ],
    },
    {
        "slug": "outsourcing-construction-estimating",
        "title": "Outsourcing Construction Estimating: Pros, Cons and How to Choose a Provider",
        "desc": "Should you outsource estimating? Costs, turnaround, accuracy and control compared, plus a checklist for choosing an estimating company in Australia.",
        "keyword": "outsource construction estimating",
        "date": "2026-10-15",
        "summary": "Outsourcing estimating gives builders fixed per-project costs, fast turnaround and specialist accuracy, at the cost of some control. Choosing a provider that shows its working closes that gap.",
        "sections": [
            ("Why builders outsource", [
                ["Tender volume is lumpy, and salaried estimators are idle or overloaded",
                 "A fixed fee per project is easier to carry into the bid than overhead",
                 "Specialist estimators measure faster and more consistently",
                 "Fast turnaround lets you price more tenders and win more work",
                 "Independent numbers give owners and lenders confidence"],
            ]),
            ("The real drawbacks", [
                "You lose some control over assumptions, and a provider that does not know your subcontractor base may use generic rates. Communication delays can hurt on fast tenders, and a cheap provider that returns a spreadsheet without marked plans leaves you unable to check the work. All of these are solved by choosing the right firm and briefing it properly.",
            ]),
            ("What to look for in an estimating company", [
                ["Colour-coded marked plans with every takeoff so you can audit quantities",
                 "Pricing against current local rates for your state, not national averages",
                 "An executive summary plus trade-by-trade detail",
                 "Clear turnaround commitments and a revision policy",
                 "Sample estimates you can review before engaging them",
                 "Secure handling of your drawings and tender information"],
            ]),
            ("How to brief an estimator", [
                "Send the full drawing set with revision numbers, the specification, geotechnical and survey reports, your preferred trade breakdown and any known subcontractor rates you want applied. Tell them the deadline and whether you need quantities only or a fully priced estimate.",
                "Qestimation works this way with developers, head contractors and subcontractors across Australia. Review our estimate samples, read about our services, or upload your drawings for a fixed-price quote returned within 24 hours.",
            ]),
        ],
    },
]
