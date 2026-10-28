import os
import shutil
import re

def setup_dual_clean_urls():
    root = os.getcwd()
    
    # Pairs of (flat_file, folder_index)
    pairs = [
        ('tentang.html', 'tentang/index.html'),
        ('produk.html', 'produk/index.html'),
        ('portofolio.html', 'portofolio/index.html'),
        ('blog.html', 'blog/index.html'),
        ('blog/tahapan-pembangunan-vila.html', 'blog/tahapan-pembangunan-vila/index.html'),
        ('blog/instalasi-pipa-sebelum-pengecoran.html', 'blog/instalasi-pipa-sebelum-pengecoran/index.html'),
        ('blog/cara-memilih-kontraktor-vila.html', 'blog/cara-memilih-kontraktor-vila/index.html'),
        ('kontak.html', 'kontak/index.html'),
        ('kebijakan-privasi.html', 'kebijakan-privasi/index.html'),
    ]
    
    clean_url_script = """  <!-- Clean URL Enforcer: Hide .html and /index from address bar immediately -->
  <script>
    (function() {
      try {
        var p = window.location.pathname;
        if (p.endsWith('.html')) {
          var clean = p.replace(/\\.html$/, '');
          if (clean.endsWith('/index')) clean = clean.replace(/\\/index$/, '');
          window.history.replaceState(null, '', (clean || '/') + window.location.search + window.location.hash);
        }
      } catch (e) {}
    })();
  </script>"""

    # 1. Update index.html
    index_path = os.path.join(root, 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Inject clean_url_script after <head> if not already there
    if '<!-- Clean URL Enforcer' not in content:
        content = content.replace('<head>', '<head>\n' + clean_url_script)
        
    # Standardize links to clean directory paths
    link_replacements = [
        ('href="/tentang"', 'href="/tentang/"'),
        ('href="/produk"', 'href="/produk/"'),
        ('href="/portofolio"', 'href="/portofolio/"'),
        ('href="/blog"', 'href="/blog/"'),
        ('href="/kontak"', 'href="/kontak/"'),
        ('href="/kebijakan-privasi"', 'href="/kebijakan-privasi/"'),
        ('href="/blog/tahapan-pembangunan-vila"', 'href="/blog/tahapan-pembangunan-vila/"'),
        ('href="/blog/instalasi-pipa-sebelum-pengecoran"', 'href="/blog/instalasi-pipa-sebelum-pengecoran/"'),
        ('href="/blog/cara-memilih-kontraktor-vila"', 'href="/blog/cara-memilih-kontraktor-vila/"'),
        # Also ensure no .html in any href
        ('href="/tentang.html"', 'href="/tentang/"'),
        ('href="/produk.html"', 'href="/produk/"'),
        ('href="/portofolio.html"', 'href="/portofolio/"'),
        ('href="/blog.html"', 'href="/blog/"'),
        ('href="/kontak.html"', 'href="/kontak/"'),
        ('href="/kebijakan-privasi.html"', 'href="/kebijakan-privasi/"'),
        ('href="tentang.html"', 'href="/tentang/"'),
        ('href="produk.html"', 'href="/produk/"'),
        ('href="portofolio.html"', 'href="/portofolio/"'),
        ('href="blog.html"', 'href="/blog/"'),
        ('href="kontak.html"', 'href="/kontak/"'),
    ]
    
    for old_l, new_l in link_replacements:
        content = content.replace(old_l, new_l)
        
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html")

    # 2. Update each pair
    for flat_rel, folder_rel in pairs:
        flat_path = os.path.join(root, flat_rel.replace('/', os.sep))
        folder_path = os.path.join(root, folder_rel.replace('/', os.sep))
        
        # Read from flat_path if exists, otherwise folder_path
        src_path = flat_path if os.path.exists(flat_path) else folder_path
        with open(src_path, 'r', encoding='utf-8') as f:
            c = f.read()
            
        if '<!-- Clean URL Enforcer' not in c:
            c = c.replace('<head>', '<head>\n' + clean_url_script)
            
        for old_l, new_l in link_replacements:
            c = c.replace(old_l, new_l)
            
        # Write to both flat_path and folder_path
        os.makedirs(os.path.dirname(flat_path), exist_ok=True)
        with open(flat_path, 'w', encoding='utf-8') as f:
            f.write(c)
            
        os.makedirs(os.path.dirname(folder_path), exist_ok=True)
        with open(folder_path, 'w', encoding='utf-8') as f:
            f.write(c)
            
        print(f"Synced {flat_rel} <-> {folder_rel}")

    # 3. Also update 404.html
    f404 = os.path.join(root, '404.html')
    if os.path.exists(f404):
        with open(f404, 'r', encoding='utf-8') as f:
            c404 = f.read()
        if '<!-- Clean URL Enforcer' not in c404:
            c404 = c404.replace('<head>', '<head>\n' + clean_url_script)
        for old_l, new_l in link_replacements:
            c404 = c404.replace(old_l, new_l)
        with open(f404, 'w', encoding='utf-8') as f:
            f.write(c404)
        print("Updated 404.html")

    print("\nDual clean URL setup successfully applied across all pages!")

if __name__ == '__main__':
    setup_dual_clean_urls()
