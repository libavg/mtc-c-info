#/bin/bash
export IN_MOVIE_DIR=../material/clamp_anim

ffmpeg -i ${IN_MOVIE_DIR}/clamp_64px_%04d.png -intra -vcodec mpeg2video -qscale 4 -an -y clamp_64.mpg

