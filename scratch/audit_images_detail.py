import os
import glob
from PIL import Image

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"

exts = ['png', 'jpg', 'jpeg', 'webp', 'gif', 'ico']
for ext in exts:
    files = glob.glob(os.path.join(workspace, f"**/*.{ext}"), recursive=True)
    files = [f for f in files if "node_modules" not in f and ".git" not in f]
    print(f"\n=== Extension: {ext} ({len(files)} files) ===")
    for f in sorted(files):
        rel = os.path.relpath(f, workspace)
        size = os.path.getsize(f)
        try:
            with Image.open(f) as im:
                dim = f"{im.width}x{im.height} ({im.format})"
        except Exception as e:
            dim = f"N/A ({e})"
        print(f"  {rel:50} | {size:7} B ({size/1024:6.2f} KB) | {dim}")
