import os
from PIL import Image

def generate_favicons():
    root_dir = os.getcwd()
    public_dir = os.path.join(root_dir, 'public')
    brand_dir = os.path.join(root_dir, 'assets', 'brand')
    os.makedirs(public_dir, exist_ok=True)
    os.makedirs(brand_dir, exist_ok=True)
    
    # Source image: hqc-emblem.png or image.png_20261026021835.jpg from parent Downloads
    src_path = os.path.join(brand_dir, 'hqc-emblem.png')
    if not os.path.exists(src_path):
        parent_src = os.path.join(os.path.dirname(root_dir), 'image.png_20261026021835.jpg')
        if os.path.exists(parent_src):
            src_path = parent_src
            
    print(f"Using source logo from: {src_path}")
    img = Image.open(src_path).convert('RGBA')
    
    # Create square canvas with high-end padding for circular/app icon safe zones
    w, h = img.size
    max_dim = max(w, h)
    
    # Square 512x512 with transparent background or navy luxury background for touch icons
    square_512 = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    scale = 440 / max_dim
    new_w = int(w * scale)
    new_h = int(h * scale)
    resized_emblem = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    offset_x = (512 - new_w) // 2
    offset_y = (512 - new_h) // 2
    square_512.paste(resized_emblem, (offset_x, offset_y), resized_emblem)
    
    # Apple touch icon 180x180 with elegant navy luxury background #10263F
    apple_icon = Image.new('RGBA', (180, 180), (16, 38, 63, 255))
    apple_scale = 140 / max_dim
    apple_w = int(w * apple_scale)
    apple_h = int(h * apple_scale)
    apple_resized = img.resize((apple_w, apple_h), Image.Resampling.LANCZOS)
    apple_icon.paste(apple_resized, ((180 - apple_w) // 2, (180 - apple_h) // 2), apple_resized)
    
    # Save destinations: root, public, and assets/brand
    dest_dirs = [root_dir, public_dir, brand_dir]
    
    for d in dest_dirs:
        # 1. favicon.png (512x512)
        fav_png = os.path.join(d, 'favicon.png')
        square_512.save(fav_png, format='PNG', optimize=True)
        
        # 2. favicon-512x512.png (512x512)
        fav_512 = os.path.join(d, 'favicon-512x512.png')
        square_512.save(fav_512, format='PNG', optimize=True)
        
        # 3. logo-512.png (512x512)
        logo_512 = os.path.join(d, 'logo-512.png')
        square_512.save(logo_512, format='PNG', optimize=True)
        
        # 4. apple-touch-icon.png (180x180)
        apple_path = os.path.join(d, 'apple-touch-icon.png')
        apple_icon.convert('RGB').save(apple_path, format='PNG', optimize=True)
        
        # 5. favicon-32x32.png
        fav_32 = os.path.join(d, 'favicon-32x32.png')
        square_512.resize((32, 32), Image.Resampling.LANCZOS).save(fav_32, format='PNG', optimize=True)
        
        # 6. favicon-16x16.png
        fav_16 = os.path.join(d, 'favicon-16x16.png')
        square_512.resize((16, 16), Image.Resampling.LANCZOS).save(fav_16, format='PNG', optimize=True)
        
        # 7. favicon.ico (16, 32, 48)
        ico_path = os.path.join(d, 'favicon.ico')
        square_512.save(ico_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
        
    print("All favicon, logo, and apple-touch-icon files generated across root, public, and assets/brand.")

if __name__ == '__main__':
    generate_favicons()
