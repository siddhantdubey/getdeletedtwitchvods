import datetime
import hashlib
import requests


def totimestamp(dt, epoch=datetime.datetime(1970, 1, 1)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6


def geturl(year, month, day, hour, minute, seconds):

    td = datetime.datetime(year, month, day, hour, minute, seconds)

    converted_timestamp = totimestamp(td)

    formattedstring = streamername + "_" + vodID + "_" + str(int(converted_timestamp))

    hash = str(hashlib.sha1(formattedstring.encode('utf-8')).hexdigest())

    requiredhash = hash[:20]

    finalformattedstring = requiredhash + '_' + formattedstring

    url = f"https://vod-secure.twitch.tv/{finalformattedstring}/chunked/index-dvr.m3u8"

    return url


streamername = input("Enter streamer name: ").strip()
vodID = input("Enter vod id: ").strip()
timestamp = input("Enter VOD timestamp (YYYY-MM-DD HH:MM:SS) UTC:  ").strip()

year = int(timestamp[:4])
month = int(timestamp[5:7])
day = int(timestamp[8:10])

hour = int(timestamp[11:13])
minute = int(timestamp[14:16])
seconds = timestamp[17:]

if seconds == '--':
    print('searching ', end='', flush=True)
    for seconds in range(60):
        print('.', end='', flush=True)
        url = geturl(year, month, day, hour, minute, seconds)
        data = requests.get(url)
        found = 0
        if data.status_code == 200:
            print(" found at:", seconds, "s")
            print(url)
            found = 1
            break

    if found == 0:
        print("none found")

else:
    seconds = int(seconds)
    url = geturl(year, month, day, hour, minute, seconds)
    print(url)
