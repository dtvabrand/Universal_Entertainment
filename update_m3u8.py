import yt_dlp

# Configura yt-dlp per utilizzare i cookie dal browser
ydl_opts = {
    'cookiesfrombrowser': ('chrome',),
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'quiet': True,
    'skip_download': True,
    'format': 'best',
    'writeinfojson': True,
}

# URL del video YouTube
url = 'https://www.youtube.com/watch?v=2Xn1Bb697A0'

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    m3u8_url = info_dict.get('url', '')

    # Salva il link m3u8 in un file
    with open('m3u8_link.txt', 'w') as file:
        file.write(m3u8_url)

print(f'Link m3u8: {m3u8_url}')
