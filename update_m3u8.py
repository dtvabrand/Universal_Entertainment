import requests, re

html = requests.get("https://www.youtube.com/watch?v=2Xn1Bb697A0", headers={'User-Agent': 'Mozilla/5.0'}).text
print(html)  # Aggiungi per vedere il contenuto della pagina
new_m3u8 = re.search(r'"hlsManifestUrl":"(https://manifest\.googlevideo\.com.*?\.m3u8)"', html)

if new_m3u8:
    new_m3u8 = new_m3u8.group(1)
    print(f"Nuovo link m3u8 trovato: {new_m3u8}")  # Debug
else:
    print("Link m3u8 non trovato nel contenuto HTML")
