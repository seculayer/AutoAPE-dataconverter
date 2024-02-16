#  -*- coding: utf-8 -*-
#  Author : Subin Lee
#  e-mail : subin.lee@seculayer.com
#  Powered by Seculayer © 2021 Service Model Team, R&D Center.

from typing import Any, List
import numpy as np

from pycmmn.utils.CV2Utils import CV2Utils
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class BilateralBlur(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """
            self.num_feat : int
                전처리 후 feature 수
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
        :return: List[Union[str, float]]
        """
        _cv2 = CV2Utils.get_cv2()
        bilateralblur = _cv2.bilateralFilter(data, d=9, sigmaColor=75, sigmaSpace=75)
        """
        d : 양방향 필터 커널 크기
        sigmaColor : 색 공간에서 필터의 표준 편차
        sigmaSpace : 좌표 공간에서 필터의 표준 편차
        """

        return [bilateralblur]


if __name__ == "__main__":
    from pycmmn.utils.ImageUtils import ImageUtils
    image_path = "/home/autoAPE"
    __cv2 = CV2Utils.get_cv2()
    with open(f"{image_path}/iris.jpg", "rb") as img_f:
        img_arr = img_f.read()
        img_data = ImageUtils.load(img_arr)
        rst = BilateralBlur(stat_dict=None, arg_list=None).apply(img_data)

    __cv2.imwrite(f"{image_path}/bilateralblur_rst.jpg", rst[0])
