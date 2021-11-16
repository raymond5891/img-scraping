import re
import os
import cv2
import shutil
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Training')
parser.add_argument('--root_dir', default='../download_images/car',type=str,
                    help="path to your dataset")
parser.add_argument('--file_size_thred', default=10*1024, type=int,
					help='image size threashold')
parser.add_argument('--width_thred', default=256, type=int, 
					help='image width threashold')
parser.add_argument('--height_thred', default=256, type=int, 
					help='image width threashold')
parser.add_argument('--gradient_thred', default=80, type=int,
					help='image gradient threashold')

args = parser.parse_args()


# 检测输入图像是否需要
def check_img(img_path):
    img = cv2.imread(img_path, flags=cv2.IMREAD_COLOR)

    # file info
    file_size = os.path.getsize(img_path)
    img_height, img_width = img.shape[:2]
    if file_size < args.file_size_thred or \
		img_width < args.width_thred or \
		img_height < args.height_thred or \
		img_height/img_width > 1:
        return False

    # image basic feature
    img_dy = img[:img_height-1] - img[1:]
    img_dx = img[:, :img_width-1] - img[:, 1:]
    img_gradient = np.mean(np.abs(img_dx)) + np.mean(np.abs(img_dy))

    print(img_path, "img_gradient =", img_gradient)
    if img_gradient < args.gradient_thred:
        return False

    return True

if __name__ == '__main__':
    file_suffix = "jpeg|jpg|png"
    remove_dir = args.root_dir + "/remove"
    if not os.path.exists(remove_dir):
        os.makedirs(remove_dir)
    for img_name in os.listdir(args.root_dir):
        # 对处理文件的类型进行过滤
        if re.search(file_suffix, img_name) is None:
            continue
        img_path = args.root_dir + "/" + img_name
        if not check_img(img_path):
            output_path = remove_dir + "/" + img_name
            shutil.move(img_path, output_path)
