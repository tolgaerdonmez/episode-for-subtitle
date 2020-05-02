# episode-for-subtitle
Episode-Subtitle Matcher

[See the new version which is more secure, stable and has a GUI](https://github.com/tolgaerdonmez/video-subtitle-matcher)

### Use this on your own risk, your files can be overwrited while renaming. I hope that does not happen :)
### **Note:** Episodes and subtitles need to be in alpabethical order or in numerical

#### For Example:

episodes can be: (the file format doesn't need to be .mp4 in the code that i implemented have *.mp4,.mkv,.avi* you can add them like in code given)

1.mp4 - 2.mp4 ....

Episode1.mp4 - Episode2.mp4 ....

subtitles can be:

1.srt - 2.srt ....

Subtitle1.mp4 - Subtitle2.mp4 ....

#### Instructions

1. Take the subtitles and the episodes in one folder
2. copy the EpisodeRenamerForSubtitle.py to the directory above the folder which includes episodes and subtitles
run **EpisodeRenamerForSubtitle.py**
type the path like:
*Season1/*

For **linux** uncomment lines includes:

```
episodes.sort()

subtitles.sort()
```

*for windows comment these out*
