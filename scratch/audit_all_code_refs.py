import os
import glob
import re

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"

search_exts = ['html', 'js', 'css', 'json', 'xml', 'txt', 'webmanifest']
all_files = []
for ext in search_exts:
    all_files.extend(glob.glob(os.path.join(workspace, f"**/*.{ext}"), recursive=True))

all_files = [f for f in all_files if "node_modules" not in f and ".git" not in f and "scratch" not in f]

print(f"Auditing {len(all_files)} production code files for .png or .jpg references:")
found_any = False
for f in sorted(all_files):
    rel = os.path.relpath(f, workspace)
    try:
        with open(f, "r", encoding="utf-8") as file_handle:
            text = file_handle.read()
    except Exception as e:
        continue

    png_matches = re.findall(r'[^"\'><\s\(\)]+\.png', text, re.IGNORECASE)
    jpg_matches = re.findall(r'[^"\'><\s\(\)]+\.jpe?g', text, re.IGNORECASE)

    if png_matches or jpg_matches:
        found_any = True
        print(f"\n{rel}:")
        if png_matches:
            print("  PNG matches:", set(png_matches))
        if jpg_matches:
            print("  JPG matches:", set(jpg_matches))

if not found_any:
    print("\nSUCCESS! Zero references to .png or .jpg found in any production code files!")
