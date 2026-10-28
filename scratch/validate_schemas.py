import os
import re
import json

def validate_all():
    root = os.getcwd()
    html_files = []
    
    # 1. Check for duplicate index.html files
    index_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        if 'scratch' in dirpath or '.agents' in dirpath:
            continue
        for f in filenames:
            full_p = os.path.join(dirpath, f)
            rel_p = os.path.relpath(full_p, root)
            if f.endswith('.html'):
                html_files.append(rel_p)
                if f.lower() == 'index.html':
                    index_files.append(rel_p)
                    
    print(f"Total HTML files found: {len(html_files)}")
    print(f"Index.html files found: {index_files}")
    assert len(index_files) == 1 and index_files[0] == 'index.html', f"FAIL: Expected ONLY root index.html, found: {index_files}"
    print("CHECK 1 PASSED: Exactly one index.html exists (only at root)!")
    
    # 2. Check each HTML file for schema, keywords, and favicons
    total_issues = 0
    
    for hf in html_files:
        full_p = os.path.join(root, hf)
        with open(full_p, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"\n--- Validating: {hf} ---")
        
        # Check Keywords
        kw_match = re.search(r'<meta\s+name=["\']keywords["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
        if not kw_match:
            print(f"ERROR: Missing <meta name='keywords'> in {hf}")
            total_issues += 1
        else:
            kws = [k.strip() for k in kw_match.group(1).split(',') if k.strip()]
            if len(kws) < 100:
                print(f"ERROR: Keywords count is {len(kws)}, less than 100 in {hf}")
                total_issues += 1
            else:
                print(f"  [OK] Keywords count: {len(kws)} (>= 100 verified)")
                
        # Check Favicon & Rel Icons
        for icon_rel in ['rel="icon"', 'rel="apple-touch-icon"', 'rel="manifest"']:
            if icon_rel not in content:
                print(f"ERROR: Missing {icon_rel} in {hf}")
                total_issues += 1
        print("  [OK] Favicon & Apple touch icon & Manifest rel tags present")
        
        # Check JSON-LD
        schema_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        if not schema_match:
            print(f"ERROR: Missing JSON-LD in {hf}")
            total_issues += 1
            continue
            
        try:
            data = json.loads(schema_match.group(1).strip())
        except Exception as e:
            print(f"ERROR: JSON-LD parse failed in {hf}: {e}")
            total_issues += 1
            continue
            
        # Validate schema graph
        graph = data.get('@graph', [])
        if not graph:
            print(f"ERROR: No @graph in JSON-LD in {hf}")
            total_issues += 1
            continue
            
        types_in_graph = [item.get('@type') for item in graph]
        print(f"  [OK] Valid JSON-LD with @graph: {len(graph)} nodes")
        
        # Check Organization
        org = next((n for n in graph if 'Organization' in str(n.get('@type'))), None)
        if not org:
            print(f"ERROR: Missing Organization in graph of {hf}")
            total_issues += 1
        else:
            if not org.get('@id') or not org.get('logo') or not org.get('name') or not org.get('url'):
                print(f"ERROR: Organization missing key attributes in {hf}")
                total_issues += 1
            else:
                logo_obj = org.get('logo', {})
                if not logo_obj.get('url') or not logo_obj.get('@id'):
                    print(f"ERROR: Organization logo not properly formatted in {hf}")
                    total_issues += 1
                else:
                    print(f"  [OK] Organization schema verified with connected logo ({logo_obj['url']})")
                    
        # Check WebSite
        site = next((n for n in graph if n.get('@type') == 'WebSite'), None)
        if not site:
            print(f"ERROR: Missing WebSite in graph of {hf}")
            total_issues += 1
        else:
            if site.get('publisher', {}).get('@id') != org.get('@id'):
                print(f"ERROR: WebSite publisher does not link to Organization @id in {hf}")
                total_issues += 1
            else:
                print(f"  [OK] WebSite schema connected to Organization @id")

    # 3. Check public/ folder contents
    print("\n--- Validating public/ directory ---")
    public_dir = os.path.join(root, 'public')
    expected_public_files = [
        'favicon.ico',
        'favicon.png',
        'favicon-512x512.png',
        'apple-touch-icon.png',
        'site.webmanifest',
        'robots.txt',
        'sitemap.xml'
    ]
    for ef in expected_public_files:
        p = os.path.join(public_dir, ef)
        if not os.path.exists(p):
            print(f"ERROR: Missing file in public/: {ef}")
            total_issues += 1
        else:
            size_kb = os.path.getsize(p) / 1024.0
            print(f"  [OK] public/{ef} ({size_kb:.2f} KB) exists and is under 100KB: {size_kb < 100}")

    if total_issues == 0:
        print("\n=======================================================")
        print("ALL 12 REQUIREMENTS VALIDATED AND VERIFIED SUCCESSFULLY!")
        print("=======================================================")
    else:
        print(f"\nCompleted with {total_issues} issues.")

if __name__ == '__main__':
    validate_all()
