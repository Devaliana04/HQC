import os
from PIL import Image, ImageDraw, ImageFont

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
brand_dir = os.path.join(workspace, "assets", "brand")
os.makedirs(brand_dir, exist_ok=True)

source_logo_path = os.path.join(workspace, "assets", "brand_inspect", "image.png_20261026021835.jpg")

# Open source logo image
img = Image.open(source_logo_path).convert("RGBA")
width, height = img.size

# Process transparency: make white background transparent
data = img.getdata()
new_data = []

# The background is white (r>235, g>235, b>235)
for item in data:
    r, g, b, a = item
    if r > 240 and g > 240 and b > 240:
        # Transparent
        new_data.append((255, 255, 255, 0))
    elif r > 215 and g > 215 and b > 215:
        # Anti-aliasing edge blend
        alpha = int(255 - ((min(r, g, b) - 215) / 25.0) * 255)
        new_data.append((r, g, b, max(0, min(255, alpha))))
    else:
        new_data.append((r, g, b, 255))

img.putdata(new_data)

# Crop tight bounding box
bbox = img.getbbox()
if bbox:
    emblem = img.crop(bbox)
else:
    emblem = img

# Resize emblem to a clean standard master height of 512px
aspect = emblem.width / emblem.height
emblem_master = emblem.resize((int(512 * aspect), 512), Image.Resampling.LANCZOS)
emblem_master.save(os.path.join(brand_dir, "hqc-emblem.webp"), format="WEBP", quality=95)
emblem_master.save(os.path.join(brand_dir, "hqc-emblem.png"), format="PNG")

# Generate Favicons
fav48 = emblem_master.resize((48, 48), Image.Resampling.LANCZOS)
fav48.save(os.path.join(brand_dir, "favicon-48.png"), format="PNG")

# Favicon.ico
fav_icon_img = emblem_master.resize((32, 32), Image.Resampling.LANCZOS)
# Put on slight navy background for crisp visibility on all browser tabs
fav_navy = Image.new("RGBA", (32, 32), (16, 38, 63, 255))
# draw circular mask or rounded rectangle
mask = Image.new("L", (32, 32), 0)
d = ImageDraw.Draw(mask)
d.rounded_rectangle([(0, 0), (31, 31)], radius=6, fill=255)
fav_navy.putalpha(mask)

emb_small = emblem_master.resize((24, int(24 / aspect)), Image.Resampling.LANCZOS)
# center emblem
x_offset = (32 - emb_small.width) // 2
y_offset = (32 - emb_small.height) // 2
fav_navy.paste(emb_small, (x_offset, y_offset), emb_small)
fav_navy.save(os.path.join(workspace, "favicon.ico"), format="ICO")

# Apple touch icon (180x180)
apple_touch = Image.new("RGBA", (180, 180), (16, 38, 63, 255))
emb_120 = emblem_master.resize((int(120 * aspect), 120), Image.Resampling.LANCZOS)
x_off = (180 - emb_120.width) // 2
y_off = (180 - emb_120.height) // 2
apple_touch.paste(emb_120, (x_off, y_off), emb_120)
apple_touch.save(os.path.join(brand_dir, "apple-touch-icon.png"), format="PNG")

# Now generate full horizontal logo brand assets:
# 1) Light version (for dark navy headers): Gold emblem + White "HQC" + Sand "HIGH QUALITY CONSTRUCTION"
logo_h = 100
emb_h = 80
emb_w = int(emb_h * aspect)
logo_light = Image.new("RGBA", (480, logo_h), (0, 0, 0, 0))
emb_resized = emblem_master.resize((emb_w, emb_h), Image.Resampling.LANCZOS)
logo_light.paste(emb_resized, (10, 10), emb_resized)

draw = ImageDraw.Draw(logo_light)
# Try system fonts or default
try:
    font_bold = ImageFont.truetype("arialbd.ttf", 42)
    font_sub = ImageFont.truetype("arial.ttf", 15)
except:
    font_bold = ImageFont.load_default()
    font_sub = ImageFont.load_default()

text_x = emb_w + 30
draw.text((text_x, 15), "HQC", fill=(255, 255, 255, 255), font=font_bold)
draw.text((text_x, 62), "HIGH QUALITY CONSTRUCTION", fill=(216, 181, 138, 255), font=font_sub)

logo_light.save(os.path.join(brand_dir, "hqc-logo-light.webp"), format="WEBP", quality=95)
logo_light.save(os.path.join(brand_dir, "hqc-logo-light.png"), format="PNG")

# 2) Dark version (for white/light backgrounds): Gold emblem + Navy "HQC" + Navy Slate subtext
logo_dark = Image.new("RGBA", (480, logo_h), (0, 0, 0, 0))
logo_dark.paste(emb_resized, (10, 10), emb_resized)
draw_dark = ImageDraw.Draw(logo_dark)
draw_dark.text((text_x, 15), "HQC", fill=(16, 38, 63, 255), font=font_bold)
draw_dark.text((text_x, 62), "HIGH QUALITY CONSTRUCTION", fill=(36, 95, 178, 255), font=font_sub)

logo_dark.save(os.path.join(brand_dir, "hqc-logo-dark.webp"), format="WEBP", quality=95)
logo_dark.save(os.path.join(brand_dir, "hqc-logo-dark.png"), format="PNG")
logo_dark.save(os.path.join(brand_dir, "hqc-logo.webp"), format="WEBP", quality=95)

print("Brand assets created successfully!")
for f in os.listdir(brand_dir):
    p = os.path.join(brand_dir, f)
    print(f, os.path.getsize(p), "bytes")
