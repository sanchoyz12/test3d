import urllib.request
import os

base_url = "https://messenger.abeto.co/assets/"
fonts = ["REM-Medium.font", "heading.font", "planet.font", "UglyDave-Alternates-optimized.font"]

for font in fonts:
    url = base_url + font
    local_path = "assets/" + font
    print("Downloading", url)
    try:
        urllib.request.urlretrieve(url, local_path)
    except Exception as e:
        print("Failed:", e)
    
    url = "https://messenger.abeto.co/" + font
    local_path = font
    print("Downloading", url)
    try:
        urllib.request.urlretrieve(url, local_path)
    except Exception as e:
        print("Failed:", e)
