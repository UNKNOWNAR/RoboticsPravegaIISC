import os
from PIL import Image

def compress_images(folder, quality=60, max_size=1200):
    """Compress all images in folder to reduce PDF size"""
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                filepath = os.path.join(root, file)
                print(f"Compressing: {file}")
                
                try:
                    img = Image.open(filepath)
                    
                    # Convert RGBA to RGB for JPEG
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                    
                    # Resize if too large
                    if max(img.size) > max_size:
                        ratio = max_size / max(img.size)
                        new_size = (int(img.size[0] * ratio), int(img.size[1] * ratio))
                        img = img.resize(new_size, Image.Resampling.LANCZOS)
                    
                    # Save with compression
                    if file.lower().endswith('.png'):
                        # For PNG, convert to JPEG for better compression
                        new_path = filepath.rsplit('.', 1)[0] + '.jpg'
                        img.save(new_path, 'JPEG', quality=quality, optimize=True)
                        os.remove(filepath)
                        print(f"  Converted to JPEG: {os.path.basename(new_path)}")
                    else:
                        img.save(filepath, 'JPEG', quality=quality, optimize=True)
                    
                    new_size_kb = os.path.getsize(filepath if file.lower().endswith(('.jpg', '.jpeg')) else new_path) / 1024
                    print(f"  New size: {new_size_kb:.1f} KB")
                    
                except Exception as e:
                    print(f"  Error: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_dir, 'images')
    cad_dir = os.path.join(base_dir, 'cad')
    
    print("Compressing images folder...")
    compress_images(images_dir, quality=70, max_size=1000)
    
    print("\nCompressing CAD folder...")
    compress_images(cad_dir, quality=70, max_size=1200)
    
    print("\n✅ Done! Now regenerate PDF.")
