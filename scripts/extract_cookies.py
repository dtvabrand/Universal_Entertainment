import os
import browser_cookie3

cookies = browser_cookie3.chrome()
with open('scripts/cookies.txt', 'w') as file:
    for cookie in cookies:
        file.write(f"{cookie.name}={cookie.value}\n")
