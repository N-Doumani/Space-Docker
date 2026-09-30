import os
import urllib.request

# قاموس يحتوي على روابط صور الكواكب والأسماء المطلوبة في الموقع
PLANET_IMAGES = {
    "mercury.jpg": "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?auto=format&fit=crop&w=800&q=80",
    "venus.jpg": "https://images.unsplash.com/photo-1614728423169-3f65fd722b7e?auto=format&fit=crop&w=800&q=80",
    "earth.jpg": "https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?auto=format&fit=crop&w=800&q=80",
    "mars.jpg": "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?auto=format&fit=crop&w=800&q=80",
    "jupiter.jpg": "https://images.unsplash.com/photo-1630839437035-dac17da580d0?auto=format&fit=crop&w=800&q=80",
    "saturn.jpg": "https://images.unsplash.com/photo-1614732414444-096e5f1122d5?auto=format&fit=crop&w=800&q=80",
    "uranus.jpg": "https://images.unsplash.com/photo-1614732484003-ef9881555dc3?auto=format&fit=crop&w=800&q=80",
    "neptune.jpg": "https://images.unsplash.com/photo-1614313913007-2b4ae8ce32d6?auto=format&fit=crop&w=800&q=80",
    "pluto.jpg": "https://images.unsplash.com/photo-1545156521-77bd85671d30?auto=format&fit=crop&w=800&q=80",
}

def download_images():
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)
    
    print("⏳ بدء تنزيل الصور...")
    for filename, url in PLANET_IMAGES.items():
        filepath = os.path.join(output_dir, filename)
        if not os.path.exists(filepath):
            print(f"⬇️ جاري تنزيل: {filename}")
            urllib.request.urlretrieve(url, filepath)
        else:
            print(f"✅ موجود بالفعل: {filename}")
    print("🎉 تم تنزيل جميع الصور بنجاح!")

if __name__ == "__main__":
    download_images()