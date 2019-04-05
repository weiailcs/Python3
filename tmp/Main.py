# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np


def get_figure_name(directory_name):
    figures_name = []
    for figure_name in os.listdir(directory_name):
        if figure_name.split('.')[-1] in ['png', 'jpg', 'bmp']:
            figures_name.append(directory_name + '/' + figure_name)
    return figures_name


def cut_figure(figure_name):
    img = cv2.imread(figure_name)

    height = len(img)
    width = len(img[0])

    img_1 = img[:, :width // 2]
    img_2 = img[:, width // 2:]
    img_1_resize = cv2.resize(img_1, (width, height), interpolation=cv2.INTER_CUBIC)
    img_2_resize = cv2.resize(img_2, (width, height), interpolation=cv2.INTER_CUBIC)

    pre_name = '.'.join(figure_name.split('.')[:-1])
    if not os.path.exists(pre_name):
        os.makedirs(pre_name)

    cv2.imwrite(pre_name + '/' + pre_name.split('/')[1] + '_LeftPart.png', img_1)
    cv2.imwrite(pre_name + '/' + pre_name.split('/')[1] + '_RightPart.png', img_2)
    cv2.imwrite(pre_name + '/' + pre_name.split('/')[1] + '_LeftPartResize.png', img_1_resize)
    cv2.imwrite(pre_name + '/' + pre_name.split('/')[1] + '_RightPartResize.png', img_2_resize)


if __name__ == '__main__':
    figures_name = get_figure_name('figure')
    for figure_name in figures_name:
        cut_figure(figure_name)
