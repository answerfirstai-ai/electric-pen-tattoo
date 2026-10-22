import json,os,sys,html
sys.path.insert(0,os.path.dirname(__file__))
from art import sprite,use,ART
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE='/electric-pen-tattoo/'; SITE='https://answerfirstai-ai.github.io'+BASE
NAME='The Electric Pen Tattoo Studio'; PHONE='(818) 506-8828'; TEL='tel:+18185068828'
IG='https://www.instagram.com/theelectricpentattoo/'
DIR='https://www.google.com/maps/search/?api=1&query=The+Electric+Pen+Tattoo+Studio+10751+Magnolia+Blvd+North+Hollywood+CA+91601'
YELP='https://www.yelp.com/biz/the-electric-pen-tattoo-studio-north-hollywood'
TDO='https://www.tattoodo.com/studios/ELECTRIC_PEN_TATTOO/'
V='5'
def need(t): return f'<span class="need">[NEED: {t}]</span>'
G=json.load(open(os.path.join(os.path.dirname(__file__),'glyphs.json')))

def lettering():
    W=700
    rows=[('the',176,'g'),('electric',318,'r'),('pen',478,'y')]
    out=[];fills={'g':[],'r':[],'y':[]};shadow=[];defs=[];n=0
    for key,base,col in rows:
        paths,w=G[key]; x=(W-w)/2
        for d in paths:
            if not d: continue
            t=f'translate({x:.1f} {base})'
            defs.append(f'<path id="gl{n}" d="{d}" transform="{t}"/>')
            fills[col].append(f'<use href="#gl{n}"/>')
            shadow.append(f'<use href="#gl{n}" x="6" y="6"/>')
            out.append(f'<path class="ln" d="{d}" transform="{t}"/>'); n+=1
    ribbon=('<g class="ribbon">'
      '<path class="ln rb" d="M120 58 L580 58 L560 84 L580 110 L120 110 L140 84 Z" />'
      '<path class="ln rb" d="M150 48 Q350 30 550 48 L550 96 Q350 78 150 96 Z"/>'
      '<text x="350" y="80" text-anchor="middle" class="rbt">Tattooing NoHo since 2005</text></g>')
    bottom=('<g class="ribbon">'
      '<path class="ln rb" d="M140 506 Q350 492 560 506 L560 546 Q350 532 140 546 Z"/>'
      '<text x="350" y="530" text-anchor="middle" class="rbt rbs">Magnolia Blvd · North Hollywood</text></g>')
    stars=''.join(f'<path class="ln st" d="M{x} {y} l6 14 l15 2 l-11 10 l3 15 l-13 -8 l-13 8 l3 -15 l-11 -10 l15 -2 z"/>' for x,y in [(200,146),(500,146)])
    bolts=('<path class="ln bolt" d="M112 410 L140 360 L132 396 L158 390 L124 458 L134 414 Z"/>'
           '<path class="ln bolt" d="M588 410 L560 360 L568 396 L542 390 L576 458 L566 414 Z"/>')
    return (f'<svg class="lettering" viewBox="0 0 700 560" role="img" aria-labelledby="lt"><title id="lt">{NAME}</title>'
      '<defs>'+''.join(defs)+'<pattern id="ht" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="3.5" cy="3.5" r="1.6" fill="#121212"/></pattern></defs>'
      f'<g class="shadow" fill="#121212">{"".join(shadow)}</g>'
      f'<g class="fill fill-g" fill="#2E7D4F">{"".join(fills["g"])}</g>'
      f'<g class="fill fill-r" fill="#C42021">{"".join(fills["r"])}</g>'
      f'<g class="fill fill-y" fill="#F2B705">{"".join(fills["y"])}</g>'
      f'<g class="halftone" fill="url(#ht)" opacity=".28">{"".join(fills["r"])}</g>'
      f'<g class="outline">{ribbon}{bottom}{stars}{bolts}{"".join(out)}</g>'
      '<circle class="tip" r="5" cx="-20" cy="-20"/></svg>')

NAV=[('Artists','artists/'),('Flash','flash/'),('Visit','visit/')]
def head(title,desc,path,extra=''):
    url=SITE+path
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta name="theme-color" content="#1B231F"><meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}favicon.svg" type="image/svg+xml"><link rel="icon" href="{BASE}favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="{BASE}assets/img/icon-180.png"><link rel="manifest" href="{BASE}site.webmanifest">
<link rel="preload" href="{BASE}assets/fonts/archivo-narrow.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{BASE}assets/css/site.css?v={V}">
<script>document.documentElement.classList.add('js')</script>{extra}</head>'''
def header(cur):
    links=''.join(f'<a class="wl" href="{BASE}{h}"{" aria-current=page" if cur==h else ""}>{t}</a>' for t,h in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a><header class="nav"><a class="mark" href="{BASE}" aria-label="{NAME}, home">{use("boltpen","mk")}<span>The Electric Pen</span></a>
<nav aria-label="Main">{links}</nav><a class="btn btn-y nav-call" href="{TEL}">Call {PHONE}</a><i class="buzz" aria-hidden="true"></i></header>'''
def ctas(cls=''): return f'<div class="ctas {cls}"><a class="btn btn-y" href="{TEL}">Call {PHONE}</a><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Directions</a><a class="btn btn-o" href="{IG}" target="_blank" rel="noopener">Instagram</a></div>'
def footer():
    return f'''<footer class="foot"><div class="fwrap"><div><p class="fname">{NAME}</p><p>10751 Magnolia Blvd, North Hollywood, CA 91601</p>
<p><a class="wl" href="{TEL}">{PHONE}</a></p><p>Tattooing · Piercing · Since 2005</p></div>
<div><p class="flab">Find us elsewhere</p><p><a class="wl" href="{IG}" target="_blank" rel="noopener">Instagram</a> · <a class="wl" href="{YELP}" target="_blank" rel="noopener">Yelp</a> · <a class="wl" href="{TDO}" target="_blank" rel="noopener">Tattoodo</a></p>
<p class="fnote">Flash art on this site is original illustration made for the site, not the studio's tattoo work.</p></div></div></footer>
<div class="mbar"><a class="btn btn-y" href="{TEL}">Call</a><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Directions</a></div>'''
SCRIPTS=f'<script src="{BASE}assets/js/gsap.min.js" defer></script><script src="{BASE}assets/js/ScrollTrigger.min.js" defer></script><script src="{BASE}assets/js/site.js?v={V}" defer></script>'
def page(path,title,desc,body,cur='',ld=None,art=()):
    ldj=f'<script type="application/ld+json">{json.dumps(ld,separators=(",",":"))}</script>' if ld else ''
    h=head(title,desc,path,ldj)+f'<body class="p-{cur.strip("/") or "home"}">'+sprite(list(art) or ['boltpen'] ).replace('</svg>','<filter id="wet"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.03" numOctaves="2" seed="3"><animate attributeName="baseFrequency" dur="2.4s" values="0.012 0.03;0.02 0.05;0.012 0.03" repeatCount="indefinite"/></feTurbulence><feDisplacementMap in="SourceGraphic" scale="9"/></filter></svg>')+header(cur)+f'<main id="main">{body}</main>'+footer()+SCRIPTS+'</body></html>'
    fp=os.path.join(ROOT,path,'index.html') if not path.endswith('.html') else os.path.join(ROOT,path)
    os.makedirs(os.path.dirname(fp),exist_ok=True); open(fp,'w').write(h)

ALL=list(ART.keys())
BUSINESS={"@type":["TattooParlor","LocalBusiness"],"@id":SITE+"#studio","name":NAME,"url":SITE,"telephone":"+1-818-506-8828",
 "image":SITE+"assets/img/og.jpg","logo":SITE+"assets/img/icon-512.png","foundingDate":"2005",
 "address":{"@type":"PostalAddress","streetAddress":"10751 Magnolia Blvd","addressLocality":"North Hollywood","addressRegion":"CA","postalCode":"91601","addressCountry":"US"},
 "areaServed":"North Hollywood, CA","priceRange":"$$$","openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"12:00","closes":"20:00"}],"hasMap":DIR,"sameAs":[IG,YELP,TDO,"https://www.facebook.com/248292815342"],
 "knowsAbout":["Custom tattooing","Black and grey tattoos","Traditional tattoos","Piercing","Art gallery"],
 "amenityFeature":[{"@type":"LocationFeatureSpecification","name":n,"value":True} for n in ["Walk-ins welcome","Wheelchair accessible entrance","Wifi"]]}
def ld(path,crumb=None):
    g=[dict(BUSINESS,**{"@context":"https://schema.org"})] if not crumb else [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE},{"@type":"ListItem","position":2,"name":crumb,"item":SITE+path}]},{"@context":"https://schema.org","@id":SITE+"#studio","@type":["TattooParlor","LocalBusiness"],"name":NAME,"telephone":"+1-818-506-8828","url":SITE}]
    return g if len(g)>1 else g[0]

ARTISTS=[('Bo Adams','Owner. Custom, creative tattooing for 20+ years.','skull'),
 ("Angel “Mr. Monster”","Tattoo artist. Client reviews mention traditional, realism, portraits and color/watercolor work.",'eye'),
('Hanna','Piercer.','star')]
FLASH=[('rose','Rose'),('swallow','Swallow'),('dagger','Dagger'),('heart','Heart & banner'),('anchor','Anchor'),('moon','Moon & stars'),('flame','Flame'),('web','Spiderweb'),('eye','All-seeing eye'),('star','Nautical star'),('skull','Skull'),('boltpen','Lightning pen')]
HOURS='Open daily, 12 PM to 8 PM. Walk-ins welcome.'

def sheet(a,label,i,cls='ws'):
    return f'<div class="{cls}" style="--r:{(i*37%9)-4}deg"><i class="tape"></i>{use(a)}<span>{label}</span></div>'
def wall():
    return ''.join(sheet(a,l,i) for i,(a,l) in enumerate(FLASH[:14]))
def artist_cards(link=True):
    out=''
    for i,(n,r,a) in enumerate(ARTISTS):
        out+=f'''<article class="acard" style="--r:{[-2,1.5,2][i]}deg"><i class="tape"></i><div class="aport">{use(a)}<span class="need">[NEED: real photo of {html.escape(n.split(" ")[0])}]</span></div>
<h3>{n}</h3><p>{r}</p><p class="small">{need("styles in their own words + portfolio link")}</p><a class="btn btn-o btn-sm" href="{TEL}">Call to book with {html.escape(n.split(" ")[0].replace("“",""))}</a></article>'''
    return out
def flash_grid(n=12):
    return ''.join(f'<figure class="fl" style="--r:{(i*53%7)-3}deg">{use(a)}<figcaption>{l}<small>Original illustration</small></figcaption></figure>' for i,(a,l) in enumerate(FLASH[:n]))
STEPS=[('Call or walk in','Call '+PHONE+' or come by. Walk-ins welcome, daily 12 to 8.','M30 20 h40 v60 h-40 z M42 70 h16'),
 ('Talk it through','Bring your idea or pick something off the wall. Every piece is priced by quote.','M20 30 h60 v35 h-35 l-15 12 v-12 h-10 z'),
 ('Lock in the design',need('deposit + booking policy'),'M50 15 l10 25 l27 3 l-20 18 l6 27 l-23 -14 l-23 14 l6 -27 l-20 -18 l27 -3 z'),
 ('Get tattooed',need('ID/age policy wording'),'M20 80 L70 30 L80 40 L30 90 Z M70 30 L85 15'),
 ('Heal it right',need("the studio's aftercare instructions"),'M50 15 C80 40 85 60 70 80 C60 92 40 92 30 80 C15 60 20 40 50 15 Z')]
def steps():
    return ''.join(f'<li class="step"><svg viewBox="0 0 100 100" aria-hidden="true"><path class="sp" d="{d}"/></svg><div><h3><span class="n">{i+1}</span>{t}</h3><p>{p}</p></div></li>' for i,(t,p,d) in enumerate(STEPS))

home=f'''<section class="hero" id="hero"><div class="wall" aria-hidden="true">{wall()}</div>
<div class="sheet" id="sheet"><div class="sheet-in"><i class="tape t1"></i><i class="tape t2"></i><i class="tape t3"></i><i class="tape t4"></i>
<h1 class="vh">{NAME}, tattoos on Magnolia Blvd, North Hollywood</h1>{lettering()}</div></div>
<div class="hero-copy"><p class="lede">Tattoos on Magnolia Blvd, North Hollywood. Pick it off the wall or bring your own idea.</p>{ctas("hc")}</div>
<a class="sticker" href="https://www.google.com/maps/place/?q=place_id:ChIJc7k_jYuVwoAR5XyQL_-abcU" target="_blank" rel="noopener"><b>4.7★</b><span>Google · 94 reviews</span></a>
<p class="scrollcue" aria-hidden="true">Scroll to see the wall</p></section>
<section class="about wrap"><div class="ab-l"><p class="ribbon-h"><span>Since 2005</span></p><h2>Twenty years on the same block of the Arts District.</h2></div>
<div class="ab-r"><blockquote class="owner"><p>“We specialize in Custom Tattooing, Black and Grey, and Traditional Artistry. We have a team of excellent artists with over 20+ years of tattooing.”</p><cite>The studio, on its Yelp page</cite></blockquote>
<ul class="tags"><li>Custom</li><li>Black &amp; grey</li><li>Traditional</li><li>Piercing</li><li>Art gallery</li></ul></div></section>
<section class="styles"><div class="wrap"><h2 class="banner-h"><span>Pick your lane</span></h2><div class="sgrid">
<article class="scard"><h3>Custom</h3><p>Your idea, drawn up for you. Bring references, a story, a placement.</p></article>
<article class="scard sc2"><h3>Black &amp; grey</h3><p>Smooth shading and soft contrast, no color needed.</p></article>
<article class="scard sc3"><h3>Traditional</h3><p>Bold lines, solid color, the classic flash look this site is built around.</p></article>
<article class="scard sc4"><h3>Piercing</h3><p>Piercing is on the menu too. Hanna is the studio's piercer. The studio also runs an art gallery. {need("gallery + piercing details")}</p></article></div></div></section>
<section class="artists wrap"><h2 class="banner-h"><span>The artists</span></h2><p class="sub">From the studio's listings. {need("confirm current roster")}</p><div class="agrid">{artist_cards()}</div></section>
<section class="flash dark"><div class="wrap"><h2 class="banner-h"><span>Off the wall</span></h2><p class="sub">These sheets are original flash-style illustrations made for this site. They are not the studio's tattoo work. {need("the studio's own flash + healed work photos, with artist credit")}</p>
<div class="fgrid">{flash_grid(8)}</div><p class="more"><a class="btn btn-o" href="{BASE}flash/">See the whole wall</a></p></div></section>
<section class="booking" id="booking"><div class="wrap bk"><div class="bk-l"><h2 class="banner-h"><span>How it goes</span></h2><p class="sub">First tattoo? Good. Ask us everything.</p>{ctas()}</div><ol class="steps">{steps()}</ol></div></section>
<section class="visit wrap"><h2 class="banner-h"><span>Come by</span></h2><div class="vgrid">
<div class="vcard"><h3>Where</h3><p>10751 Magnolia Blvd, North Hollywood, CA 91601. NoHo Arts District.</p><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Directions</a></div>
<div class="vcard"><h3>When</h3><p>{HOURS}</p><a class="btn btn-y" href="{TEL}">Call {PHONE}</a></div>
<div class="vcard"><h3>Good to know</h3><ul class="amen"><li>Walk-ins welcome</li><li>Wheelchair-accessible entrance</li><li>Accessible parking near the entrance</li><li>LGBTQ friendly</li><li>Wifi</li></ul><p class="small">Per the studio's Yelp and Tattoodo listings.</p></div></div></section>'''
page('', 'The Electric Pen Tattoo Studio | Tattoo Shop in North Hollywood','Custom, black and grey, and traditional tattoos plus piercing at 10751 Magnolia Blvd, North Hollywood, since 2005. Walk-ins welcome daily 12-8. Rated 4.7 on Google.',home,'',ld(''),ALL)

art_body=f'''<section class="phead wrap"><h1 class="banner-h"><span>The artists</span></h1><p class="lede">The people behind the needles at The Electric Pen, as named on the studio's listings. {need("confirm current roster with the shop")}</p></section>
<section class="wrap"><div class="agrid">{artist_cards()}</div></section><section class="wrap cta-band"><h2>Not sure who fits your idea?</h2><p>Call and describe it. The studio will point you to the right artist.</p>{ctas()}</section>'''
page('artists/','Tattoo Artists | The Electric Pen Tattoo Studio, North Hollywood','Meet the artists and piercer at The Electric Pen Tattoo Studio in North Hollywood: owner Bo Adams, Angel “Mr. Monster” and piercer Hanna.',art_body,'artists/',ld('artists/','Artists'),[a for _,_,a in ARTISTS])
fl_body=f'''<section class="phead wrap"><h1 class="banner-h"><span>The flash wall</span></h1><p class="lede">Traditional flash, the way it hangs in a shop. Every sheet here is an original illustration drawn for this website. None of it is the studio's tattoo work. {need("the studio's own flash sheets + healed work photos, with artist credit")}</p></section>
<section class="dark"><div class="wrap"><div class="fgrid">{flash_grid()}</div></div></section><section class="wrap cta-band"><h2>See something close?</h2><p>Call the studio and talk it through. They do custom work too.</p>{ctas()}</section>'''
page('flash/','Flash Wall | The Electric Pen Tattoo Studio, North Hollywood','Traditional flash-style art and custom tattoo ideas at The Electric Pen Tattoo Studio on Magnolia Blvd, North Hollywood. Call (818) 506-8828.',fl_body,'flash/',ld('flash/','Flash'),ALL)
vi_body=f'''<section class="phead wrap"><h1 class="banner-h"><span>Visit the studio</span></h1><p class="lede">Magnolia Blvd in the NoHo Arts District, North Hollywood.</p></section>
<section class="visit wrap"><div class="vgrid">
<div class="vcard"><h2>Address</h2><p>10751 Magnolia Blvd<br>North Hollywood, CA 91601</p><a class="btn btn-o" href="{DIR}" target="_blank" rel="noopener">Open in Google Maps</a></div>
<div class="vcard"><h2>Hours</h2><p>{HOURS}</p><a class="btn btn-y" href="{TEL}">Call {PHONE}</a></div>
<div class="vcard"><h2>Before you come</h2><ul class="amen"><li>Walk-ins welcome</li><li>Wheelchair-accessible entrance</li><li>Accessible parking near the entrance</li><li>Wifi</li></ul><p>{need("parking details")} {need("ID/age policy")} Every piece is priced by quote.</p></div></div></section>
<section class="booking"><div class="wrap bk"><div class="bk-l"><h2 class="banner-h"><span>How it goes</span></h2>{ctas()}</div><ol class="steps">{steps()}</ol></div></section>'''
page('visit/','Visit & Hours | The Electric Pen Tattoo Studio, Magnolia Blvd NoHo','Find The Electric Pen Tattoo Studio at 10751 Magnolia Blvd in the NoHo Arts District, North Hollywood. Directions, hours and how booking works. Call (818) 506-8828.',vi_body,'visit/',ld('visit/','Visit'),['star','heart','skull'])
nf=f'<section class="phead wrap nf">{use("skull","nfart")}<h1 class="banner-h"><span>Blown out</span></h1><p class="lede">This page isn\'t on the wall. Head back home or call the studio.</p><p class="ctas"><a class="btn btn-y" href="{BASE}">Back to the wall</a><a class="btn btn-o" href="{TEL}">Call {PHONE}</a></p></section>'
page('404.html','Page not found | The Electric Pen Tattoo Studio','That page is not on the wall. Head back to The Electric Pen Tattoo Studio home page.',nf,'404',None,['skull'])
s=open(os.path.join(ROOT,'404.html')).read().replace('<head>','<head><meta name="robots" content="noindex">',1); open(os.path.join(ROOT,'404.html'),'w').write(s)
open(os.path.join(ROOT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
open(os.path.join(ROOT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{p}</loc><lastmod>2026-10-22</lastmod></url>' for p in ['','artists/','flash/','visit/'])+'</urlset>\n')
open(os.path.join(ROOT,'site.webmanifest'),'w').write(json.dumps({"name":NAME,"short_name":"Electric Pen","start_url":BASE,"display":"standalone","background_color":"#1B231F","theme_color":"#1B231F","icons":[{"src":BASE+"assets/img/icon-192.png","sizes":"192x192","type":"image/png"},{"src":BASE+"assets/img/icon-512.png","sizes":"512x512","type":"image/png"}]}))
open(os.path.join(ROOT,'.nojekyll'),'w').write('')
print('built')
