#!/bin/bash

# extract figures
pandoc $1 --extract-media=. -o tmp.md

# change extension to correct extention for tmp files
for f in media/*.tmp; do
	ext=$(file -b $f | awk '{print tolower($1)}')
	mv -- "$f" "${f%.tmp}.$ext"
done

#compress images
pngquant -f --ext .png media/*.png
jpegoptim -m 70 media/*.jpeg
jpegoptim -m 70 media/*.jpg

# format markdown files
python3 convert_pandoc.py tmp.md "${1%.docx}.md"

# clean
rm -rf media
