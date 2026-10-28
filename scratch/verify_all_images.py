import os

def check_images():
    assets_dir = os.path.join(os.getcwd(), 'assets')
    all_ok = True
    print(f"{'File Path':<65} | {'Size (KB)':<10} | {'Status'}")
    print("-" * 88)
    
    for root, dirs, files in os.walk(assets_dir):
        # Verify no index.html exists in assets directories
        if 'index.html' in files:
            print(f"ERROR: index.html found in asset dir: {root}")
            all_ok = False
            
        for file in files:
            if file.lower().endswith(('.webp', '.jpg', '.jpeg', '.png', '.ico', '.svg')):
                full_path = os.path.join(root, file)
                size_bytes = os.path.getsize(full_path)
                size_kb = size_bytes / 1024.0
                rel_path = os.path.relpath(full_path, os.getcwd())
                
                status = "OK (<100KB)" if size_kb < 100 else "EXCEEDS 100KB"
                if size_kb >= 100:
                    all_ok = False
                print(f"{rel_path:<65} | {size_kb:>8.2f} KB | {status}")
                
    print("-" * 88)
    if all_ok:
        print("SUCCESS: 100% of images are strictly UNDER 100KB and NO index.html in asset folders!")
    else:
        print("FAIL: Some images exceed 100KB or index.html found in assets.")

if __name__ == '__main__':
    check_images()
