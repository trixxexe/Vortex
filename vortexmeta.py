from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import sys
import os

def banner():
    os.system('clear')
    print("\033[1;32m") # Hacker Green
    print(" [ VORTEX - Image Metadata Extractor ]")
    print("\033[0m")

def get_exif(filename):
    try:
        image = Image.open(filename)
        image.verify()
        return image._getexif()
    except:
        return None

def get_geotagging(exif):
    if not exif: return None
    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif: return None
            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]
    return geotagging

def extract_meta():
    banner()
    img_path = input("\n\033[1;36m[?] Enter path to image (e.g. photo.jpg): \033[0m")
    
    if not os.path.exists(img_path):
        print("\033[1;31m[!] File not found.\033[0m")
        sys.exit()

    print(f"\n\033[1;33m[*] Extracting Data from {img_path}...\033[0m\n")
    
    try:
        image = Image.open(img_path)
        exifdata = image.getexif()
        
        # 1. Basic Details
        print("\033[1;37m[+] BASIC DETAILS:\033[0m")
        print(f" Format: {image.format}")
        print(f" Size:   {image.size}")
        print(f" Mode:   {image.mode}")
        
        # 2. EXIF Data (Camera Model, Date, Software)
        print("\n\033[1;37m[+] EXIF DATA:\033[0m")
        if exifdata:
            for tag_id in exifdata:
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # Filter out long bytes data
                if isinstance(data, bytes):
                    data = data.decode(errors='replace')[:20] + "..."
                print(f" {tag:25}: {data}")
        else:
            print(" No EXIF data found.")

        # 3. GPS Hunt (The Sigma Move)
        # Note: Accessing detailed GPS often requires raw _getexif processing
        # This is a basic check.
        
    except Exception as e:
        print(f"\033[1;31m[!] Error reading file: {e}\033[0m")

if __name__ == "__main__":
    extract_meta()

