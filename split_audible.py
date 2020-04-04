import requests
import sys
import time 
import re


if len(sys.argv) < 3:
    print("Usage: ")
    print(sys.argv[0] + " <FILE_IN> <CODE | META_DATA_URL> [\"ffmpeg options\" [OUTPUT_EXT]]")
    exit()

file_in = sys.argv[1]
file_ext = file_in.split('.')[-1]
chapters_url = sys.argv[2]
ffmpeg_option = "-c copy"
if len(sys.argv) > 3:
    ffmpeg_option = sys.argv[3]
if len(sys.argv) > 4:
    file_ext = sys.argv[4]

if re.fullmatch(r"[\w]+", chapters_url):
    chapters_url = f"https://stories.audible.com/audibleapi/1.0/content/{chapters_url}/metadata?drm_type=Hls&response_groups=chapter_info"

resp = requests.get(chapters_url)
content = resp.json()
chapters = content['content_metadata']['chapter_info']['chapters']




for i, chapter in enumerate(chapters):
    start_ms = str(time.strftime('%H:%M:%S', time.gmtime(chapter['start_offset_ms'] / 1000))) + '.' + f"{(chapter['start_offset_ms'] % 1000):03d}"
    length_ms = str(time.strftime('%H:%M:%S', time.gmtime(chapter['length_ms'] / 1000))) + '.' + f"{(chapter['length_ms'] % 1000):03d}"
    filename = f"{i:03d} {chapter['title']}.{file_ext}"
    filename = re.sub(r"[^\w\-_\. ']", '_', filename)
    print(f"ffmpeg -i \"{file_in}\" -ss {start_ms} -t {length_ms} {ffmpeg_option} \"{filename}\" & ^")

print("echo Done!")