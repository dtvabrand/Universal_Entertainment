import requests

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        print('URL M3U8 non trovato')
        return None

    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            return link[start : end]
        else:
            tuner += 5

# Esempio di utilizzo
video_url = 'https://www.youtube.com/watch?v=2Xn1Bb697A0'
m3u8_url = grab(video_url)
print(m3u8_url)
