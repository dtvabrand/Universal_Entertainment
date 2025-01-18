import yt_dlp

video_url = 'https://www.youtube.com/watch?v=2Xn1Bb697A0'

with yt_dlp.YoutubeDL() as ydl:
    info = ydl.extract_info(video_url, download=False)
    m3u8_url = info.get('url')

with open('playlist.m3u8', 'r') as file:
    lines = file.readlines()

with open('playlist.m3u8', 'w') as file:
    for line in lines:
        if line.startswith('https://manifest.googlevideo.com'):
            file.write(f"{m3u8_url}\n")
        else:
            file.write(line)

print(f"Updated m3u8 link: {m3u8_url}")
