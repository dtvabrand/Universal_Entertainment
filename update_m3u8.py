import requests
from bs4 import BeautifulSoup

# Creare una sessione di requests
session = requests.Session()

# Impostare i cookies nella sessione (sostituisci con i tuoi cookies di YouTube)
cookies = {
    'cookie_name': 'cookie_value',
    # Aggiungi altri cookies necessari
}
session.cookies.update(cookies)

def grab_youtube(url: str):
    """
    Grabs the live-streaming M3U8 file from YouTube
    :param url: The YouTube URL of the livestream
    """
    if '&' in url:
        url = url.split('&')[0]

    requests.packages.urllib3.disable_warnings()
    stream_info = session.get(url, timeout=15)
    response = stream_info.text
    soup = BeautifulSoup(stream_info.text, features="html.parser")

    if '.m3u8' not in response or stream_info.status_code != 200:
        return "https://github.com/ExperiencersInternational/tvsetup/raw/main/staticch/no_stream_2.mp4"
    
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end - tuner: end]:
            link = response[end - tuner: end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            return link[start: end]
        else:
            tuner += 5

video_url = 'https://www.youtube.com/watch?v=2Xn1Bb697A0'
m3u8_url = grab_youtube(video_url)
print(m3u8_url)
