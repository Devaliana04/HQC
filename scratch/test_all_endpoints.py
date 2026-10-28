import os
import http.server
import socketserver
import threading
import urllib.request
import time

def test_endpoints():
    PORT = 8765
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        thread = threading.Thread(target=httpd.serve_forever)
        thread.daemon = True
        thread.start()
        print(f"Test server started on port {PORT}")
        time.sleep(0.5)
        
        urls_to_test = [
            f"http://127.0.0.1:{PORT}/",
            f"http://127.0.0.1:{PORT}/tentang/",
            f"http://127.0.0.1:{PORT}/produk/",
            f"http://127.0.0.1:{PORT}/portofolio/",
            f"http://127.0.0.1:{PORT}/blog/",
            f"http://127.0.0.1:{PORT}/blog/tahapan-pembangunan-vila/",
            f"http://127.0.0.1:{PORT}/blog/instalasi-pipa-sebelum-pengecoran/",
            f"http://127.0.0.1:{PORT}/blog/cara-memilih-kontraktor-vila/",
            f"http://127.0.0.1:{PORT}/kontak/",
            f"http://127.0.0.1:{PORT}/kebijakan-privasi/",
            # Flat html fallbacks
            f"http://127.0.0.1:{PORT}/tentang.html",
            f"http://127.0.0.1:{PORT}/produk.html",
            f"http://127.0.0.1:{PORT}/portofolio.html",
            f"http://127.0.0.1:{PORT}/blog.html",
            f"http://127.0.0.1:{PORT}/kontak.html",
            f"http://127.0.0.1:{PORT}/kebijakan-privasi.html",
            f"http://127.0.0.1:{PORT}/favicon.ico",
            f"http://127.0.0.1:{PORT}/favicon.png",
            f"http://127.0.0.1:{PORT}/site.webmanifest",
            f"http://127.0.0.1:{PORT}/robots.txt",
            f"http://127.0.0.1:{PORT}/sitemap.xml",
        ]
        
        all_passed = True
        for u in urls_to_test:
            try:
                req = urllib.request.urlopen(u)
                code = req.getcode()
                body = req.read(200).decode('utf-8', errors='ignore')
                print(f"[HTTP {code}] OK: {u}")
            except Exception as e:
                print(f"[FAIL] {u}: {e}")
                all_passed = False
                
        httpd.shutdown()
        if all_passed:
            print("\nSUCCESS: All endpoints return HTTP 200 without Cannot GET errors!")
        else:
            print("\nFAIL: Some endpoints failed.")

if __name__ == '__main__':
    test_endpoints()
