import ImgTextClipboard
import cv2
import numpy as np

from PIL import Image


def main():
    # 透明度
    transparent = 0.5
    # 欲叠加图片路径
    add_img_path = 'images/pic.png'
    # 读取欲叠加图片
    add_img = cv2.imread(add_img_path, cv2.IMREAD_UNCHANGED)

    # 读取剪贴板内图片
    img = ImgTextClipboard.copyImgFormClipboard()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    img = picAdd(img, add_img, transparent)

    # 写入剪贴板
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ImgTextClipboard.pasteImgToClipboard(img)


# 图像叠加
def picAdd(img, add_img, transparent):
    img_size = img.shape
    add_img_size = add_img.shape

    # 图像裁剪
    img_s1 = img[:add_img_size[0], 0:]
    img_s2 = img[add_img_size[0]:img_size[0], 0:]

    img_s1_1 = img_s1[:, :add_img_size[1]]
    img_s1_2 = img_s1[:, add_img_size[1]:]

    # 叠加图像
    img_s1_1 = cv2.addWeighted(img_s1_1, 1 - transparent, add_img, transparent, 0)

    # 拼接图像
    img_s1 = np.concatenate([img_s1_1, img_s1_2], axis=1)
    img = np.concatenate([img_s1, img_s2], axis=0)

    return img


if __name__ == '__main__':
    main()
