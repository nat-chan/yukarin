#!/bin/zsh

#刻み幅
#横:32
#縦:48

for y in 4;do
	mkdir $y
	cd $y
	for x in {1..8};do
		convert -crop 24x38+$((32*x-27-1))+$((48*y-36-2)) ../3657666.png ${x}.png
	done
	cd ..
done
