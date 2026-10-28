import os
import urllib.request

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
css_dir = os.path.join(workspace, "assets", "css")
js_dir = os.path.join(workspace, "assets", "js")
os.makedirs(css_dir, exist_ok=True)
os.makedirs(js_dir, exist_ok=True)

bs_css_url = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
bs_js_url = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"

print("Downloading Bootstrap CSS...")
urllib.request.urlretrieve(bs_css_url, os.path.join(css_dir, "bootstrap.min.css"))

print("Downloading Bootstrap Bundle JS...")
urllib.request.urlretrieve(bs_js_url, os.path.join(js_dir, "bootstrap.bundle.min.js"))

print("Bootstrap assets downloaded successfully!")
print("bootstrap.min.css:", os.path.getsize(os.path.join(css_dir, "bootstrap.min.css")), "bytes")
print("bootstrap.bundle.min.js:", os.path.getsize(os.path.join(js_dir, "bootstrap.bundle.min.js")), "bytes")
