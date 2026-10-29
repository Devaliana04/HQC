import os
import re

def verify_final():
    root = os.getcwd()
    
    # 1. Count index.html
    index_files = []
    sitemaps = []
    for dirpath, dirnames, filenames in os.walk(root):
        if 'scratch' in dirpath or '.agents' in dirpath or '.git' in dirpath:
            continue
        for f in filenames:
            rel = os.path.relpath(os.path.join(dirpath, f), root)
            if f.lower() == 'index.html':
                index_files.append(rel)
            if f.lower() == 'sitemap.xml':
                sitemaps.append(rel)
                
    print(f"Index.html files count: {len(index_files)} -> {index_files}")
    assert len(index_files) == 1 and index_files[0] == 'index.html', "ERROR: Must have ONLY 1 index.html at root!"
    print("CHECK 1 PASSED: Only 1 index.html at root!")
    
    print(f"Sitemap.xml count: {len(sitemaps)} -> {sitemaps}")
    assert len(sitemaps) == 1 and sitemaps[0] == 'sitemap.xml', "ERROR: Must have ONLY 1 sitemap.xml at root!"
    print("CHECK 2 PASSED: Only 1 sitemap.xml at root!")
    
    # 2. Check internal links in blog articles
    blog_articles = [
        os.path.join(root, 'blog', 'tahapan-pembangunan-vila.html'),
        os.path.join(root, 'blog', 'instalasi-pipa-sebelum-pengecoran.html'),
        os.path.join(root, 'blog', 'cara-memilih-kontraktor-vila.html'),
    ]
    
    for ba in blog_articles:
        rel = os.path.relpath(ba, root)
        with open(ba, 'r', encoding='utf-8') as f:
            c = f.read()
        links = re.findall(r'href=["\'](/[^"\']+)["\']', c)
        internal_links = [l for l in links if not l.startswith('http') and not l.startswith('/assets/')]
        print(f"{rel}: {len(internal_links)} internal links found")
        assert len(internal_links) >= 10, f"ERROR: Not enough internal links in {rel}"
        assert 'hqc-related-articles' in c, f"ERROR: Missing related articles block in {rel}"
        
    print("CHECK 3 PASSED: All blog articles have rich contextual internal links & related articles!")

    print("\nALL VERIFICATIONS PASSED 100%!")

if __name__ == '__main__':
    verify_final()
