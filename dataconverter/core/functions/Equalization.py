#  -*- coding: utf-8 -*-
#  Author : Subin Lee
#  e-mail : subin.lee@seculayer.com
#  Powered by Seculayer © 2021 Service Model Team, R&D Center.

from typing import Any, List

import cv2
import numpy as np

from pycmmn.utils.CV2Utils import CV2Utils
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class Equalization(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """
            self.num_feat : int
                전처리 후 feature 수
            self.return_type int
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
        hsv = _cv2.cvtColor(data, _cv2.COLOR_BGR2HSV)  # HSV 컬러맵으로 변환
        h, s, v = _cv2.split(hsv)  # h(색상), s(채도), v(명도)
        equalizedV = _cv2.equalizeHist(v)  # v에 평활화 적용
        hsv2 = _cv2.merge([h, s, equalizedV])  # 합친 후 새로운 HSV 이미지 생성
        equalization = _cv2.cvtColor(hsv2, _cv2.COLOR_HSV2BGR)  # BGR 컬러맵으로 변환

        return [equalization]


if __name__ == "__main__":
    from pycmmn.utils.ImageUtils import ImageUtils
    image_path = "/home/autoAPE"
    __cv2 = CV2Utils.get_cv2()
    with open(f"{image_path}/iris.jpg", "rb") as img_f:
        img_arr = img_f.read()
        img_data = ImageUtils.load(img_arr)
        rst = Equalization(stat_dict=None, arg_list=None).apply(img_data)

    __cv2.imwrite(f"{image_path}/equalization_rst.jpg", rst[0])
