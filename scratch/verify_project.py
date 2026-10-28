import os

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"

print("--- 1. Checking all files with 'index' in their name ---")
index_files = []
for root, dirs, files in os.walk(workspace):
    for f in files:
        if 'index' in f.lower():
            p = os.path.relpath(os.path.join(root, f), workspace)
            index_files.append(p)
            print("Found:", p)

# Expected page route index files only
expected_indices = {
    "index.html",
    os.path.join("tentang", "index.html"),
    os.path.join("produk", "index.html"),
    os.path.join("portofolio", "index.html"),
    os.path.join("blog", "index.html"),
    os.path.join("blog", "tahapan-pembangunan-vila", "index.html"),
    os.path.join("blog", "instalasi-pipa-sebelum-pengecoran", "index.html"),
    os.path.join("blog", "cara-memilih-kontraktor-vila", "index.html"),
    os.path.join("kontak", "index.html"),
    os.path.join("kebijakan-privasi", "index.html"),
}

unexpected = [p for p in index_files if p not in expected_indices]
print("\nUnexpected index files found:", unexpected)

print("\n--- 2. Checking for .html or index.html in links ---")
html_files = []
for root, dirs, files in os.walk(workspace):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

href_issues = []
for hf in html_files:
    rel_path = os.path.relpath(hf, workspace)
    with open(hf, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            if 'href="' in line or "href='" in line:
                # Allow css/js links or canonical or favicon
                for bad in ['index.html', '.html"', ".html'"]:
                    if bad in line and '404.html' not in line:
                        href_issues.append((rel_path, idx, line.strip()))

if href_issues:
    print(f"Found {len(href_issues)} href issues:")
    for issue in href_issues:
        print(issue)
else:
    print("ALL HREFS ARE 100% CLEAN! No index.html or .html found in any navigation link!")

print("\n--- 3. Checking image file sizes (Must ALL be < 100,000 bytes) ---")
oversized = []
total_images = 0
for root, dirs, files in os.walk(workspace):
    for f in files:
        if f.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
            total_images += 1
            full_p = os.path.join(root, f)
            sz = os.path.getsize(full_p)
            rel = os.path.relpath(full_p, workspace)
            if sz > 100000:
                oversized.append((rel, sz))

print(f"Total images checked: {total_images}")
if oversized:
    print(f"OVERSIZED ({len(oversized)}):", oversized)
else:
    print("SUCCESS: EVERY SINGLE IMAGE IS STRICTLY UNDER 100KB!")
