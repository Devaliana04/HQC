import os
from PIL import Image

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
images_dir = os.path.join(workspace, "assets", "images")

MAX_BYTES = 95 * 1024 # 97,280 bytes (safely below 100KB)

all_files = []
for root, dirs, files in os.walk(images_dir):
    for f in files:
        if f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png')):
            all_files.append(os.path.join(root, f))

print(f"Checking {len(all_files)} images...")

for path in all_files:
    sz = os.path.getsize(path)
    if sz > MAX_BYTES:
        print(f"Compressing {os.path.basename(path)}: was {sz} bytes...")
        img = Image.open(path)
        is_rgba = (img.mode == 'RGBA')
        
        # Iteratively reduce dimensions and quality until under MAX_BYTES
        max_dim = 1200
        quality = 80
        fmt = "WEBP" if path.lower().endswith('.webp') else ("PNG" if path.lower().endswith('.png') else "JPEG")
        
        while sz > MAX_BYTES and (max_dim >= 600 or quality >= 30):
            w, h = img.size
            if max(w, h) > max_dim:
                scale = max_dim / max(w, h)
                resized = img.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
            else:
                resized = img.copy()
            
            if fmt == "WEBP":
                resized.save(path, format="WEBP", quality=quality, method=6)
            elif fmt == "JPEG":
                if resized.mode != "RGB":
                    resized = resized.convert("RGB")
                resized.save(path, format="JPEG", quality=quality, optimize=True)
            elif fmt == "PNG":
                resized.save(path, format="PNG", optimize=True)
                
            sz = os.path.getsize(path)
            quality -= 5
            if quality < 50:
                max_dim -= 100

        print(f" -> Result for {os.path.basename(path)}: {sz} bytes")

print("\n--- FINAL VERIFICATION: ALL ASSETS UNDER 100KB ---")
over_count = 0
for root, dirs, files in os.walk(images_dir):
    for f in files:
        p = os.path.join(root, f)
        size = os.path.getsize(p)
        status = "OK (<100KB)" if size < 100000 else "OVER!"
        if size >= 100000:
            over_count += 1
        print(f"{os.path.relpath(p, workspace)}: {size:,} bytes | {status}")

print(f"\nTotal oversized files: {over_count}")
