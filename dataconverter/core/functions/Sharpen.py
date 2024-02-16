# -*- coding: utf-8 -*-
# Author : JunHyuck Kim
# e-mail : junhyuck.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

from __future__ import annotations
from typing import Any, List
import numpy as np

from pycmmn.utils.CV2Utils import CV2Utils
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants

class Sharpen(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """
           self.num_feat : int
               전처리 후 Feature 수
           self.return_type : int
                결과 값 type
       """
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_INT

    def apply(self, data: Any) -> List:
        """
            데이터를 받아 실제 전처리를 진행하는 함수
        :param data: Any
            특정 line의 특정 column의 데이터
        :return: List
        """
        _cv2 = CV2Utils.get_cv2()
        img = _cv2.cvtColor(data, _cv2.COLOR_BGR2GRAY)
        """
        커널 3x3, 중앙 값 + 그 외의 값의 합의 합이 1이되는 커널 구조
        중앙 값: 9, 그 외의 값의 합 : -8
        """
        sharpening_kernel = np.array([[-1, -1, -1],
                                      [-1, 9, -1],
                                      [-1, -1, -1]])

        sharpened = _cv2.filter2D(img, -1, sharpening_kernel)

        return [sharpened]


if __name__ == "__main__":
    from pycmmn.utils.ImageUtils import ImageUtils
    image_path = "/home/autoAPE"
    __cv2 = CV2Utils.get_cv2()
    with open(f"{image_path}/sobel.jpg", "rb") as img_f:
        img_arr = img_f.read()
        img_data = ImageUtils.load(img_arr)
        rst = Sharpen(stat_dict=None, arg_list=None).apply(img_data)

        print(rst[0])
    __cv2.imwrite(f"{image_path}/sharpen_rst.jpg", rst[0])


