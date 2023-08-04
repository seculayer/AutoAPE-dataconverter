#  -*- coding: utf-8 -*-
#  Author : Subin Lee
#  e-mail : subin.lee@seculayer.com
#  Powered by Seculayer © 2021 Service Model Team, R&D Center.

from typing import Any, List
import numpy as np

from pycmmn.utils.CV2Utils import CV2Utils
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class AverageBlur(ConvertAbstract):
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
        averageblur = _cv2.blur(data, ksize=(5, 5))
        """
        ksize : 평균 커널 크기
        """

        return [averageblur]


if __name__ == "__main__":
    from pycmmn.utils.ImageUtils import ImageUtils
    image_path = "/home/autoAPE"
    __cv2 = CV2Utils.get_cv2()
    with open(f"{image_path}/iris.jpg", "rb") as img_f:
        img_arr = img_f.read()
        img_data = ImageUtils.load(img_arr)
        rst = AverageBlur(stat_dict=None, arg_list=None).apply(img_data)

    __cv2.imwrite(f"{image_path}/averageblur_rst.jpg", rst[0])
