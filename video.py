

import requests
import wget
import urllib2, ssl
import shutil
import subprocess

for i in range(0,10):
    print i

    url = "https://live1.xegmenta.com/vods3/_definst_/smil:amazons3/xegmentavod/bancoagrario/140420/360.smil/media_w149394245_b548000_" + str(i) + ".ts"

    request = urllib2.Request(url)
    response = urllib2.urlopen(request, context=ssl._create_unverified_context())

    datatowrite = response.read()
    with open('c:/Users/pablo.uribe/Documents/Study/videos/video' + str(i) + '.ts', 'wb') as f:
        f.write(datatowrite)

    with open('c:/Users/pablo.uribe/Documents/Study/videos/videoJUNTO.ts', 'ab') as f:
        f.write(datatowrite)
