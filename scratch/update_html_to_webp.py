import os
import glob
import re

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
html_files = glob.glob(os.path.join(workspace, "**/*.html"), recursive=True)
html_files = [f for f in html_files if "node_modules" not in f and ".git" not in f]

print(f"Updating {len(html_files)} HTML files...")

for h in sorted(html_files):
    rel = os.path.relpath(h, workspace)
    with open(h, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content

    # 1. Favicon links
    content = content.replace(
        '<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">',
        '<link rel="icon" type="image/webp" sizes="16x16" href="/favicon-16x16.webp">'
    )
    content = content.replace(
        '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">',
        '<link rel="icon" type="image/webp" sizes="32x32" href="/favicon-32x32.webp">'
    )
    content = content.replace(
        '<link rel="icon" type="image/png" sizes="512x512" href="/favicon.png">',
        '<link rel="icon" type="image/webp" sizes="512x512" href="/favicon.webp">'
    )
    content = content.replace(
        '<link rel="icon" type="image/png" sizes="512x512" href="/favicon-512x512.png">',
        '<link rel="icon" type="image/webp" sizes="512x512" href="/favicon-512x512.webp">'
    )
    content = content.replace(
        '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">',
        '<link rel="apple-touch-icon" href="/apple-touch-icon.webp">'
    )

    # 2. Open Graph & Twitter
    content = content.replace(
        'https://hqc-high-quality-construction.vercel.app/assets/images/og/hqc-og-home.jpg',
        'https://hqc-high-quality-construction.vercel.app/assets/images/og/hqc-og-home.webp'
    )
    content = content.replace(
        '<meta property="og:image:type" content="image/jpeg">',
        '<meta property="og:image:type" content="image/webp">'
    )

    # 3. Schema logo
    content = content.replace(
        'https://hqc-high-quality-construction.vercel.app/favicon.png',
        'https://hqc-high-quality-construction.vercel.app/favicon.webp'
    )

    # 4. Any generic remaining /favicon.png
    content = content.replace('/favicon.png', '/favicon.webp')
    content = content.replace('/favicon-512x512.png', '/favicon-512x512.webp')
    content = content.replace('/apple-touch-icon.png', '/apple-touch-icon.webp')
    content = content.replace('/favicon-32x32.png', '/favicon-32x32.webp')
    content = content.replace('/favicon-16x16.png', '/favicon-16x16.webp')

    if content != orig_content:
        with open(h, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [UPDATED] {rel}")
    else:
        print(f"  [NO CHANGE] {rel}")

print("\nAll HTML files updated successfully.")
