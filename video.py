

import requests
import wget
import urllib2, ssl
import shutil
import subprocess

for i in range(1,200):

    # url = "https://live1.xegmenta.com/vods3/_definst_/smil:amazons3/xegmentavod/bancoagrario/140420/360.smil/media_w149394245_b548000_" + str(i) + ".ts"

    url = "https://embed-fastly.wistia.com/deliveries/aded4fec93d39eba3e708c2b8d543df893f33e76.m3u8/seg-" + str(i) + "-v1-a1.ts"

    print url

    request = urllib2.Request(url)
    response = urllib2.urlopen(request, context=ssl._create_unverified_context())

    datatowrite = response.read()
    with open('c:/Users/pablo.uribe/Documents/Study/videosV/video' + str(i) + '.ts', 'wb') as f:
        f.write(datatowrite)

    with open('c:/Users/pablo.uribe/Documents/Study/videosV/videoJUNTO.ts', 'ab') as f:
        f.write(datatowrite)

    print i
