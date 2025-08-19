import os
import gzip
import xml.etree.ElementTree as ET
import requests
import re

save_as_gz = False  # Set to True to save an additional .gz version

urls = [
    'http://www.epgitalia.tv/gzip',
    'https://www.open-epg.com/files/italy1.xml.gz',
    'https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz',
    'https://epgshare01.online/epgshare01/epg_ripper_US1.xml.gz',
    'https://epgshare01.online/epgshare01/epg_ripper_US_LOCALS2.xml.gz',
    'https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz',
]

playlist_sets = [
    {"playlist_file": "playlist.m3u8", "output_file": "epg.xml"},
    {"playlist_file": "d_playlist.m3u8", "output_file": "d_epg.xml"},
]

def fetch_and_extract_xml(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    try:
        if url.endswith('.gz') or url.endswith('gzip'):
            decompressed_data = gzip.decompress(response.content)
            return ET.fromstring(decompressed_data)
        else:
            return ET.fromstring(response.content)
    except Exception as e:
        print(f"Failed to parse XML from {url}: {e}")
        return None

def filter_and_build_epg(playlist_file, output_file):
    playlist_path = os.path.join(os.path.dirname(__file__), playlist_file)
    output_path = os.path.join(os.path.dirname(__file__), output_file)
    output_gz_path = output_path + ".gz"

    with open(playlist_path, "r", encoding="utf-8") as f:
        playlist_content = f.read()

    tvg_ids = re.findall(r'tvg-id="([^"]+)"', playlist_content)

    root = ET.Element('tv')

    for url in urls:
        epg_data = fetch_and_extract_xml(url)
        if epg_data is None:
            continue

        for channel in epg_data.findall('channel'):
            if channel.get('id') in tvg_ids:
                root.append(channel)

        for programme in epg_data.findall('programme'):
            if programme.get('channel') in tvg_ids:
                root.append(programme)

    tree = ET.ElementTree(root)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    print(f"New EPG saved to {output_path}")

    with open(output_path, 'r+', encoding='utf-8') as f:
        xml_content = f.read()
        xml_content = xml_content.replace(' -0400', ' +0400')
        xml_content = xml_content.replace(' +0200', ' -0200')
        f.seek(0)
        f.write(xml_content)
        f.truncate()

    if save_as_gz:
        with gzip.open(output_gz_path, 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
        print(f"New EPG saved to {output_gz_path}")

if __name__ == "__main__":
    for pset in playlist_sets:
        filter_and_build_epg(pset["playlist_file"], pset["output_file"])
