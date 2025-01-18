import requests, re

url = "https://www.youtube.com/watch?v=2Xn1Bb697A0"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
}

# Prima richiesta per ottenere i cookie
session = requests.Session()
response = session.get(url, headers=headers)

# Estrarre i cookie dalla sessione
cookies = session.cookies.get_dict()

# Ottieni il contenuto HTML della pagina YouTube
html = response.text

# Estrai il link m3u8
new_m3u8 = re.search(r'"hlsManifestUrl":"(https://manifest\.googlevideo\.com.*?\.m3u8)"', html)

if new_m3u8:
    new_m3u8 = new_m3u8.group(1)
    print(f"Nuovo link m3u8 trovato: {new_m3u8}")  # Debug

    # URL del file playlist.m3u8
    file_url = "https://raw.githubusercontent.com/dtvabrand/Universal_Entertainment/refs/heads/main/playlist.m3u8"
    
    # Ottieni il contenuto del file playlist.m3u8
    file_content = requests.get(file_url).text
    
    # Sostituisci il link m3u8 esistente con quello nuovo
    updated_content = re.sub(r'https://manifest\.googlevideo\.com.*?\.m3u8', new_m3u8, file_content)
    
    # Carica il contenuto aggiornato
    requests.put(file_url, data=updated_content)
else:
    print("Link m3u8 non trovato nel contenuto HTML")
