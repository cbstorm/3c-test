URL = https://www.youtube.com/watch?v=ryqlYFgtCpA

download:
	youtubedr download -q 136 $(URL) -f asset/vid_0.mp4
info:
	youtubedr info $(URL)
cut:
	ffmpeg -i asset/vid_0.mp4 -ss 00:01:10 -t 00:01:20 -c:v copy -c:a copy asset/output0.mp4
	ffmpeg -i asset/output0.mp4 -filter:v fps=1 -y asset/output1.mp4
st:
	ffmpeg -i asset/output0.mp4 -frames:v 1 asset/output0.png
circle:
	python circle.py --video asset/output0.mp4