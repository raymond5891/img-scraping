#!/bin/bash

ROOT_PATH='../download_images/car'
FILE_SIZE_TH=10240
WIDTH_TH=256
HEIGHT_TH=256
GRADIENT_TH=80

python img_primary_filter.py \
	--root_dir ${ROOT_PATH} \
	--file_size_thred ${FILE_SIZE_TH} \
	--width_thred ${WIDTH_TH} \
	--height_thred ${HEIGHT_TH} \
	--gradient_thred ${GRADIENT_TH}

