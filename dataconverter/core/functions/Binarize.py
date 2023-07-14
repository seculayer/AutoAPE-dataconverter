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

class Binarize(ConvertAbstract):
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
            threshold : 이미지 평균 값
            평균 이하 -> 0
            평균 이상 -> 최댓값 : 255
        """
        thresh = np.mean(img, axis=(0,1))
        ret, binary = _cv2.threshold(img, thresh, 255, _cv2.THRESH_BINARY)

        return[binary]


if __name__ == "__main__":
    from pycmmn.utils.ImageUtils import ImageUtils
    image_path = "/home/autoAPE"
    __cv2 = CV2Utils.get_cv2()
    with open(f"{image_path}/sobel.jpg", "rb") as img_f:
        img_arr = img_f.read()
        img_data = ImageUtils.load(img_arr)
        # _img = __cv2.imread(f"{image_path}/iris.jpg", __cv2.IMREAD_GRAYSCALE)
        rst = Binarize(stat_dict=None, arg_list=None).apply(img_data)

        print(rst[0])
    __cv2.imwrite(f"{image_path}/binary_rst.jpg", rst[0])
