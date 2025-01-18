import httpx
import json

# Crea una sessione HTTP
client = httpx.Client(http2=True)

# Accedi a YouTube e ottieni i cookie
response = client.get('https://www.youtube.com')
cookies = client.cookies.jar

# Salva i cookie in formato Mozilla/Netscape
with open('scripts/cookies.txt', 'w') as file:
    file.write('# Netscape HTTP Cookie File\n')
    for cookie in cookies:
        expires = cookie.expires if cookie.expires else 0
        file.write(f"{cookie.domain}\tTRUE\t{cookie.path}\t{str(cookie.secure).upper()}\t{expires}\t{cookie.name}\t{cookie.value}\n")

print("Cookie estratti e salvati con successo.")
