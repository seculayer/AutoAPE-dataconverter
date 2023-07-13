# -*- coding: utf-8 -*-
# Author : JunHyuck Kim
# e-mail : junhyuck.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

from typing import Any, List

from pycmmn.utils.CV2Utils import CV2Utils
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants

class Opening(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """
        self.num_feat : int
           전처리 후 Feature 수
        self.return_type : int
            결과 값 type
        self.iterations : 반복 횟수
        """
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_INT
        self.iterations = self.arg_list[0]

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
           kernel : 커널 형태 지정
           [[0 0 1 0 0]
            [0 0 1 0 0]
            [1 1 1 1 1]
            [0 0 1 0 0]
            [0 0 1 0 0]]
       """
        kernel = _cv2.getStructuringElement(_cv2.MORPH_CROSS, (5,5))
        opening = _cv2.morphologyEx(img, _cv2.MORPH_OPEN, kernel, iterations=self.iterations)

        return [opening]

if __name__ == "__main__":

    from pycmmn.utils.ImageUtils import ImageUtils
    image_path = "/home/autoAPE"
    __cv2 = CV2Utils.get_cv2()
    with open(f"{image_path}/noise_img.png", "rb") as img_f:
        img_arr = img_f.read()
        img_data = ImageUtils.load(img_arr)
        # _img = __cv2.imread(f"{image_path}/iris.jpg", __cv2.IMREAD_GRAYSCALE)
        rst = Opening(stat_dict=None, arg_list=[2]).apply(img_data)

        print(rst[0])
    __cv2.imwrite(f"{image_path}/opening_rst_arg5.jpg", rst[0])

