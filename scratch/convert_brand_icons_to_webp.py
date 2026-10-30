import os
import glob
from PIL import Image

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
brand_dir = os.path.join(workspace, "assets", "brand")

# Find master emblem
src_candidates = [
    os.path.join(brand_dir, "hqc-emblem.webp"),
    os.path.join(brand_dir, "hqc-emblem.png"),
    os.path.join(os.path.dirname(workspace), "image.png_20261026021835.jpg")
]

src_path = None
for c in src_candidates:
    if os.path.exists(c):
        src_path = c
        break

print(f"Master emblem source: {src_path}")
img = Image.open(src_path).convert("RGBA")
w, h = img.size
max_dim = max(w, h)

# 1. 512x512 square canvas with transparent background
square_512 = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
scale = 440 / max_dim
new_w = int(w * scale)
new_h = int(h * scale)
resized_emblem = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
offset_x = (512 - new_w) // 2
offset_y = (512 - new_h) // 2
square_512.paste(resized_emblem, (offset_x, offset_y), resized_emblem)

# 2. Apple Touch Icon 180x180 with elegant navy luxury background #10263F
apple_icon = Image.new("RGBA", (180, 180), (16, 38, 63, 255))
apple_scale = 140 / max_dim
apple_w = int(w * apple_scale)
apple_h = int(h * apple_scale)
apple_resized = img.resize((apple_w, apple_h), Image.Resampling.LANCZOS)
apple_icon.paste(apple_resized, ((180 - apple_w) // 2, (180 - apple_h) // 2), apple_resized)

# Save targets
dest_dirs = [workspace, brand_dir]

for d in dest_dirs:
    # 512x512 WebP icons
    square_512.save(os.path.join(d, "favicon.webp"), format="WEBP", quality=92, method=6)
    square_512.save(os.path.join(d, "favicon-512x512.webp"), format="WEBP", quality=92, method=6)
    square_512.save(os.path.join(d, "logo-512.webp"), format="WEBP", quality=92, method=6)

    # 180x180 Apple touch icon WebP
    apple_icon.save(os.path.join(d, "apple-touch-icon.webp"), format="WEBP", quality=92, method=6)

    # 32x32 & 16x16 WebP
    fav_32 = square_512.resize((32, 32), Image.Resampling.LANCZOS)
    fav_32.save(os.path.join(d, "favicon-32x32.webp"), format="WEBP", lossless=True)

    fav_16 = square_512.resize((16, 16), Image.Resampling.LANCZOS)
    fav_16.save(os.path.join(d, "favicon-16x16.webp"), format="WEBP", lossless=True)

# Also save 48x48 in brand_dir
fav_48 = square_512.resize((48, 48), Image.Resampling.LANCZOS)
fav_48.save(os.path.join(brand_dir, "favicon-48.webp"), format="WEBP", lossless=True)

print("WebP brand icons generated successfully.")

# Now delete all remaining PNG files from workspace
png_files = glob.glob(os.path.join(workspace, "**/*.png"), recursive=True)
png_files = [f for f in png_files if "node_modules" not in f and ".git" not in f]
print(f"\nDeleting {len(png_files)} PNG files:")
for p in png_files:
    os.remove(p)
    print(f"  Deleted: {os.path.relpath(p, workspace)}")

# Delete the 1 remaining JPG file
og_jpg = os.path.join(workspace, "assets", "images", "og", "hqc-og-home.jpg")
if os.path.exists(og_jpg):
    os.remove(og_jpg)
    print(f"  Deleted: {os.path.relpath(og_jpg, workspace)}")

print("\nAll non-WebP images (except favicon.ico) deleted.")
