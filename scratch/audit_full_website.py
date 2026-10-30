import os
import re
import json

def audit_website():
    root = os.getcwd()
    print("==================================================")
    print("      HQC WEBSITE FULL PRODUCTION AUDIT           ")
    print("==================================================")
    
    html_files = [
        'index.html',
        'tentang.html',
        'produk.html',
        'portofolio.html',
        'blog.html',
        'blog/blog.html',
        'blog/tahapan-pembangunan-vila.html',
        'blog/instalasi-pipa-sebelum-pengecoran.html',
        'blog/cara-memilih-kontraktor-vila.html',
        'kontak.html',
        'kebijakan-privasi.html',
        '404.html'
    ]
    
    total_issues = 0
    
    # 1. Check all HTML pages exist
    for hf in html_files:
        p = os.path.join(root, hf.replace('/', os.sep))
        if not os.path.exists(p):
            print(f"[FAIL] Missing page: {hf}")
            total_issues += 1
        else:
            size_kb = os.path.getsize(p) / 1024.0
            print(f"[PASS] Page exists: {hf} ({size_kb:.1f} KB)")
            
    # 2. Check index.html uniqueness
    all_index_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        if any(skip in dirpath for skip in ['scratch', '.agents', '.git']):
            continue
        for f in filenames:
            if f.lower() == 'index.html':
                rel = os.path.relpath(os.path.join(dirpath, f), root)
                all_index_files.append(rel)
    if len(all_index_files) == 1 and all_index_files[0] == 'index.html':
        print(f"\n[PASS] Exactly 1 index.html found at root: {all_index_files}")
    else:
        print(f"\n[FAIL] Multiple index.html found: {all_index_files}")
        total_issues += 1
        
    # 3. Check single sitemap.xml
    all_sitemaps = []
    for dirpath, dirnames, filenames in os.walk(root):
        if any(skip in dirpath for skip in ['scratch', '.agents', '.git']):
            continue
        for f in filenames:
            if f.lower() == 'sitemap.xml':
                rel = os.path.relpath(os.path.join(dirpath, f), root)
                all_sitemaps.append(rel)
    if len(all_sitemaps) == 1 and all_sitemaps[0] == 'sitemap.xml':
        print(f"[PASS] Exactly 1 sitemap.xml found at root: {all_sitemaps}")
    else:
        print(f"[FAIL] Multiple sitemap.xml found: {all_sitemaps}")
        total_issues += 1

    # 4. Check that ZERO .png or .jpg files exist in the project
    print("\n--- Verifying Image Formats (WebP Only, Zero PNG/JPG) ---")
    forbidden_images = []
    for dirpath, dirnames, filenames in os.walk(root):
        if any(skip in dirpath for skip in ['scratch', '.agents', '.git', 'node_modules']):
            continue
        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in ['.png', '.jpg', '.jpeg']:
                rel = os.path.relpath(os.path.join(dirpath, f), root)
                forbidden_images.append(rel)
    if forbidden_images:
        print(f"[FAIL] Found {len(forbidden_images)} non-WebP image files: {forbidden_images}")
        total_issues += len(forbidden_images)
    else:
        print("[PASS] ZERO PNG or JPG files in project. All images are 100% WebP (+ favicon.ico fallback)!")

    # 5. Deep check into each page
    print("\n--- Verifying Content, Schemas, Keywords & Links ---")
    for hf in html_files:
        p = os.path.join(root, hf.replace('/', os.sep))
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
            
        # Check Clean URL Enforcer
        if 'Clean URL Enforcer' not in c:
            print(f"[WARN] {hf}: Missing Clean URL Enforcer script in <head>")
            total_issues += 1
            
        # Check Keywords (>= 100)
        kw_match = re.search(r'<meta\s+name=["\']keywords["\']\s+content=["\'](.*?)["\']', c, re.IGNORECASE)
        if kw_match:
            kws = [k.strip() for k in kw_match.group(1).split(',') if k.strip()]
            if len(kws) < 100:
                print(f"[FAIL] {hf}: Keywords count is {len(kws)} (< 100)")
                total_issues += 1
        else:
            print(f"[FAIL] {hf}: Missing meta keywords")
            total_issues += 1
            
        # Check JSON-LD
        schema_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', c, re.DOTALL)
        if schema_match:
            try:
                data = json.loads(schema_match.group(1).strip())
                graph = data.get('@graph', [])
                if not graph:
                    print(f"[FAIL] {hf}: JSON-LD missing @graph")
                    total_issues += 1
            except Exception as e:
                print(f"[FAIL] {hf}: JSON-LD invalid JSON: {e}")
                total_issues += 1
        else:
            print(f"[FAIL] {hf}: Missing JSON-LD")
            total_issues += 1
            
        # Check WhatsApp button & floating controls (except 404)
        if hf != '404.html':
            if '6282144267826' not in c:
                print(f"[FAIL] {hf}: Missing official WhatsApp number 6282144267826")
                total_issues += 1
            if 'hqcScrollUp' not in c or 'hqcScrollDown' not in c:
                print(f"[FAIL] {hf}: Missing scroll up/down buttons")
                total_issues += 1
                
        # Check for bad internal links containing .html in href (except 404.html)
        bad_hrefs = re.findall(r'href=["\'](/[^"\']*?\.html)["\']', c)
        bad_hrefs = [h for h in bad_hrefs if not h.endswith('404.html')]
        if bad_hrefs:
            print(f"[FAIL] {hf}: Found .html in href: {bad_hrefs}")
            total_issues += 1

        # Check for any .png references in HTML
        if '.png' in c.lower():
            print(f"[FAIL] {hf}: Still contains .png references")
            total_issues += 1
            
    # 6. Check all images in assets/ are < 100KB
    print("\n--- Verifying Asset Sizes (< 100KB) ---")
    assets_dir = os.path.join(root, 'assets')
    overweight_images = []
    total_imgs = 0
    for dirpath, dirnames, filenames in os.walk(assets_dir):
        for f in filenames:
            if f.lower().endswith(('.webp', '.png', '.jpg', '.jpeg', '.ico')):
                total_imgs += 1
                fp = os.path.join(dirpath, f)
                kb = os.path.getsize(fp) / 1024.0
                if kb >= 100.0:
                    overweight_images.append((os.path.relpath(fp, root), kb))
                    
    if overweight_images:
        print(f"[FAIL] Found {len(overweight_images)} images over 100KB:")
        for img, kb in overweight_images:
            print(f"  - {img}: {kb:.2f} KB")
        total_issues += len(overweight_images)
    else:
        print(f"[PASS] All {total_imgs} images are strictly under 100KB!")
        
    print("\n==================================================")
    if total_issues == 0:
        print("AUDIT RESULT: 100% CLEAN - ALL TESTS PASSED!")
    else:
        print(f"AUDIT RESULT: {total_issues} issues detected.")
    print("==================================================")
    return total_issues

if __name__ == '__main__':
    exit(audit_website())
