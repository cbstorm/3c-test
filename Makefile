URL = https://www.youtube.com/watch?v=xvU0C8cIWPs
FILE = asset/vid_0.mp4
CUT = asset/output-$(shell date +%s).mp4
U = https://media2.billizone.com/movie/personal_highrun/pheavyq/2020/11/30/1726/JANG258019/inn_pheavyq_20201130_1726_Tb1_%EC%9E%A5%EC%9E%AC%EA%B7%9C30_13.mp4
download:
	mkdir -p asset
	youtubedr download -q 137 $(URL) -o $(FILE)
info:
	youtubedr info $(URL)
cut:
	ffmpeg -i $(FILE) -ss 170 -t 30 -c:v copy -c:a copy -y $(CUT)
	# ffmpeg -i $(CUT) -filter:v fps=1 -y asset/output1.mp4
st:
	ffmpeg -i $(CUT) -frames:v 1 asset/output0.png
circle:
	python circle.py --video $(CUT)
deps:
	conda install --yes --file requirements.txt
deps-list:
	conda list -e > requirements.txt
durl:
	curl $(U) > asset/$(shell date +%s).mp4