import requests
import argparse

def get_public_ip():
    response = requests.get("https://ifconfig.me")
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Non è possibile ottenere l'IP pubblico")

def update_m3u_file(port):
    ip = get_public_ip()
    with open('youtubelive.m3u', 'r') as file:
        data = file.read()

    # Sostituisci l'indirizzo IP e la porta con i nuovi valori
    data = data.replace('OLD_IP', ip).replace('OLD_PORT', port)

    with open('youtubelive.m3u', 'w') as file:
        file.write(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update m3u file with new port.')
    parser.add_argument('--port', required=True, help='Port number')

    args = parser.parse_args()
    update_m3u_file(args.port)
