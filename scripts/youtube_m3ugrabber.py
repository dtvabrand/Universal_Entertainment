import yt_dlp
import os

def grab(url):
    # Utilizzo di yt-dlp per ottenere il flusso m3u8 da YouTube
    ydl_opts = {
        'quiet': True,
        'format': 'best',
        'extractor_args': {
            'youtube': {
                'geo_bypass': True,  # Per aggirare le restrizioni geografiche
            }
        },
        'outtmpl': 'temp.m3u8',  # Salva l'output temporaneo in un file m3u8
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])

        # Cerchiamo il flusso m3u8
        for f in formats:
            if 'm3u8' in f.get('url', ''):
                print(f"{f['url']}")
                return

    print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')

# URL direttamente di YouTube
url = 'https://www.youtube.com/watch?v=2Xn1Bb697A0'

# Stampa l'intestazione per la playlist
print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')

# Chiamata alla funzione con il link YouTube
grab(url)
