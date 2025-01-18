import yt_dlp

# URL del video YouTube
video_url = 'https://www.youtube.com/watch?v=2Xn1Bb697A0'

# Opzioni per yt-dlp, incluso un user agent personalizzato
ydl_opts = {
    'noplaylist': True,
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',  # User agent di un browser
}

# Estrazione dell'URL m3u8 dal video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, download=False)
    m3u8_url = info.get('url')

# Lettura del file playlist.m3u8 esistente
with open('playlist.m3u8', 'r') as file:
    lines = file.readlines()

# Sovrascrittura del file playlist.m3u8 con il nuovo link
with open('playlist.m3u8', 'w') as file:
    for line in lines:
        if line.startswith('https://manifest.googlevideo.com'):
            file.write(f"{m3u8_url}\n")  # Sovrascrive il vecchio link con il nuovo
        else:
            file.write(line)

# Stampa il link aggiornato
print(f"Updated m3u8 link: {m3u8_url}")
