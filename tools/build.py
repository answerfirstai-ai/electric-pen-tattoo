import json,os,sys,html
sys.path.insert(0,os.path.dirname(__file__))
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE='/electric-pen-tattoo/'; SITE='https://answerfirstai-ai.github.io'+BASE
NAME='The Electric Pen Tattoo Studio'; PHONE='(818) 506-8828'; TEL='tel:+18185068828'
IG='https://www.instagram.com/theelectricpentattoo/'
DIR='https://www.google.com/maps/search/?api=1&query=The+Electric+Pen+Tattoo+Studio+10751+Magnolia+Blvd+North+Hollywood+CA+91601'
YELP='https://www.yelp.com/biz/the-electric-pen-tattoo-studio-north-hollywood'
V='19'
def need(t): return f'<span class="need">[NEED: {t}]</span>'
NAV=[('On the wall','flash/'),('Artists','artists/'),('Visit','visit/')]
def head(title,desc,path,extra='',extra_pre=''):
    url=SITE+path
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta name="theme-color" content="#1B231F"><meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}favicon.svg" type="image/svg+xml"><link rel="icon" href="{BASE}favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="{BASE}assets/img/icon-180.png"><link rel="manifest" href="{BASE}site.webmanifest">
<link rel="preload" href="{BASE}assets/fonts/archivo-narrow.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{BASE}assets/fonts/grenze.woff2" as="font" type="font/woff2" crossorigin>{extra_pre}
<link rel="stylesheet" href="{BASE}assets/css/site.css?v={V}">
<script>document.documentElement.classList.add('js')</script>{extra}</head>'''
def header(cur):
    links=''.join(f'<a class="wl" href="{BASE}{h}"{" aria-current=page" if cur==h else ""}>{t}</a>' for t,h in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a><header class="nav"><a class="mark" href="{BASE}" aria-label="{NAME}, home"><span>The Electric Pen</span></a>
<nav class="dnav" aria-label="Main">{links}</nav><details class="mnav"><summary aria-label="Open menu">Menu</summary><nav aria-label="Mobile">{links}<a class="wl" href="{TEL}">Call {PHONE}</a></nav></details><a class="btn btn-y nav-call" href="{TEL}">Call {PHONE}</a><i class="buzz" aria-hidden="true"></i></header>'''
def ctas(cls=''): return f'<div class="ctas {cls}"><a class="btn btn-y" href="{TEL}">Call {PHONE}</a><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Directions</a><a class="btn btn-o" href="{IG}" target="_blank" rel="noopener">Instagram</a></div>'
def footer(body=''):
    fn=("The machine on this page is a 3D illustration, not the studio's equipment. " if 'machine-' in body else '')+("The hero scene is an AI illustration. " if 'hero-d-' in body else '')
    return f'''<footer class="foot"><div class="fwrap"><div><p class="fname">{NAME}</p><p>10751 Magnolia Blvd, North Hollywood, CA 91601</p>
<p><a class="wl" href="{TEL}">{PHONE}</a></p><p>Open daily, 12 PM to 8 PM</p></div><nav class="fnav" aria-label="Footer"><p class="flab">Pages</p><a class="wl" href="{BASE}">Home</a><a class="wl" href="{BASE}artists/">Artists</a><a class="wl" href="{BASE}flash/">Work</a><a class="wl" href="{BASE}visit/">Visit</a></nav>
<div><p class="flab">Find us elsewhere</p><p><a class="wl" href="{IG}" target="_blank" rel="noopener">Instagram</a> · <a class="wl" href="{YELP}" target="_blank" rel="noopener">Yelp</a></p>
<p class="fnote">Images marked “Illustrative scene” are AI-generated or rendered. They are not photos of The Electric Pen, its people or its tattoo work.</p></div></div></footer>
<div class="mbar"><a class="btn btn-y" href="{TEL}">Call</a><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Directions</a></div>'''
SCRIPTS=f'<script src="{BASE}assets/js/gsap.min.js" defer></script><script src="{BASE}assets/js/ScrollTrigger.min.js" defer></script><script src="{BASE}assets/js/site.js?v={V}" defer></script>'
def page(path,title,desc,body,cur='',ld=None,art=()):
    ldj=f'<script type="application/ld+json">{json.dumps(ld,separators=(",",":"))}</script>' if ld else ''
    h=head(title,desc,path,ldj,PRE.get(path,''))+f'<body class="p-{cur.strip("/") or "home"}">'+''+header(cur)+f'<main id="main">{body}</main>'+footer(body)+SCRIPTS+'</body></html>'
    fp=os.path.join(ROOT,path,'index.html') if not path.endswith('.html') else os.path.join(ROOT,path)
    os.makedirs(os.path.dirname(fp),exist_ok=True); open(fp,'w').write(h)

ALL=[]
BUSINESS={"@type":["TattooParlor","LocalBusiness"],"@id":SITE+"#studio","name":NAME,"url":SITE,"telephone":"+1-818-506-8828",
 "logo":SITE+"assets/img/icon-512.png",
 "address":{"@type":"PostalAddress","streetAddress":"10751 Magnolia Blvd","addressLocality":"North Hollywood","addressRegion":"CA","postalCode":"91601","addressCountry":"US"},
 "areaServed":"North Hollywood, CA","geo":{"@type":"GeoCoordinates","latitude":34.1650733,"longitude":-118.3655833},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"12:00","closes":"20:00"}],"hasMap":DIR,"sameAs":[IG,YELP],
 "knowsAbout":["Tattooing"],"image":{"@type":"ImageObject","url":SITE+"assets/img/og.jpg","creditText":"Illustrative (AI-generated)"}}
def ld(path,crumb=None):
    g=[dict(BUSINESS,**{"@context":"https://schema.org"})] if not crumb else [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE},{"@type":"ListItem","position":2,"name":crumb,"item":SITE+path}]},{"@context":"https://schema.org","@id":SITE+"#studio","@type":["TattooParlor","LocalBusiness"],"name":NAME,"telephone":"+1-818-506-8828","url":SITE}]
    return g if len(g)>1 else g[0]

HOURS='Open daily, 12 PM to 8 PM.'
WALKIN='Listings say walk-ins are welcome; call ahead at (818) 506-8828 to check the wait.'

PRE={'':f'<link rel="preload" as="image" type="image/avif" media="(min-width:901px)" imagesrcset="{BASE}assets/img/hero-d-1280.avif 1280w, {BASE}assets/img/hero-d-1920.avif 1920w, {BASE}assets/img/hero-d-2560.avif 2560w, {BASE}assets/img/hero-d-2880.avif 2880w" imagesizes="100vw" fetchpriority="high"><link rel="preload" as="image" type="image/avif" media="(max-width:900px)" imagesrcset="{BASE}assets/img/hero-m-800.avif 800w, {BASE}assets/img/hero-m-1200.avif 1200w, {BASE}assets/img/hero-m-1600.avif 1600w" imagesizes="100vw" fetchpriority="high">'}
LAB3D='<figcaption class="illus">3D illustration. Not the studio\'s equipment.</figcaption>'
def machine_pic(sizes,eager=False):
    ss=lambda e:', '.join(f'{BASE}assets/img/machine-{w}.{e} {w}w' for w in (480,800,1024))
    ld='fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<figure class="ph m-fallback"><picture><source type="image/avif" srcset="{ss("avif")}" sizes="{sizes}"><source type="image/webp" srcset="{ss("webp")}" sizes="{sizes}"><img src="{BASE}assets/img/machine-800.webp" width="1024" height="1024" alt="3D illustration: a generic chrome and brass coil tattoo machine on black" {ld}></picture>{LAB3D}</figure>'
def tag(t): return f'<span class="tag">{t}</span>'
def pin(): return '<span class="pin" aria-hidden="true"></span>'
def ctas_core(): return f'<a class="btn btn-y" href="{TEL}">Call {PHONE}</a><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Directions</a>'
def footer(body=''):
    fn=("The machine on this page is a 3D illustration, not the studio's equipment. " if 'machine-' in body else '')+("The hero scene is an AI illustration. " if 'hero-d-' in body else '')
    return f'''<footer class="foot"><div class="sheet f-sheet" style="--r:-.4deg">{pin()}{tag("last sheet")}<p class="fname">The Electric Pen</p>
<p>10751 Magnolia Blvd, North Hollywood 91601. <a class="wl" href="{TEL}">{PHONE}</a>. Open daily, 12 to 8.</p>
<nav class="fnav" aria-label="Footer"><a class="wl" href="{BASE}">Home</a><a class="wl" href="{BASE}flash/">On the wall</a><a class="wl" href="{BASE}artists/">Artists</a><a class="wl" href="{BASE}visit/">Visit</a><a class="wl" href="{IG}" target="_blank" rel="noopener">Instagram</a><a class="wl" href="{YELP}" target="_blank" rel="noopener">Yelp</a></nav>
<p class="fnote">{fn}Map data © OpenStreetMap contributors.</p></div></footer>
<div class="mbar"><a class="btn btn-y" href="{TEL}">Call</a><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Directions</a></div>'''
def wall_sec(h='h2'):
    return f'''<section class="sec wallsec" id="work"><{h} class="sec-t">On the wall</{h}><div class="wall">
<figure class="sheet s-big s-port" style="--r:-.6deg">{pin()}<div class="ig-grid"><a class="ig-c" href="https://www.instagram.com/theelectricpentattoo/p/DHxy7cFRXS4/" target="_blank" rel="noopener"><picture><source type="image/avif" srcset="{BASE}assets/img/ig/ig01-540.avif 540w, {BASE}assets/img/ig/ig01-1080.avif 1080w" sizes="(min-width:901px) 248px, 45vw"><img src="{BASE}assets/img/ig/ig01-540.webp" srcset="{BASE}assets/img/ig/ig01-540.webp 540w, {BASE}assets/img/ig/ig01-1080.webp 1080w" sizes="(min-width:901px) 248px, 45vw" width="540" height="540" alt="Ornate tattoo across the wrist and hand, from the studio's Instagram (co-posted with @boadamsart)" loading="lazy" decoding="async"></picture></a><a class="ig-c" href="https://www.instagram.com/theelectricpentattoo/p/DIB3NtwJDKf/" target="_blank" rel="noopener"><picture><source type="image/avif" srcset="{BASE}assets/img/ig/ig02-540.avif 540w, {BASE}assets/img/ig/ig02-1080.avif 1080w" sizes="(min-width:901px) 248px, 45vw"><img src="{BASE}assets/img/ig/ig02-540.webp" srcset="{BASE}assets/img/ig/ig02-540.webp 540w, {BASE}assets/img/ig/ig02-1080.webp 1080w" sizes="(min-width:901px) 248px, 45vw" width="540" height="540" alt="Skull tattoo on an arm, from the studio's Instagram" loading="lazy" decoding="async"></picture></a><a class="ig-c" href="https://www.instagram.com/theelectricpentattoo/p/DHHrJPfyoDg/" target="_blank" rel="noopener"><picture><source type="image/avif" srcset="{BASE}assets/img/ig/ig03-540.avif 540w, {BASE}assets/img/ig/ig03-1080.avif 1080w" sizes="(min-width:901px) 248px, 45vw"><img src="{BASE}assets/img/ig/ig03-540.webp" srcset="{BASE}assets/img/ig/ig03-540.webp 540w, {BASE}assets/img/ig/ig03-1080.webp 1080w" sizes="(min-width:901px) 248px, 45vw" width="540" height="540" alt="Full-colour tattoo sleeve, from the studio's Instagram" loading="lazy" decoding="async"></picture></a><a class="ig-c" href="https://www.instagram.com/theelectricpentattoo/p/DGrmx2ppJIu/" target="_blank" rel="noopener"><picture><source type="image/avif" srcset="{BASE}assets/img/ig/ig04-540.avif 540w, {BASE}assets/img/ig/ig04-1080.avif 1080w" sizes="(min-width:901px) 248px, 45vw"><img src="{BASE}assets/img/ig/ig04-540.webp" srcset="{BASE}assets/img/ig/ig04-540.webp 540w, {BASE}assets/img/ig/ig04-1080.webp 1080w" sizes="(min-width:901px) 248px, 45vw" width="540" height="540" alt="Alien heart tattoo, from the studio's Instagram" loading="lazy" decoding="async"></picture></a></div><figcaption class="cap ig-cred">Photos: <a href="https://www.instagram.com/theelectricpentattoo/" target="_blank" rel="noopener">@theelectricpentattoo</a> · first photo with <a href="https://www.instagram.com/boadamsart/" target="_blank" rel="noopener">@boadamsart</a></figcaption></figure>
<div class="sheet s-svc s1" style="--r:.9deg">{pin()}{tag("listed")}<svg class="sk" viewBox="0 0 48 48" aria-hidden="true"><path d="M8 40 L30 18 M30 18 l6-6 4 4-6 6 M14 34 l-4 4"/><circle cx="40" cy="10" r="3"/></svg><h3>Custom tattoos</h3><p>Listings say the studio does custom work. Bring a reference; every piece is priced by quote.</p></div>
<div class="sheet s-svc s2" style="--r:-1.1deg">{pin()}{tag("listed")}<svg class="sk" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="26" r="12"/><circle cx="36" cy="26" r="3"/></svg><h3>Piercing</h3><p>Listings mention piercing. Call ahead to check who is in.</p></div>
<div class="sheet s-svc s3" style="--r:.5deg">{pin()}{tag("listed")}<svg class="sk" viewBox="0 0 48 48" aria-hidden="true"><rect x="7" y="10" width="34" height="28"/><path d="M12 33 l9-10 6 6 5-5 5 9"/></svg><h3>Gallery</h3><p>Listings mention an art gallery. Ask at the counter what is up now.</p></div>
</div></section>'''
def consult_sec(h='h2'):
    L=["Bring a reference, or pick a sheet off the wall.","Size, placement and a quote at the counter.",f"Deposit and date. <a href=\"{TEL}\">Call to confirm the deposit.</a>"]
    return f'''<section class="sec consult" id="booking"><div class="sheet rules" style="--r:.5deg">{pin()}{tag("house rules")}<{h}>Getting a consult</{h}><ol>'''+''.join(f'<li><span class="nc">{i+1}</span>{t}</li>' for i,t in enumerate(L))+f'''</ol><div class="ctas">{ctas_core()}</div></div>
<p class="side-note">Every piece is priced by quote. Ask about ID requirements and aftercare when you <a href="{TEL}">call</a>.</p></section>'''
def artists_sec(h='h2'):
    return f'''<section class="sec artists" id="artists"><{h} class="sec-t">Artists</{h}><div class="tags-row">
<div class="sheet ntag" style="--r:-1.5deg">{pin()}<p class="nt-h">Hello, my name is</p><p class="nt-n">Bo Adams</p><p class="nt-r">Owner</p></div>
<div class="sheet ntag" style="--r:1deg">{pin()}<p class="nt-h">Also on the wall</p><p class="nt-n">Resident artists</p><p class="nt-r">Ask about our resident artists and piercer</p></div></div>
<p class="side-note">Call and we'll match your idea to the right person. Bo is listed as owner on the studio's Tattoodo and Yelp pages.</p></section>'''
def visit_sec(h='h2'):
    return f'''<section class="sec visitsec" id="visit"><div class="sheet receipt" style="--r:-.7deg">{pin()}{tag("visit")}<{h}>10751 Magnolia Blvd</{h}><p>North Hollywood, CA 91601</p>
<p>Open daily, 12 to 8. {WALKIN}</p><div class="ctas">{ctas_core()}</div></div>
<a class="sheet mapsheet" style="--r:.6deg" href="{DIR}" target="_blank" rel="noopener">{pin()}<picture><source type="image/avif" srcset="{BASE}assets/img/map-360.avif 360w, {BASE}assets/img/map-720.avif 720w" sizes="(min-width:901px) 45vw, 92vw"><img src="{BASE}assets/img/map-720.webp" srcset="{BASE}assets/img/map-360.webp 360w, {BASE}assets/img/map-720.webp 720w" sizes="(min-width:901px) 45vw, 92vw" width="720" height="540" alt="Street map of Magnolia Blvd, North Hollywood, centered on 10751 Magnolia Blvd" loading="lazy" decoding="async"></picture><span class="mk-pin" aria-hidden="true"></span><span class="vh">Open in Google Maps</span><span class="osm">© OpenStreetMap contributors</span></a></section>'''
MACHINE=f'''<section class="sec machine" id="machine"><div class="m-stage"><div class="m-canvas" aria-hidden="true"></div>{machine_pic("(min-width:901px) 480px, 92vw")}</div><div class="m-copy"><h2>The coil machine</h2><p>Chrome frame, brass posts, copper coils. A 3D illustration of the classic tool.</p></div></section>'''

home=f'''<section class="hero"><div class="h-copy"><h1>The Electric Pen<span class="vh"> Tattoo Studio</span></h1><p class="lede">Tattoo studio at 10751 Magnolia Blvd, North Hollywood. Open daily, 12 to 8.</p><div class="ctas">{ctas_core()}</div><p class="addr-sm">Serving North Hollywood since 2005 (per the studio).</p></div><div class="h-bg"><picture><source media="(max-width:900px)" type="image/avif" srcset="{BASE}assets/img/hero-m-800.avif 800w, {BASE}assets/img/hero-m-1200.avif 1200w, {BASE}assets/img/hero-m-1600.avif 1600w" sizes="100vw"><source media="(max-width:900px)" type="image/webp" srcset="{BASE}assets/img/hero-m-800.webp 800w, {BASE}assets/img/hero-m-1200.webp 1200w, {BASE}assets/img/hero-m-1600.webp 1600w" sizes="100vw"><source type="image/avif" srcset="{BASE}assets/img/hero-d-1280.avif 1280w, {BASE}assets/img/hero-d-1920.avif 1920w, {BASE}assets/img/hero-d-2560.avif 2560w, {BASE}assets/img/hero-d-2880.avif 2880w" sizes="100vw"><source type="image/webp" srcset="{BASE}assets/img/hero-d-1280.webp 1280w, {BASE}assets/img/hero-d-1920.webp 1920w, {BASE}assets/img/hero-d-2560.webp 2560w, {BASE}assets/img/hero-d-2880.webp 2880w" sizes="100vw"><img src="{BASE}assets/img/hero-d-1920.webp" width="2880" height="1620" alt="Illustrative: a single sheet of tracing paper pinned to a dark plaster wall, with an original pencil stencil outline of a moth and crescent moon in raking light" fetchpriority="high"></picture><span class="h-sweep" aria-hidden="true"></span><span class="h-label">Illustrative scene</span></div></section>
{wall_sec()}{MACHINE}{consult_sec()}{artists_sec()}{visit_sec()}'''
page('', 'The Electric Pen Tattoo Studio | Tattoo Shop in North Hollywood','Tattoo studio at 10751 Magnolia Blvd, North Hollywood. Open daily 12-8. Call (818) 506-8828 or get directions.',home,'',ld(''))
page('artists/','Tattoo Artists | The Electric Pen Tattoo Studio, North Hollywood','Owner Bo Adams and the resident artists at The Electric Pen Tattoo Studio, 10751 Magnolia Blvd, North Hollywood. Call (818) 506-8828.',
 f'<section class="phead"><h1>Artists</h1><p class="lede">The roster changes, so only names the studio confirms go up.</p></section>'+artists_sec('h2')+consult_sec(),'artists/',ld('artists/','Artists'))
page('flash/','On the Wall | The Electric Pen Tattoo Studio, North Hollywood','Custom tattoos, piercing and gallery at The Electric Pen Tattoo Studio, 10751 Magnolia Blvd, North Hollywood. Call (818) 506-8828.',
 f'<section class="phead"><h1>On the wall</h1><p class="lede">The studio\'s own flash and healed work go up here once it sends photos. Until then, call or visit to see the books.</p></section>'+wall_sec('h2').replace('<h2 class="sec-t">On the wall</h2>','<h2 class="vh">Sheets</h2>')+MACHINE,'flash/',ld('flash/','On the wall'))
page('visit/','Visit & Hours | The Electric Pen Tattoo Studio, Magnolia Blvd NoHo','The Electric Pen Tattoo Studio is at 10751 Magnolia Blvd, North Hollywood, open daily 12-8 PM. Directions, map and how a consult works.',
 f'<section class="phead"><h1>Visit</h1><p class="lede">10751 Magnolia Blvd, North Hollywood. Open daily, 12 to 8. For parking, <a href="{TEL}">call to confirm</a>.</p></section>'+visit_sec()+consult_sec(),'visit/',ld('visit/','Visit'))
nf=f'<section class="phead nf"><h1>Page not found</h1><p class="lede">This sheet fell off the wall. Head back home or call the studio.</p><div class="ctas"><a class="btn btn-y" href="{BASE}">Back home</a><a class="btn btn-o" href="{TEL}">Call {PHONE}</a></div></section>'
page('404.html','Page not found | The Electric Pen Tattoo Studio','That page is not here. Head back to The Electric Pen Tattoo Studio home page.',nf,'404',None)
s=open(os.path.join(ROOT,'404.html')).read().replace('<head>','<head><meta name="robots" content="noindex">',1); open(os.path.join(ROOT,'404.html'),'w').write(s)
open(os.path.join(ROOT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
open(os.path.join(ROOT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{p}</loc><lastmod>2026-10-22</lastmod></url>' for p in ['','artists/','flash/','visit/'])+'</urlset>\n')
print('built')
