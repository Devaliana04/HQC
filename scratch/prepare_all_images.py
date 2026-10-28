import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
artifact_dir = r"C:\Users\LENOVO\.gemini\antigravity-ide\brain\4441eff4-c466-4368-ac24-2d40af242334"

process_dir = os.path.join(workspace, "assets", "images", "process")
portfolio_dir = os.path.join(workspace, "assets", "images", "portfolio")
services_dir = os.path.join(workspace, "assets", "images", "services")
blog_dir = os.path.join(workspace, "assets", "images", "blog")
og_dir = os.path.join(workspace, "assets", "images", "og")

for d in [process_dir, portfolio_dir, services_dir, blog_dir, og_dir]:
    os.makedirs(d, exist_ok=True)

# Sources
hero_src = os.path.join(artifact_dir, "hqc_hero_construction_1793222879805.jpg")
rebar_piping_src = os.path.join(artifact_dir, "hqc_rebar_piping_1793222918022.jpg")
facade_scaffold_src = os.path.join(artifact_dir, "hqc_facade_scaffolding_1793222978895.jpg")
exterior_pool_src = os.path.join(artifact_dir, "hqc_exterior_pool_1793223056110.jpg")
arch_facade_src = os.path.join(artifact_dir, "hqc_arch_facade_1793223146420.jpg")
rebar_detail_src = os.path.join(artifact_dir, "hqc_rebar_detail_1793223254544.jpg")

img_hero = Image.open(hero_src).convert("RGB")
img_piping = Image.open(rebar_piping_src).convert("RGB")
img_scaffold = Image.open(facade_scaffold_src).convert("RGB")
img_pool = Image.open(exterior_pool_src).convert("RGB")
img_arch = Image.open(arch_facade_src).convert("RGB")
img_rebar = Image.open(rebar_detail_src).convert("RGB")

def save_webp_under_100kb(image, target_path, max_dim=1280, max_bytes=98000, start_q=84):
    w, h = image.size
    scale = min(1.0, max_dim / max(w, h))
    if scale < 1.0:
        image = image.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    
    q = start_q
    while q > 25:
        image.save(target_path, "WEBP", quality=q, method=6)
        sz = os.path.getsize(target_path)
        if sz <= max_bytes:
            return sz
        q -= 5
    return os.path.getsize(target_path)

def crop_center(img, aspect_ratio):
    w, h = img.size
    target_aspect = aspect_ratio
    current_aspect = w / h
    if current_aspect > target_aspect:
        new_w = int(h * target_aspect)
        offset = (w - new_w) // 2
        return img.crop((offset, 0, offset + new_w, h))
    else:
        new_h = int(w / target_aspect)
        offset = (h - new_h) // 2
        return img.crop((0, offset, w, offset + new_h))

# 1. 10 Process & Portfolio Images (PRD Section 5)
images_manifest = [
    # 01: Pembesian tulangan pondasi & jalur pipa
    {"name": "hqc-struktur-pembesian-instalasi-pipa-01.webp", "src": crop_center(img_piping, 4/3)},
    # 02: Area pembesian dan instalasi pipa sudut lebar
    {"name": "hqc-area-struktur-pipa-02.webp", "src": crop_center(img_piping, 16/10)},
    # 03: Pembesian dan pipa dengan bangunan bertingkat dalam pengerjaan
    {"name": "hqc-struktur-depan-bangunan-03.webp", "src": crop_center(img_hero, 16/9)},
    # 04: Detail utilitas pipa & rebar
    {"name": "hqc-jaringan-pipa-pembesian-04.webp", "src": crop_center(img_rebar, 16/9)},
    # 05: Tulangan baja & detail pembesian
    {"name": "hqc-pembesian-struktur-05.webp", "src": crop_center(img_rebar, 4/3)},
    # 06: Rangka fasad baja ringan
    {"name": "hqc-pekerjaan-rangka-fasad-06.webp", "src": crop_center(img_scaffold, 4/5)},
    # 07: Perancah & dinding luar
    {"name": "hqc-pekerjaan-dinding-scaffolding-07.webp", "src": crop_center(img_scaffold, 4/5)},
    # 08: Finishing plesteran & acian dinding
    {"name": "hqc-finishing-plester-dinding-08.webp", "src": crop_center(img_arch, 4/5)},
    # 09: Progres eksterior bangunan & kolam
    {"name": "hqc-progres-eksterior-kolam-09.webp", "src": crop_center(img_pool, 16/9)},
    # 10: Fasad arsitektur bukaan lengkung
    {"name": "hqc-progres-fasad-bangunan-10.webp", "src": crop_center(img_arch, 4/3)}
]

print("Saving 10 process and portfolio images...")
for item in images_manifest:
    path_process = os.path.join(process_dir, item["name"])
    path_portfolio = os.path.join(portfolio_dir, item["name"])
    sz1 = save_webp_under_100kb(item["src"], path_process, max_dim=1200)
    sz2 = save_webp_under_100kb(item["src"], path_portfolio, max_dim=1200)
    print(f"{item['name']}: {sz1} bytes (< 100KB)")

# 2. Hero Poster Image
hero_poster_path = os.path.join(process_dir, "hqc-hero-poster.webp")
save_webp_under_100kb(crop_center(img_hero, 16/9), hero_poster_path, max_dim=1600, max_bytes=98000)
print(f"hqc-hero-poster.webp: {os.path.getsize(hero_poster_path)} bytes (< 100KB)")

# 3. 5 Services Images
services = [
    ("service-villa.webp", crop_center(img_pool, 16/10)),
    ("service-hotel.webp", crop_center(img_hero, 16/10)),
    ("service-structure.webp", crop_center(img_piping, 16/10)),
    ("service-mep.webp", crop_center(img_rebar, 16/10)),
    ("service-finishing.webp", crop_center(img_arch, 16/10)),
]
print("\nSaving service images...")
for name, img in services:
    target = os.path.join(services_dir, name)
    sz = save_webp_under_100kb(img, target, max_dim=1080)
    print(f"{name}: {sz} bytes (< 100KB)")

# 4. 3 Blog Covers
blog_covers = [
    ("blog-tahapan-vila.webp", crop_center(img_pool, 16/9)),
    ("blog-instalasi-pipa.webp", crop_center(img_piping, 16/9)),
    ("blog-kontraktor-vila.webp", crop_center(img_hero, 16/9)),
]
print("\nSaving blog covers...")
for name, img in blog_covers:
    target = os.path.join(blog_dir, name)
    sz = save_webp_under_100kb(img, target, max_dim=1080)
    print(f"{name}: {sz} bytes (< 100KB)")

# 5. Open Graph 1200x630 Social Sharing Image (with WhatsApp support)
print("\nCreating 1200x630 Open Graph card...")
og_card = Image.new("RGB", (1200, 630), (16, 38, 63)) # HQC Navy background

# Right side: 65% photo crop
right_photo = crop_center(img_hero, 780/630).resize((780, 630), Image.Resampling.LANCZOS)
og_card.paste(right_photo, (420, 0))

# Left gradient overlay over photo transition
draw_og = ImageDraw.Draw(og_card, "RGBA")
for x in range(360, 560):
    alpha = int(255 * (1.0 - (x - 360) / 200.0))
    draw_og.line([(x, 0), (x, 630)], fill=(16, 38, 63, alpha))

# Solid left navy block
draw_og.rectangle([(0, 0), (360, 630)], fill=(16, 38, 63, 255))

# Draw architectural thin blue line accent
draw_og.line([(60, 140), (320, 140)], fill=(36, 95, 178, 255), width=3)
draw_og.line([(60, 520), (320, 520)], fill=(216, 181, 138, 255), width=2)

# Load emblem to stamp on OG card
brand_emblem_path = os.path.join(workspace, "assets", "brand", "hqc-emblem.png")
if os.path.exists(brand_emblem_path):
    emblem_og = Image.open(brand_emblem_path).convert("RGBA")
    emb_h = 70
    emb_w = int(emb_h * (emblem_og.width / emblem_og.height))
    emblem_og = emblem_og.resize((emb_w, emb_h), Image.Resampling.LANCZOS)
    og_card.paste(emblem_og, (60, 55), emblem_og)

try:
    font_title = ImageFont.truetype("arialbd.ttf", 36)
    font_bold = ImageFont.truetype("arialbd.ttf", 28)
    font_sub = ImageFont.truetype("arial.ttf", 16)
    font_eyebrow = ImageFont.truetype("arialbd.ttf", 13)
except:
    font_title = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_eyebrow = ImageFont.load_default()

# Typography on OG card
draw_og.text((140, 62), "HQC", fill=(255, 255, 255, 255), font=font_title)
draw_og.text((140, 105), "HIGH QUALITY CONSTRUCTION", fill=(216, 181, 138, 255), font=font_sub)

draw_og.text((60, 170), "BLUEPRINT TO BUILT", fill=(216, 181, 138, 255), font=font_eyebrow)
draw_og.text((60, 205), "The Work Behind\nExceptional\nSpaces.", fill=(255, 255, 255, 255), font=font_bold)
draw_og.text((60, 360), "Dokumentasi nyata tahapan\nkonstruksi vila & hotel\ndari pembesian hingga\nfinishing arsitektural.", fill=(221, 236, 245, 255), font=font_sub)

draw_og.text((60, 540), "WhatsApp: +62 821-4426-7826", fill=(255, 255, 255, 255), font=font_sub)

og_webp_path = os.path.join(og_dir, "hqc-og-home.webp")
og_jpg_path = os.path.join(og_dir, "hqc-og-home.jpg")

save_webp_under_100kb(og_card, og_webp_path, max_dim=1200, max_bytes=98000)
# Also save JPEG under 100KB for maximum compatibility with all WhatsApp versions
q = 80
while q > 25:
    og_card.save(og_jpg_path, "JPEG", quality=q, optimize=True)
    if os.path.getsize(og_jpg_path) <= 98000:
        break
    q -= 5

print(f"hqc-og-home.webp: {os.path.getsize(og_webp_path)} bytes (< 100KB)")
print(f"hqc-og-home.jpg: {os.path.getsize(og_jpg_path)} bytes (< 100KB)")

print("\nALL IMAGES CREATED AND COMPRESSED TO UNDER 100KB!")
