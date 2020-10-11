
# -*- coding: utf-8 -*-
__version__ = "0.02"

"""
Source : https://github.com/izneo-get/audible-tools
"""

import requests
import sys
import time 
import re


if len(sys.argv) < 2:
    print("Usage: ")
    print(sys.argv[0] + " <CODE | META_DATA_URL> [FILE_IN [\"ffmpeg options\" [OUTPUT_EXT]]]")
    print()
    print("Examples:")
    print(sys.argv[0] + " B00TKSFFJE")
    print(sys.argv[0] + " \"https://stories.audible.com/audibleapi/1.0/content/B00TKSFFJE/metadata?drm_type=Hls&response_groups=chapter_info\"")
    print(sys.argv[0] + " B00TKSFFJE pierre_et_le_loup.mp4")
    print(sys.argv[0] + " B00TKSFFJE pierre_et_le_loup.mp4 \"-b:a 64k -c:a mp3\" mp3")
    exit()

chapters_url = sys.argv[1]

file_in = "file_in.mp4"
if len(sys.argv) > 2:
    file_in = sys.argv[2]
file_ext = file_in.split('.')[-1]

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
    chap_num = i + 1
    start_ms = str(time.strftime('%H:%M:%S', time.gmtime(chapter['start_offset_ms'] / 1000))) + '.' + f"{(chapter['start_offset_ms'] % 1000):03d}"
    length_ms = str(time.strftime('%H:%M:%S', time.gmtime(chapter['length_ms'] / 1000))) + '.' + f"{(chapter['length_ms'] % 1000):03d}"
    filename = f"{chap_num:03d} {chapter['title']}.{file_ext}"
    filename = re.sub(r"[^\w\-_\. ']", '_', filename)
    print(f"ffmpeg -i \"{file_in}\" -ss {start_ms} -t {length_ms} {ffmpeg_option} \"{filename}\" && ^")

print("echo Done!")