import xml.etree.ElementTree as ET
import subprocess
import json

def parse_xml(file_path):
    """Parse the XML file and extract channel information."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        channels = []
        for channel in root.findall('channel'):
            channel_info = {
                'name': (channel.find('channel-name').text or '').strip() if channel.find('channel-name') is not None else 'Unknown',
                'youtube-url': (channel.find('youtube-url').text or '').strip() if channel.find('youtube-url') is not None else ''
            }
            if channel_info['youtube-url']:
                channels.append(channel_info)
        return channels
    except Exception as e:
        print(f'Error parsing XML: {e}')
        return None

def get_stream_url(youtube_url):
    """Use Streamlink to extract the best stream URL."""
    try:
        info_command = ['streamlink', '--json', youtube_url]
        info_process = subprocess.Popen(info_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        info_output, info_error = info_process.communicate()

        if info_process.returncode != 0:
            return None

        try:
            stream_info = json.loads(info_output)
            return stream_info['streams'].get('best', {}).get('url')
        except json.JSONDecodeError:
            return None
    except Exception:
        return None

if __name__ == '__main__':
    xml_file = 'youtubelinks.xml'

    channels = parse_xml(xml_file)
    if channels:
        for channel in channels:
            stream_url = get_stream_url(channel['youtube-url'])
            if stream_url:
                print(stream_url)
    else:
        print('No channels found.')
