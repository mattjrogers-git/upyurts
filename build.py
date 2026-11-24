#!/usr/bin/env python3
"""Builds the UP Yurts static site. Edit content here, run `python3 build.py`, commit.
Shared header/footer live in this file so every page stays consistent."""
import pathlib, datetime

SITE = "https://upyurts.info"
ORDER_URL = "https://form.jotform.com/261616096843059"  # TODO: order form (see README)
PHONE, PHONE_TEL, EMAIL = "845-384-2994", "+18453842994", "info@upyurts.info"
YEAR = datetime.date.today().year

NAV = [("index.html", "Home"), ("metal-yurt-roofs.html", "Why Metal"), ("features.html", "Features"),
       ("roof.html", "Sizes &amp; Prices"), ("faq.html", "FAQ"), ("about.html", "About")]

SIZES = [("12'", 3999, "6′0″ × 40″ × 26″", 850, "Liftgate or forklift"),
         ("15'", 5499, "7′8″ × 40″ × 28″", 1000, "Liftgate or forklift"),
         ("18'", 6900, "9′0″ × 42″ × 30″", 1250, "Forklift"),
         ("21'", 8350, "12′2″ × 45″ × 43″", 1600, "Forklift"),
         ("24'", 9999, "13′1″ × 45″ × 43″", 1900, "Forklift"),
         ("27'", 11599, "14′10″ × 45″ × 40″", 2150, "Forklift"),
         ("30'", 12999, "16′7″ × 45″ × 40″", 2400, "Forklift"),
         ("33'", 14999, "18′1″ × 46″ × 35″", 2690, "Forklift"),
         ("36'", 17999, "20′1″ × 46″ × 40″", 3450, "Forklift"),
         ("39'", 23999, "21′9″ × 48″ × 42″", 4000, "Forklift"),
         ("42'", 29999, "23′6″ × 50″ × 44″", 4700, "Forklift")]


def page(slug, title, desc, body, og_img="img/roof-finished.jpg"):
    nav = "".join(f'<a href="/{"" if h == "index.html" else h.replace(".html", "")}"'
                  f'{" aria-current=page" if h == slug else ""}>{t}</a>' for h, t in NAV)
    canon = SITE + "/" + ("" if slug == "index.html" else slug.replace(".html", ""))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{og_img}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="UP Yurts">
<link rel="icon" href="/assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@500&family=Nunito+Sans:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap">
<a class="logo" href="/"><img src="/assets/logo.png" alt="UP Yurts" width="148" height="50"></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">Menu</button>
<nav class="nav" id="nav">{nav}</nav>
<a class="head-phone" href="tel:{PHONE_TEL}">{PHONE}</a>
</div></header>
<main id="main">
{body}
{CONTACT}
</main>
<footer class="site-foot"><div class="wrap">
<span>© {YEAR} UP Yurts · New Paltz, NY</span>
<span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="/terms">Terms of Sale</a></span>
</div></footer>
</body>
</html>
"""


CONTACT = f"""<section class="contact"><div class="wrap split">
<div><h2>Questions? Ready to order?</h2>
<p>Tell us your yurt's diameter and roof pitch and we'll confirm the right roof size, delivery and unloading for your site.</p>
<div class="btns"><a class="btn light" href="mailto:{EMAIL}">Email us</a><a class="btn light" href="/roof#order">How to order</a></div></div>
<ul class="contact-list"><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li><li>New Paltz, NY</li></ul>
</div></section>"""


EAST = 1000  # extra freight east of the Mississippi


def size_table(prices=True, crate=False):
    head = "<th>Roof diameter</th>" + ("<th class=num>West of the Mississippi</th><th class=num>East of the Mississippi</th>" if prices else "") + \
           ("<th>Crate L × W × H</th><th class=num>Approx. weight</th><th>Unload with</th>" if crate else "")
    rows = ""
    for s, p, c, w, u in SIZES:
        rows += f"<tr><td>{s}</td>" + (f"<td class=num>${p:,}</td><td class=num>${p + EAST:,}</td>" if prices else "") + \
                (f"<td>{c}</td><td class=num>{w:,} lb</td><td>{u}</td>" if crate else "") + "</tr>"
    return f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'


PAGES = {}

PAGES["index.html"] = ("UP Yurts | Metal Yurt Roofs | Replacement Roofs for Yurts",
"Galvanized steel replacement roofs for yurts and round houses. 11 sizes from 12' to 42', built for a 70-year life, with freight to your door included.",
f"""<div class="hero">
<video autoplay muted loop playsinline poster="/img/roof-finished.jpg"><source src="/media/roof-drone-1.mp4" type="video/mp4"></video>
<div class="wrap">
<h1>UP Yurts</h1>
<p class="lead">Metal replacement roofs for yurts, and new roofs for any round building.</p>
<p class="sub">We protect your yurt investment, starting with what's up above your head: the roof.</p>
<div class="btns"><a class="btn solid" href="/roof">Sizes &amp; prices</a><a class="btn light" href="/metal-yurt-roofs">Why a metal roof?</a></div>
</div></div>

<section><div class="wrap">
<div class="facts">
<div class="fact"><b>24 ga</b><span>galvanized steel, nearly twice as thick as residential metal roofing</span></div>
<div class="fact"><b>70 yrs</b><span>average roof life, versus 10–15 years for a fabric cover</span></div>
<div class="fact"><b>12'–42'</b><span>11 sizes for any yurt with a 30° roof pitch</span></div>
<div class="fact"><b>1–3 days</b><span>typical install, right over your existing cover</span></div>
</div></div></section>

<section class="alt"><div class="wrap split">
<div class="split-media"><img src="/img/img_3580.jpg" alt="Installing metal roof panels on a yurt" loading="lazy"></div>
<div><p class="kicker">Replace the roof once</p>
<h2>A steel roof that outlasts five fabric covers</h2>
<p>Fabric yurt roofs wear out every 10 to 15 years. An UP Yurts metal roof is a one-time investment: heavy galvanized steel panels that shed snow, stop falling branches and hail, and keep your walls dry under a wide overhang.</p>
<p>Screw-down roofs go right over your existing fabric cover, so your yurt is never open to the weather during the install.</p>
<div class="btns"><a class="btn" href="/metal-yurt-roofs">See the benefits</a></div></div>
</div></section>

<section><div class="wrap split flip">
<div class="split-media"><div class="video-box"><video controls muted playsinline preload="none" poster="/img/img_3600.jpg"><source src="/media/roof-drone-2.mp4" type="video/mp4"></video></div></div>
<div><p class="kicker">Will it fit?</p>
<h2>Two measurements tell you</h2>
<ul class="ticks"><li><b>Roof pitch:</b> our roofs fit any yurt with a 30° roof pitch, which most major yurt makers use. A level app on your phone will measure your rafters.</li>
<li><b>Diameter:</b> roofs come in 3-foot steps from 12' to 42'. We recommend going up one size for a generous 18-inch overhang.</li></ul>
<div class="btns"><a class="btn solid" href="/roof">Find your size</a><a class="btn" href="/faq">Read the FAQ</a></div></div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Recent install</h2>
<div class="gallery">
<img src="/img/img_3549.jpg" alt="Setting the first roof panels">
<img src="/img/img_3572.jpg" alt="Deep-rib galvanized roof panels">
<img src="/img/img_3599.jpg" alt="Finished roof panels">
<img src="/img/img_3569.jpg" alt="Roof center ring opening">
</div></div></section>""")

PAGES["metal-yurt-roofs.html"] = ("Why a Metal Yurt Roof | UP Yurts",
"Why replace a fabric yurt roof with galvanized steel: strength, a 70-year life, lower lifetime cost, wide overhangs, no chemical coatings and protection from falling branches.",
"""<div class="page-head"><div class="wrap"><p class="kicker">Why metal</p><h1>The benefits of a metal roof for your yurt</h1>
<p>Makes vinyl seem like flimsy fabric. Here's what changes when you put steel over your head instead.</p></div></div>

<section><div class="wrap split">
<div class="split-media"><img src="/img/img_3572.jpg" alt="Deep-rib galvanized steel roof panels" loading="lazy"></div>
<div><h2>Strength and durability</h2>
<p>Our metal yurt roofs are built to stand up to the weather for 70 years.</p>
<ul class="ticks"><li>Regular residential metal roofing is 29 gauge; high-end residential is 26 gauge. Our roofs are 24 gauge or thicker galvanized steel, nearly twice as thick.</li>
<li>The steel is galvanized to G-115: a zinc coating of 1.15 oz per square foot, nearly twice the protection of standard roofing.</li>
<li>One-piece, deep-rib panels with 3¼-inch (82 mm) box ribs carry heavy snow and ice loads.</li>
<li>Each roof is made of 24 or 36 panels depending on diameter, with a weather-tight closure.</li></ul></div>
</div></section>

<section class="alt"><div class="wrap split flip">
<div class="split-media"><img src="/img/img_3580.jpg" alt="Crew installing panels over the existing yurt cover" loading="lazy"></div>
<div><h2>Easy to assemble</h2>
<p>Every bolt hole is pre-punched, so most roofs go together in 1 to 3 days, depending on your crew and the size of the roof.</p>
<p>Standard metal roofing screws fasten the panels to your rafters, straight through your old yurt cover. Leaving the fabric cover in place means your yurt is never open to the weather, even mid-install.</p></div>
</div></section>

<section><div class="wrap split">
<div class="split-media"><img src="/img/img_3599.jpg" alt="Finished galvanized roof panels" loading="lazy"></div>
<div><h2>Lower lifetime cost and maintenance</h2>
<p>A fabric roof needs replacing every 10 to 15 years. You <i>might</i> get 20 from a premium cover, but one leak and the savings go down the drain.</p>
<p>Our metal roofs last an average of 70 years, saving you the cost and hassle of 5 to 7 fabric covers: a 75% or greater savings over the life of the roof. You can paint the roof at any time to extend its life or change its color.</p></div>
</div></section>

<section class="alt"><div class="wrap split flip">
<div class="split-media"><img src="/img/roof-finished.jpg" alt="Finished metal yurt roof with wide overhang" loading="lazy"></div>
<div><h2>Wide roof overhangs</h2>
<p>A metal roof can carry a wide overhang that keeps rain off your walls, so you can leave windows open in a light rain.</p>
<p>Dry walls mean longer-lasting side covers and less time scrubbing mold and mildew off the fabric.</p></div>
</div></section>

<section><div class="wrap split">
<div class="split-media"><img src="/img/img_3596.jpg" alt="Galvanized steel roof seen from the peak" loading="lazy"></div>
<div><h2>Safe for the chemically sensitive</h2>
<p>Galvanized steel contains three elements: iron, carbon and zinc. No algicides, mildewcides, plasticizers, chlorine compounds or proprietary coatings, unlike fabric yurt roofs.</p>
<p>Whatever the brand name, fabric roof covers are vinyl-coated fabrics that can contain chemicals such as BPA, which leach into the air and water.</p></div>
</div></section>

<section class="alt"><div class="wrap split flip">
<div class="split-media"><img src="/img/roof-2013.jpg" alt="Metal yurt roof in the woods" loading="lazy"></div>
<div><h2>Protection from falling objects</h2>
<p>A metal roof puts solid steel between you and falling branches or hail.</p>
<p>Would you rather have steel or fabric between you and a falling tree limb?</p>
<div class="btns"><a class="btn solid" href="/roof">See sizes &amp; prices</a></div></div>
</div></section>""")

PAGES["features.html"] = ("Metal Yurt Roof Features | UP Yurts",
"24-gauge G-115 galvanized steel panels, bolt-together or screw-down installation, 11 sizes from 12' to 42', and a fit for any yurt with a 30-degree roof pitch.",
"""<div class="page-head"><div class="wrap"><p class="kicker">Features</p><h1>Built like nothing else on a yurt</h1>
<p>Steel panels, precision-formed, in a size for every yurt and round house.</p></div></div>

<section><div class="wrap split">
<div class="split-media tall"><img src="/img/img_3540.jpg" alt="Nested roof panels in the shipping crate" loading="lazy"></div>
<div><h2>Solid steel construction</h2>
<p>Thick 24-gauge galvanized steel is CNC-folded into the pie-shaped panels that make up each roof.</p>
<p>The high-strength steel is coated to the G-115 specification, a zinc coating nearly 60% thicker than most other metal roofs. That means a longer life and less maintenance.</p></div>
</div></section>

<section class="alt"><div class="wrap split flip">
<div class="split-media"><img src="/img/img_3588.jpg" alt="Panels bolted together at the ribs" loading="lazy"></div>
<div><h2>Bolt-together or screw-down installation</h2>
<p><b>Bolt-together roofs</b> are for new construction, or structures with bare rafters where you can reach the panels from inside. Every panel has pre-punched holes, only a few fastener sizes are needed, and the only tools are a drill, a ½-inch socket or wrench, and a ¼-inch punch or rod to line up the holes.</p>
<p><b>Screw-down roofs</b> are for fabric yurts with an existing roof cover. They fasten with standard metal roofing screws driven through the cover into the rafters.</p>
<p>The average roof installs in 1 to 3 days, depending on your crew and the roof size.</p></div>
</div></section>

<section><div class="wrap split">
<div class="split-media"><img src="/img/img_3544.jpg" alt="Metal roof going onto a yurt" loading="lazy"></div>
<div><h2>A range of sizes</h2>
<p>Roofs come in 3-foot steps from 12' to 42': 12', 15', 18', 21', 24', 27', 30', 33', 36', 39' and 42'.</p>
<p>Each roof is 3 to 5 inches larger than its stated size, so a 30' roof fits a 30' yurt. When the sizes match exactly, we recommend going up one size.</p>
<p>Larger and smaller roofs are available on request. For round-house builds (not yurt replacements) we offer higher snow-load ratings, roof hatches, covered vents and ladder rungs.</p></div>
</div></section>

<section class="alt"><div class="wrap split flip">
<div class="split-media"><img src="/img/img_3553.jpg" alt="Measuring rafters on a yurt" loading="lazy"></div>
<div><h2>Fits every yurt with a 30° roof pitch</h2>
<p>If your yurt has a 30-degree roof pitch, the roof will fit. Most major yurt makers use this angle.</p>
<p>Any protractor, angle finder or free level app on your phone will measure your rafters. Take several readings and average them.</p>
<div class="btns"><a class="btn solid" href="/roof">Sizes &amp; prices</a></div></div>
</div></section>""")

PAGES["roof.html"] = ("Metal Yurt Roof Sizes & Prices | UP Yurts",
"Prices for UP Yurts metal roofs from 12' ($3,999) to 42' ($29,999). Freight is included west of the Mississippi; add $1,000 east of the Mississippi.",
f"""<div class="page-head"><div class="wrap"><p class="kicker">Sizes &amp; prices</p><h1>Metal Yurt Roof</h1>
<p>Our metal roofs fit 98% of yurts and round houses: any roof with a 30° pitch. Premium galvanized steel, built for a 70-year life, in 11 sizes from 12' to 42'.</p></div></div>

<section><div class="wrap split">
<div>
<h2>Prices</h2>
<p class="note"><b>Freight is included in every price.</b> Delivery east of the Mississippi River costs <b>$1,000 more</b> because freight there is higher, so both prices are shown.</p>
{size_table()}
<p>Hawaii, Alaska and Canada pay the west price: we deliver to your chosen logistics company in the lower 48, and final delivery from there is at your expense. Prices exclude sales tax, which applies where required, including roofs picked up in New York.</p>
</div>
<div><div class="video-box"><video controls muted playsinline preload="none" poster="/img/roof-finished.jpg"><source src="/media/roof-drone-1.mp4" type="video/mp4"></video></div>
<h3 style="margin-top:24px">Every roof includes</h3>
<ul class="ticks"><li>24-gauge G-115 galvanized steel panels with pre-punched holes</li>
<li>A 22-inch center opening on 12' and 15' roofs; a factory-finished 36-inch peak opening on 18' and larger</li>
<li>Freight delivery in one wooden crate by LTL truck</li></ul>
<h3>Option</h3>
<ul class="ticks"><li>60-inch dome flashing kit: $150. Choose it on the order form.</li></ul></div>
</div></section>

<section class="alt" id="order"><div class="wrap">
<h2>How to order</h2>
<ol class="steps">
<li><b>Measure your yurt.</b> Confirm a 30° roof pitch and your diameter. Not sure which size? <a href="mailto:{EMAIL}">Email us</a> and we'll confirm it with you.</li>
<li><b>Fill out the order form.</b> Choose your roof size, delivery location (west or east of the Mississippi), the optional dome flashing kit, and how you'll pay. The form totals your order and deposit.</li>
<li><b>Pay a 50% deposit</b> by ACH bank debit or check. Your roof goes into production once the deposit clears.</li>
<li><b>Pay the balance</b> about one week before your roof ships. We email you the amount and date first.</li>
</ol>
<div class="btns"><a class="btn solid" href="{ORDER_URL}">Order form</a><a class="btn" href="/terms">Terms of Sale</a></div>
<p class="note">Please check your measurements before ordering. Roofs are made to order and can't be returned once fabrication starts. See the <a href="/terms">Terms of Sale</a>.</p>
</div></section>

<section id="shipping"><div class="wrap">
<h2>Shipping, crate sizes and unloading</h2>
<p>Your roof arrives in one sturdy wooden crate on an LTL freight truck. Freight is included west of the Mississippi; east of the Mississippi it's $1,000 extra. Some remote locations are excluded. Hawaii, Alaska and Canada pay the west price for delivery to your chosen logistics company in the lower 48; final delivery from there is at your expense. You're responsible for unloading, and we're glad to help you plan it.</p>
{size_table(prices=False, crate=True)}
<p>Weights include about 200 lb of margin, so plan your equipment for the weight shown. Crate sizes vary by a few inches, and orders with extra parts can ship taller and heavier.</p>
<p>12' and 15' crates come off on the truck's liftgate. 18' and larger need a forklift. Crates over 20 feet (36'–42' roofs) are easiest with fork extensions or two forklifts, so contact us before delivery to plan it.</p>
<div class="btns"><a class="btn" href="/unloading">Step-by-step unloading guide</a></div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Returns</h2>
<p>Roofs are made to order and can't be returned once opened. Inspect your crate when it arrives and note any freight damage on the delivery receipt before you sign, then tell us in writing within 5 business days so we can help with the carrier claim. See the <a href="/terms">Terms of Sale</a> for warranty and claim details.</p>
</div></section>""")

PAGES["unloading.html"] = ("Unloading Your Roof Crate | UP Yurts",
"Step-by-step forklift instructions for unloading an UP Yurts metal roof crate from an LTL freight truck, with or without a liftgate.",
f"""<div class="page-head"><div class="wrap"><p class="kicker">Delivery day</p><h1>Unloading your roof crate</h1>
<p>Your roof ships in one long wooden crate, from about 6 feet and 850 lb for a 12' roof up to 23½ feet and 4,700 lb for a 42' roof. Print this page for delivery day.</p></div></div>

<section><div class="wrap">
<p>12' and 15' crates are short enough to come off on the truck's liftgate. 18' and larger crates arrive in an enclosed LTL trailer, and you unload them with one forklift working from the ground. A crate this long can't be carried safely from one end, so keep one end supported while the forklift moves the other, then lift the crate from the side at its center. See your crate's size and weight on the <a href="/roof">Sizes &amp; prices</a> page.</p>
<p><a href="https://www.youtube.com/shorts/4uMBuf5D_44">Watch the short unloading video</a></p>

<h2>What you need</h2>
<ul class="ticks">
<li>A forklift rated above your crate's weight at a 24-inch load center (5,000 lb or more covers every size), with forks 42 inches or longer.</li>
<li>Blocking that holds at least half the crate's weight at trailer-floor height, 48 to 52 inches for a standard trailer: a heavy-duty sawhorse or stand, or 8 to 9 pallets stacked flat. Needed only if there's no liftgate.</li>
<li>A helper, shims, a tape measure, and firm, level ground: your crate's length plus 17 feet clear behind the trailer.</li></ul>

<h2>When the truck arrives</h2>
<ol class="steps">
<li>Photograph the crate and write any damage on the delivery receipt before you sign.</li>
<li>Ask the driver to set the brakes and bring the crate to the rear door with one end facing out.</li>
<li>Measure the trailer floor height and set your blocking to match.</li></ol>

<h2>Method A: no liftgate</h2>
<ol class="steps">
<li>Raise the forks to floor height, spread them wide, and slide them under the end of the crate.</li>
<li>Lift that end an inch or two, tilt the mast back slightly, and back away slowly; the far end slides along the trailer floor.</li>
<li>Stop when only the last 6 to 12 inches is still on the trailer floor. Your helper watches that end so it never drops off the edge.</li>
<li>Your helper sets the blocking under the crate just past the fork tips, across its full width, with hands never under the crate.</li>
<li>Lower the crate onto the blocking, check that it's stable, and back the forks out.</li>
<li>Measure the crate and mark the center of its long side, halfway between the ends.</li>
<li>Drive up to the side, spread the forks wide, center them on the mark, and drive them fully under the crate.</li>
<li>Lift slowly until the crate clears the floor and the blocking. If one end stays down, set it back and shift the forks toward that end.</li>
<li>Back away slowly, steering so the trailing end swings clear of the door frame.</li>
<li>Carry the crate low and slow, and set it down on level ground.</li></ol>

<h2>Method B: with a liftgate</h2>
<ol class="steps">
<li>The driver raises the liftgate level with the trailer floor.</li>
<li>Pull the crate out by one end, as in Method A steps 1 and 2, until its trailing end is fully on the liftgate platform.</li>
<li>Lower together in small steps: the driver lowers the liftgate a few inches, then you match it with the forks, keeping the crate level.</li>
<li>Set your end down, back the forks out, and lift the crate from the side at its center mark, as in Method A steps 6 to 8.</li>
<li>Back straight away so it comes off the liftgate, and carry it low and slow to its spot.</li></ol>

<h2>Safety</h2>
<ul class="ticks">
<li>Never stand or reach under the crate, or between the crate and the trailer.</li>
<li>Never lift the whole crate from one end; the side lift at the center mark is the only full lift.</li>
<li>If anything shifts, set the crate down and reset.</li></ul>
<p class="note">Questions before delivery day? Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
</div></section>""")

FAQ = [
("What sizes do you offer?", "Our metal roofs come in 11 sizes: 12', 15', 18', 21', 24', 27', 30', 33', 36', 39' and 42' diameters. Sizes are nominal; the actual diameter is 3 to 4 inches larger. We recommend going up one size for a generous 18-inch eave overhang. <a href=\"/roof\">See prices</a>."),
("How do I know if it will fit my yurt?", "Two measurements. First and most important is your roof angle: our roofs are made to a 30° pitch to match most major yurt makers, with a 1–2° tolerance. Second is your yurt's diameter."),
("What are the main benefits of a metal roof over a fabric roof?", "<ul class=ticks><li>A wide overhang keeps your walls dry, so windows can stay open in a light rain.</li><li>Thick steel protects you from falling branches and hail.</li><li>Our roofs last an average of 70 years, a 75% or greater savings over the life of the roof.</li><li>Galvanized steel contains only three elements: iron, carbon and zinc.</li></ul><a href=\"/metal-yurt-roofs\">More on the benefits</a>."),
("How will it work with my clear dome?", "Our 12' and 15' roofs have a 22-inch center opening. All sizes 18' and larger have a factory-finished 36-inch peak opening. An optional 60-inch dome flashing kit is available for $150. We'll also try to work with your existing dome and hardware, or provide a replacement dome."),
("How long does it take to install?", "Pre-punched bolt holes and fully formed flashing panels make the install quick. A competent crew can install a smaller roof in a day; larger roofs take 1 to 3 days depending on crew size and speed."),
("How much does the roof weigh? Can my yurt take the weight?", "Our roofs weigh about 2 to 2.5 pounds per square foot. Most yurt roofs are rated for 20 to 40 pounds per square foot or more, so this matters only if your yurt's rating is close to your local snow load. When engineered into a structure, the roof is designed for a 22 psf overall load; it doesn't increase your yurt's load capacity. Roof stiffeners and metal rafters are available for round houses."),
("What are the roof panels made of?", "High-quality galvanized steel with a G-115 coating (minimum 350 g/m² of zinc). No other roofing uses a thicker zinc coating, and zinc is what keeps steel from corroding."),
("Do your roofs fit round buildings other than yurts?", "Yes. Our roofs have been used on strawbale, earthbag and wood-frame round houses. The roof can be engineered into the structure as a complete rafter and roof system, or set on standard rafters."),
("How is my roof shipped?", "Freight to your address is included west of the Mississippi River; east of the Mississippi it costs $1,000 more. Some remote locations are excluded. Hawaii, Alaska and Canada pay the west price for delivery to your chosen logistics company in the lower 48, with final delivery at your expense. Your roof arrives as one sturdy wooden crate on an LTL freight truck. You're responsible for unloading, and we're happy to help you plan it."),
("What countries do you ship to?", "The US and Canada. For Hawaii, Alaska and Canada we deliver to your chosen logistics company in the lower 48 at the west-of-the-Mississippi price, and final delivery from there is at your expense."),
("How big and heavy is the crate?", "From 6 feet and 850 lb for a 12' roof up to 23½ feet and 4,700 lb for a 42' roof. Weights include about 200 lb of margin. <a href=\"/roof#shipping\">See the crate table</a> for every size."),
("How do I unload the crate?", "12' and 15' crates can come off on the truck's liftgate. 18' and larger roofs need a forklift. Crates over 20 feet (36'–42' roofs) are easiest with fork extensions or two forklifts, so contact us before delivery. Follow our <a href=\"/unloading\">step-by-step unloading guide</a>."),
("How do I order and pay?", "Fill out the order form with your size, delivery location and options, then pay a 50% deposit by ACH bank debit or check. The balance is due about a week before your roof ships. <a href=\"/roof#order\">How to order</a>."),
]
PAGES["faq.html"] = ("FAQ | Metal Yurt Roofs | UP Yurts",
"Answers about UP Yurts metal roofs: sizes, fit, domes, install time, weight, materials, shipping, crate sizes, unloading and ordering.",
"""<div class="page-head"><div class="wrap"><p class="kicker">FAQ</p><h1>Frequently asked questions</h1></div></div>
<section><div class="wrap">""" + "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in FAQ) + "</div></section>")

PAGES["about.html"] = ("About | UP Yurts",
"UP Yurts is run by Matt Rogers in New Paltz, NY, with more than 25 years of woodworking and yurt-building experience.",
"""<div class="page-head"><div class="wrap"><p class="kicker">About</p><h1>About UP Yurts</h1></div></div>
<section><div class="wrap split">
<div class="split-media"><img src="/img/about-yurt.jpg" alt="A yurt at sunset in the desert" loading="lazy"></div>
<div><p>Owner and operator Matt Rogers has more than 25 years of experience in woodworking and building yurts.</p>
<p>With the world's only metal yurt roof replacement system, he's helping yurts live longer, better lives and protecting their owners' investments.</p>
<p>UP Yurts is based in New Paltz, New York, in the Hudson Valley.</p>
<div class="btns"><a class="btn solid" href="/roof">Sizes &amp; prices</a></div></div>
</div></section>""")

TERMS_SRC = pathlib.Path(__file__).with_name("terms.html.part")
PAGES["terms.html"] = ("Terms and Conditions of Sale | UP Yurts",
"Terms and Conditions of Sale for UP Yurts metal yurt roof orders.",
"""<div class="page-head"><div class="wrap"><p class="kicker">Legal</p><h1>Terms and Conditions of Sale</h1></div></div>
<section><div class="wrap terms">""" + TERMS_SRC.read_text() + "</div></section>")

PAGES["404.html"] = ("Page not found | UP Yurts", "Page not found.",
"""<div class="page-head"><div class="wrap"><h1>Page not found</h1><p>That page has moved. Try the <a href="/">home page</a> or <a href="/roof">sizes &amp; prices</a>.</p></div></div>""")

if __name__ == "__main__":
    root = pathlib.Path(__file__).parent / "public"
    for slug, (t, d, b) in PAGES.items():
        (root / slug).write_text(page(slug, t, d, b))
    urls = [s for s in PAGES if s != "404.html"]
    (root / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"<url><loc>{SITE}/{'' if s == 'index.html' else s[:-5]}</loc></url>\n" for s in urls) + "</urlset>\n")
    print("built", len(PAGES), "pages")
