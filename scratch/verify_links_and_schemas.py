import os
import re
import json

def verify_site():
    root_dir = os.getcwd()
    html_files = []
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'scratch' in dirpath or '.agents' in dirpath:
            continue
        for f in filenames:
            if f.endswith('.html'):
                html_files.append(os.path.join(dirpath, f))
                
    print(f"Found {len(html_files)} HTML pages:")
    for hf in html_files:
        print(" -", os.path.relpath(hf, root_dir))
        
    print("\n--- Verifying Links, Images, Schemas & OpenGraph ---")
    issues = 0
    
    for hf in html_files:
        rel_path = os.path.relpath(hf, root_dir)
        with open(hf, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Check for visible .html in internal links
        bad_links = re.findall(r'href=["\'](/[^"\']*?\.html)["\']', content)
        # 404.html is an exception if linked directly or not linked
        bad_links = [l for l in bad_links if not l.endswith('404.html')]
        if bad_links:
            print(f"[LINK WARNING] in {rel_path}: Found .html in href: {bad_links}")
            issues += 1
            
        # 2. Check for index.html in links
        if 'index.html' in content and 'sitemap.xml' not in content:
            # Let's check occurrences of index.html in href
            index_hrefs = re.findall(r'href=["\'][^"\']*index\.html[^"\']*["\']', content)
            if index_hrefs:
                print(f"[LINK ERROR] in {rel_path}: Found index.html in href: {index_hrefs}")
                issues += 1
                
        # 3. Check JSON-LD
        schema_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        if not schema_blocks:
            print(f"[SCHEMA ERROR] in {rel_path}: No JSON-LD block found!")
            issues += 1
        else:
            for i, block in enumerate(schema_blocks):
                try:
                    parsed = json.loads(block.strip())
                except Exception as e:
                    print(f"[SCHEMA PARSE ERROR] in {rel_path} (block {i}): {e}")
                    issues += 1
                    
        # 4. Check OpenGraph
        if '<meta property="og:title"' not in content or '<meta property="og:image"' not in content:
            print(f"[OG WARNING] in {rel_path}: Missing og:title or og:image!")
            issues += 1
            
        # 5. Check Scroll buttons (pages except 404)
        if '404.html' not in rel_path and 'hqcScrollUp' not in content:
            print(f"[SCROLL WARNING] in {rel_path}: Missing scroll controls (#hqcScrollUp)!")
            issues += 1
            
        # 6. Check images referenced exist
        img_srcs = re.findall(r'src=["\'](/assets/[^"\']+)["\']', content)
        for src in img_srcs:
            asset_local = os.path.join(root_dir, src.lstrip('/'))
            if not os.path.exists(asset_local):
                print(f"[IMAGE NOT FOUND] in {rel_path}: {src}")
                issues += 1

    if issues == 0:
        print("\nALL VERIFICATIONS PASSED CLEANLY! No broken images, valid JSON-LD schemas, clean URLs, and OG tags verified.")
    else:
        print(f"\nCompleted with {issues} issues to review.")

if __name__ == '__main__':
    verify_site()
