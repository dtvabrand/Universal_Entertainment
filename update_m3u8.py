import requests, re
html = requests.get("https://www.youtube.com/watch?v=2Xn1Bb697A0").text
new_m3u8 = re.search(r'https://manifest\.googlevideo\.com.*?\.m3u8', html).group()
file_url = "https://raw.githubusercontent.com/dtvabrand/Universal_Entertainment/refs/heads/main/playlist.m3u8"
updated_content = re.sub(r'https://manifest\.googlevideo\.com.*?\.m3u8', new_m3u8, requests.get(file_url).text)
requests.put(file_url, data=updated_content)
