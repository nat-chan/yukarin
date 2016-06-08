#!/bin/zsh

#刻み幅
#横:32
#縦:48

function par2waku(){
	width=$1;height=$2
	x=$3;y=$4
	txt+="-draw"
	txt+="line $((x-2)),$((y-1)) $((x-1)),$((y+height))"
	txt+="-draw"
	txt+="line $((x-1)),$((y-1)) $((x+width)),$((y-1))"
	txt+="-draw"
	txt+="line $((x+width)),$((y-1)) $((x+width)),$((y+height))"
	txt+="-draw"
	txt+="line $((x-1)),$((y+height)) $((x+width)),$((y+height))"
}

txt=()
for y in 1;do
	#mkdir $y
	#cd $y
	for x in 1 2 3;do
		par2waku 24 38 $((32*x-27-1)) $((48*y-36-2))
		#convert -crop 24x38+$((32*x-27-1))+$((48*y-36-2)) ../3657666.png ${x}.png
	done
	#cd ..
done

convert $txt $1 $2

