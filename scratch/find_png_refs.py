import glob
import re
import os

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
html_files = glob.glob(os.path.join(workspace, "**/*.html"), recursive=True)

print(f"Scanning {len(html_files)} HTML files for .png or .jpg:")
for h in html_files:
    if "node_modules" in h:
        continue
    with open(h, "r", encoding="utf-8") as f:
        content = f.read()
    png_matches = re.findall(r'[^"\'><\s]+\.png', content, re.IGNORECASE)
    jpg_matches = re.findall(r'[^"\'><\s]+\.jpe?g', content, re.IGNORECASE)
    if png_matches or jpg_matches:
        rel = os.path.relpath(h, workspace)
        print(f"\n{rel}:")
        if png_matches:
            print("  PNG:", sorted(set(png_matches)))
        if jpg_matches:
            print("  JPG:", sorted(set(jpg_matches)))
