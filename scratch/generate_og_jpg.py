import os
from PIL import Image

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
og_webp_path = os.path.join(workspace, "assets", "images", "og", "hqc-og-home.webp")
og_jpg_path = os.path.join(workspace, "assets", "images", "og", "hqc-og-home.jpg")
root_og_jpg = os.path.join(workspace, "hqc-og-home.jpg")

im = Image.open(og_webp_path).convert("RGB")
# Save with progressive JPEG and optimize for WhatsApp (needs crisp, clean image < 100KB)
quality = 88
while quality > 40:
    im.save(og_jpg_path, format="JPEG", quality=quality, optimize=True, progressive=True)
    size_kb = os.path.getsize(og_jpg_path) / 1024.0
    if size_kb < 98.0:
        break
    quality -= 3

# Copy to root as well
im.save(root_og_jpg, format="JPEG", quality=quality, optimize=True, progressive=True)

size_kb = os.path.getsize(og_jpg_path) / 1024.0
print(f"Generated OG JPEG: {og_jpg_path} ({size_kb:.2f} KB, quality={quality})")
