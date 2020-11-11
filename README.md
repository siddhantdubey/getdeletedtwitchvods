# Download Deleted Twitch Vods

Requirements:
- Hashlib. install if you don't have it
- Datetime. install if you don't have it
- Python 3+
 

Once you have all requirements installed, run the script and enter the info it needs (streamer name, vod ID, start timestamp of stream) and it will return a url. Feed this url into VLC's network stream and you can now view deleted vods.

streamer name: the exact streamer's name
vod ID: the broadcast id of the vod
start timestamp: formatted like this (YYYY-MM-DD HH:MM:SS) in UTC time.

Credit to u/ForgotMyPassword_III for outlining the steps implemented in this script and to Geeken on twitch for showing that it is possible in the first place. 
