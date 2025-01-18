from playwright.sync_api import sync_playwright
import json

def save_cookies_as_mozilla_format(cookies, file_path):
    with open(file_path, 'w') as f:
        f.write('# Netscape HTTP Cookie File\n')
        for cookie in cookies:
            f.write(f"{cookie['domain']}\t{'TRUE' if cookie['secure'] else 'FALSE'}\t{cookie['path']}\t{'TRUE' if cookie['httpOnly'] else 'FALSE'}\t{cookie['expires']}\t{cookie['name']}\t{cookie['value']}\n")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Accedi a YouTube e ottieni i cookie
    page.goto('https://www.youtube.com')
    page.wait_for_timeout(10000)  # Aspetta 10 secondi per assicurarti che la pagina si carichi completamente
    
    # Salva i cookie in formato Mozilla/Netscape
    cookies = context.cookies()
    save_cookies_as_mozilla_format(cookies, 'scripts/cookies.txt')
    
    browser.close()
