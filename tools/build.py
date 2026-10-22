import json,os,sys,html
sys.path.insert(0,os.path.dirname(__file__))
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE='/electric-pen-tattoo/'; SITE='https://answerfirstai-ai.github.io'+BASE
NAME='The Electric Pen Tattoo Studio'; PHONE='(818) 506-8828'; TEL='tel:+18185068828'
IG='https://www.instagram.com/theelectricpentattoo/'
DIR='https://www.google.com/maps/search/?api=1&query=The+Electric+Pen+Tattoo+Studio+10751+Magnolia+Blvd+North+Hollywood+CA+91601'
YELP='https://www.yelp.com/biz/the-electric-pen-tattoo-studio-north-hollywood'
TDO='https://www.tattoodo.com/studios/ELECTRIC_PEN_TATTOO/'
V='13'
def need(t): return f'<span class="need">[NEED: {t}]</span>'
NAV=[('Work','flash/'),('Artists','artists/'),('Visit','visit/')]
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
def footer():
    return f'''<footer class="foot"><div class="fwrap"><div><p class="fname">{NAME}</p><p>10751 Magnolia Blvd, North Hollywood, CA 91601</p>
<p><a class="wl" href="{TEL}">{PHONE}</a></p><p>Open daily, 12 PM to 8 PM</p></div><nav class="fnav" aria-label="Footer"><p class="flab">Pages</p><a class="wl" href="{BASE}">Home</a><a class="wl" href="{BASE}artists/">Artists</a><a class="wl" href="{BASE}flash/">Work</a><a class="wl" href="{BASE}visit/">Visit</a></nav>
<div><p class="flab">Find us elsewhere</p><p><a class="wl" href="{IG}" target="_blank" rel="noopener">Instagram</a> · <a class="wl" href="{YELP}" target="_blank" rel="noopener">Yelp</a> · <a class="wl" href="{TDO}" target="_blank" rel="noopener">Tattoodo</a></p>
<p class="fnote">Images marked “Illustrative scene” are AI-generated or rendered. They are not photos of The Electric Pen, its people or its tattoo work.</p></div></div></footer>
<div class="mbar"><a class="btn btn-y" href="{TEL}">Call</a><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Directions</a></div>'''
SCRIPTS=f'<script src="{BASE}assets/js/gsap.min.js" defer></script><script src="{BASE}assets/js/ScrollTrigger.min.js" defer></script><script src="{BASE}assets/js/site.js?v={V}" defer></script>'
def page(path,title,desc,body,cur='',ld=None,art=()):
    ldj=f'<script type="application/ld+json">{json.dumps(ld,separators=(",",":"))}</script>' if ld else ''
    h=head(title,desc,path,ldj,PRE.get(path,''))+f'<body class="p-{cur.strip("/") or "home"}">'+''+header(cur)+f'<main id="main">{body}</main>'+footer()+SCRIPTS+'</body></html>'
    fp=os.path.join(ROOT,path,'index.html') if not path.endswith('.html') else os.path.join(ROOT,path)
    os.makedirs(os.path.dirname(fp),exist_ok=True); open(fp,'w').write(h)

ALL=[]
BUSINESS={"@type":["TattooParlor","LocalBusiness"],"@id":SITE+"#studio","name":NAME,"url":SITE,"telephone":"+1-818-506-8828",
 "logo":SITE+"assets/img/icon-512.png","foundingDate":"2005",
 "address":{"@type":"PostalAddress","streetAddress":"10751 Magnolia Blvd","addressLocality":"North Hollywood","addressRegion":"CA","postalCode":"91601","addressCountry":"US"},
 "areaServed":"North Hollywood, CA","geo":{"@type":"GeoCoordinates","latitude":34.1650733,"longitude":-118.3655833},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"12:00","closes":"20:00"}],"hasMap":DIR,"sameAs":[IG,YELP,TDO],
 "knowsAbout":["Tattooing"],"image":{"@type":"ImageObject","url":SITE+"assets/img/og.jpg","creditText":"Illustrative (AI-generated)"}}
def ld(path,crumb=None):
    g=[dict(BUSINESS,**{"@context":"https://schema.org"})] if not crumb else [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE},{"@type":"ListItem","position":2,"name":crumb,"item":SITE+path}]},{"@context":"https://schema.org","@id":SITE+"#studio","@type":["TattooParlor","LocalBusiness"],"name":NAME,"telephone":"+1-818-506-8828","url":SITE}]
    return g if len(g)>1 else g[0]

HOURS='Open daily, 12 PM to 8 PM.'
WALKIN='Listings say walk-ins are welcome. Call ahead to check availability.'

IMG={'wall':(1280,720,[640,1024,1280]),'stencil':(1280,720,[640,1024,1280]),'machine':(1024,1024,[480,800,1024])}
ALT={'wall':'Illustrative: a dim tattoo-shop wall covered in generic flash sheets under a tungsten bulb',
 'stencil':'Illustrative: gloved hands applying a purple rose stencil to a forearm',
 'machine':'Illustrative: a chrome and brass coil tattoo machine on black'}
LABEL='<figcaption class="illus">Illustrative scene. Not a photo of The Electric Pen.</figcaption>'
def pic(n,cls='',sizes='100vw',eager=False):
    w,h,ws=IMG[n]
    ss=lambda ext:', '.join(f'{BASE}assets/img/{n}-{x}.{ext} {x}w' for x in ws)
    load='fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<figure class="ph {cls}"><picture><source type="image/avif" srcset="{ss("avif")}" sizes="{sizes}"><source type="image/webp" srcset="{ss("webp")}" sizes="{sizes}">'
      f'<img src="{BASE}assets/img/{n}-{ws[1]}.webp" width="{w}" height="{h}" alt="{ALT[n]}" {load}></picture>{LABEL}</figure>')
PRE={}
HANDLE='@theelectricpentattoo'
ROT=[-1.2,.8,-.4,1,-.8,.5,-1,.6]
def frames(n,cls='salon'):
    sz=['t','w','s','t','s','w','t','s'][:n]
    return f'<div class="{cls}">'+''.join(f'<a class="frame f-{z}" href="{IG}" target="_blank" rel="noopener" style="--r:{ROT[i]}deg" aria-label="Portfolio slot {i+1}, on Instagram"><span class="pin" aria-hidden="true"></span><span class="fr-in"><span class="fr-n">{i+1:02d}</span><span class="need">[NEED: portfolio piece from {HANDLE}, pending permission]</span></span></a>' for i,z in enumerate(sz))+'</div>'
def bo():
    return (f'<div class="bo"><div class="frame f-p" style="--r:-.8deg"><span class="pin" aria-hidden="true"></span><span class="fr-in"><span class="need">[NEED: photo of Bo Adams, with permission]</span></span></div>'
     f'<div class="bo-tx"><h3>Bo Adams</h3><p class="role">Owner</p><p>Listed as the owner on the studio\'s Tattoodo and Yelp pages. {need("styles in his own words")}</p>'
     f'<p class="ask">Ask about our resident artists and piercer. Call and we\'ll match your idea to the right person.</p><a class="btn btn-y" href="{TEL}">Call {PHONE}</a></div></div>')
STEPS=[('Call first','Call '+PHONE+'. '+WALKIN),('Talk through the idea','Bring your idea or a reference. Every piece is priced by quote.'),
 ('Deposit and booking',need('deposit + booking policy')),('ID and age',need('ID/age policy wording')),('Aftercare',need("the studio's aftercare instructions"))]
def steps(): return '<ol class="steps">'+''.join(f'<li><span class="n">{i+1}</span><div><h3>{t}</h3><p>{p}</p></div></li>' for i,(t,p) in enumerate(STEPS))+'</ol>'
def ctas_core(): return f'<a class="btn btn-y" href="{TEL}">Call {PHONE}</a><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Directions</a>'
def booking():
    return (f'<section class="sec booking" id="booking"><div class="sheet bk-sheet" style="--r:.4deg"><span class="pin" aria-hidden="true"></span><h2>Booking &amp; walk-ins</h2>{steps()}<div class="ctas">{ctas_core()}</div></div>'
      f'<div class="bk-media">{pic("stencil","",sizes="(min-width:900px) 40vw, 100vw")}</div></section>')
MACHINE=(f'<section class="sec machine" id="machine"><div class="m-stage"><div class="m-canvas" aria-hidden="true"></div>{pic("machine","m-fallback",sizes="(min-width:900px) 50vw, 100vw")}</div>'
 '<div class="m-copy"><h2>The coil machine</h2><p>Chrome frame, brass posts, copper coils. This is a rendered model of the classic tool, not the studio\'s own equipment. Their real setup is worth seeing in person.</p></div></section>')
def visit():
    return (f'<section class="sec visit" id="visit"><div class="sheet v-sheet" style="--r:-.5deg"><span class="pin" aria-hidden="true"></span><h2>Find us on Magnolia</h2>'
     f'<p class="addr">10751 Magnolia Blvd<br>North Hollywood, CA 91601</p><p class="city">NoHo Arts District</p><div class="ctas">{ctas_core()}</div></div>'
     f'<dl class="v-facts"><div><dt>Hours</dt><dd>{HOURS}</dd></div><div><dt>Walk-ins</dt><dd>{WALKIN}</dd></div><div><dt>Pricing</dt><dd>By quote. Prices aren\'t published.</dd></div>'
     f'<div><dt>Access</dt><dd>Listings note a wheelchair-accessible entrance and accessible parking near the entrance.</dd></div><div><dt>Online</dt><dd><a class="wl" href="{IG}" target="_blank" rel="noopener">Instagram {HANDLE}</a></dd></div></dl></section>')
home=(f'<section class="hero"><div class="h-copy"><h1>The Electric Pen<span class="vh"> Tattoo Studio</span></h1>'
 f'<p class="lede">Tattoos on Magnolia Blvd, North Hollywood. Open daily 12–8. Walk-ins: call ahead.</p><div class="ctas">{ctas_core()}</div>'
 f'<p class="addr-sm">10751 Magnolia Blvd · <a class="wl" href="{TEL}">{PHONE}</a><br>Serving North Hollywood since 2005 (per the studio).</p></div>'
 f'<div class="h-media">{pic("wall","h-ph",sizes="(min-width:900px) 58vw, 100vw")}</div></section>'
 f'<section class="sec work" id="work"><div class="sec-head"><h2>Work</h2><p>Portfolio from <a class="wl" href="{IG}" target="_blank" rel="noopener">{HANDLE}</a> goes up here once the studio gives permission. Each piece will be credited to its artist.</p></div>{frames(8)}</section>'
 f'<section class="sec crew" id="artists"><div class="sec-head"><h2>Artists</h2><p>The roster changes, so only confirmed names go up. {need("current roster + consent")}</p></div>{bo()}</section>'
 +booking()+MACHINE+visit())
page('', 'The Electric Pen Tattoo Studio | Tattoo Shop in North Hollywood','Tattoos at 10751 Magnolia Blvd, North Hollywood. Open daily 12–8. Call (818) 506-8828 or get directions.',home,'',ld(''))
art_body=(f'<section class="phead"><h1>Artists</h1><p class="lede">Who\'s on the floor at The Electric Pen. The roster changes, so only names the studio confirms go up. {need("current roster + consent")}</p></section>'
 f'<section class="sec crew"><h2 class="vh">Owner</h2>{bo()}</section>'+booking())
page('artists/','Tattoo Artists | The Electric Pen Tattoo Studio, North Hollywood','Owner Bo Adams and the resident artists at The Electric Pen Tattoo Studio, 10751 Magnolia Blvd, North Hollywood. Call (818) 506-8828.',art_body,'artists/',ld('artists/','Artists'))
fl_body=(f'<section class="phead"><h1>Work</h1><p class="lede">Flash and healed work from the studio\'s artists, from <a class="wl" href="{IG}" target="_blank" rel="noopener">{HANDLE}</a>, once the studio gives permission. Every piece will be credited. Until then, call or visit to see the books.</p></section>'
 f'<section class="sec work"><h2 class="vh">Portfolio slots</h2>{frames(8)}</section>'+MACHINE)
page('flash/','Tattoo Work | The Electric Pen Tattoo Studio, North Hollywood','Tattoo work from The Electric Pen Tattoo Studio, 10751 Magnolia Blvd, North Hollywood. Portfolio coming soon. Call (818) 506-8828.',fl_body,'flash/',ld('flash/','Work'))
vi_body=(f'<section class="phead"><h1>Visit</h1><p class="lede">10751 Magnolia Blvd, North Hollywood. Open daily 12–8.</p></section>'+visit()+booking()+
 f'<section class="sec note"><p>{need("parking details")} {need("ID/age policy")}</p></section>')
page('visit/','Visit & Hours | The Electric Pen Tattoo Studio, Magnolia Blvd NoHo','The Electric Pen Tattoo Studio is at 10751 Magnolia Blvd, North Hollywood, open daily 12–8 PM. Directions, hours and how booking works.',vi_body,'visit/',ld('visit/','Visit'))
nf=f'<section class="phead nf"><h1>Page not found</h1><p class="lede">This page isn\'t here. Head back home or call the studio.</p><div class="ctas"><a class="btn btn-y" href="{BASE}">Back home</a><a class="btn btn-o" href="{TEL}">Call {PHONE}</a></div></section>'
page('404.html','Page not found | The Electric Pen Tattoo Studio','That page is not here. Head back to The Electric Pen Tattoo Studio home page.',nf,'404',None)
s=open(os.path.join(ROOT,'404.html')).read().replace('<head>','<head><meta name="robots" content="noindex">',1); open(os.path.join(ROOT,'404.html'),'w').write(s)
open(os.path.join(ROOT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
open(os.path.join(ROOT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{p}</loc><lastmod>2026-10-22</lastmod></url>' for p in ['','artists/','flash/','visit/'])+'</urlset>\n')
print('built')
