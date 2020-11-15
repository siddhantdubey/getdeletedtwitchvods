# Download Deleted Twitch Vods

#DISCLAIMER: I am fairly certain that for most streamers you can only obtain vods that were deleted within the last two months (60 days)

Requirements:
- Hashlib. install if you don't have it
- Datetime. install if you don't have it
- Python 3+  
 

Once you have all requirements installed, run the script and enter the info it needs (streamer name, vod ID, start timestamp of stream) and it will return a url. Feed this url into VLC's network stream and you can now view deleted vods.  

streamer name: the exact streamer's name  
vod ID: The broadcast id can be found in the last part of the URL on twitchtracker. For example https://twitchtracker.com/hasanabi/streams/40383779998, the broadcast id is 40383779998.  
start timestamp: formatted like this (YYYY-MM-DD HH:MM:SS) in UTC time.  

Credit to u/ForgotMyPassword_III for outlining the steps implemented in this script and to Geeken on twitch for showing that it is possible in the first place. 
