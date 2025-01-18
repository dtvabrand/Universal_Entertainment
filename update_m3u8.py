import requests, re

# Usa una sessione per mantenere i cookie e gli header
session = requests.Session()

# Aggiungi headers per simulare il comportamento del browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

# Richiesta alla pagina di YouTube
html = session.get("https://www.youtube.com/watch?v=2Xn1Bb697A0", headers=headers).text

# Estrazione del link m3u8
new_m3u8 = re.search(r'"hlsManifestUrl":"(https://manifest\.googlevideo\.com.*?\.m3u8)"', html)
if new_m3u8:
    new_m3u8 = new_m3u8.group(1)
else:
    print("m3u8 link not found")
    exit(1)

# Ottieni e aggiorna il contenuto del file playlist.m3u8 su GitHub
file_url = "https://raw.githubusercontent.com/dtvabrand/Universal_Entertainment/refs/heads/main/playlist.m3u8"
file_content = session.get(file_url).text
updated_content = re.sub(r'https://manifest\.googlevideo\.com.*?\.m3u8', new_m3u8, file_content)

# Sovrascrivi il file su GitHub
requests.put(file_url, data=updated_content)

print(f"Nuovo link m3u8 trovato: {new_m3u8}")
