import os
import shutil
import json
import re

def migrate_and_optimize():
    root = os.getcwd()
    
    # 1. Load 120 keywords
    with open(os.path.join(root, 'scratch', 'keywords_100.txt'), 'r', encoding='utf-8') as f:
        keywords_str = f.read()
    keywords_list = [k.strip() for k in keywords_str.split(',') if k.strip()]
    
    print(f"Loaded {len(keywords_list)} keywords.")
    
    # 2. File relocation mapping
    moves = [
        ('tentang/index.html', 'tentang.html'),
        ('produk/index.html', 'produk.html'),
        ('portofolio/index.html', 'portofolio.html'),
        ('blog/index.html', 'blog.html'),
        ('blog/tahapan-pembangunan-vila/index.html', 'blog/tahapan-pembangunan-vila.html'),
        ('blog/instalasi-pipa-sebelum-pengecoran/index.html', 'blog/instalasi-pipa-sebelum-pengecoran.html'),
        ('blog/cara-memilih-kontraktor-vila/index.html', 'blog/cara-memilih-kontraktor-vila.html'),
        ('kontak/index.html', 'kontak.html'),
        ('kebijakan-privasi/index.html', 'kebijakan-privasi.html'),
    ]
    
    for src_rel, dst_rel in moves:
        src_path = os.path.join(root, src_rel)
        dst_path = os.path.join(root, dst_rel)
        if os.path.exists(src_path):
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy2(src_path, dst_path)
            print(f"Copied {src_rel} -> {dst_rel}")
            
    # Remove old index.html files and empty directories
    for src_rel, _ in moves:
        src_path = os.path.join(root, src_rel)
        if os.path.exists(src_path):
            os.remove(src_path)
            parent_dir = os.path.dirname(src_path)
            try:
                if len(os.listdir(parent_dir)) == 0:
                    os.rmdir(parent_dir)
                    print(f"Removed empty directory: {parent_dir}")
            except Exception as e:
                pass
                
    # Also clean up article subdirectories in blog/ if empty
    for d in ['tahapan-pembangunan-vila', 'instalasi-pipa-sebelum-pengecoran', 'cara-memilih-kontraktor-vila']:
        sub = os.path.join(root, 'blog', d)
        if os.path.exists(sub) and os.path.isdir(sub):
            try:
                if len(os.listdir(sub)) == 0:
                    os.rmdir(sub)
                    print(f"Removed empty subfolder: {sub}")
            except Exception:
                pass

    print("File migration completed. Now updating all HTML contents...")

if __name__ == '__main__':
    migrate_and_optimize()
