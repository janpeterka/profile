#!/bin/bash
for filename in public/mms/*.mkv; do
		# echo $filename
		if [[ $filename == "public/mms/*.mkv" ]]; then
			break
		fi

        file=${filename##*/} #foo.mkv
        file_name=$(basename ${filename%.*}) #foo

        mkdir public/mms/$file_name
        # cp $filename public/mms/$file_name/$file
        mv $filename public/mms/$file_name/$file

        # ffmpeg -i public/mms/$file_name/$file  -vn -c:a libpm3lame -y public/mms/$file_name/$file_name.mp3
        # ffmpeg -i public/mms/$file_name/$file  -vn -b:a 192k public/mms/$file_name/$file_name.mp3
        ffmpeg -i public/mms/$file_name/$file public/mms/$file_name/$file_name.mp3

        ffmpeg -i public/mms/$file_name/$file public/mms/$file_name/$file_name.flv
done