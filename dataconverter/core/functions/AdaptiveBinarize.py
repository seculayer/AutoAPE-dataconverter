# -*- coding: utf-8 -*-
# Author : JunHyuck Kim
# e-mail : junhyuck.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

from __future__ import annotations
from typing import Any, List

from pycmmn.utils.CV2Utils import CV2Utils
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants

class AdaptiveBinarize(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """
           self.num_feat : int
               전처리 후 Feature 수
           self.return_type : int
                결과 값 type
            self.method : 0 or 1/
                          0 : 가우시안, 1 : 평균으로 적응형 이진화 계산을 한다.
       """
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_INT
        self.method = self.arg_list[0]

    def apply(self, data: Any) -> List:
        """
            데이터를 받아 실제 전처리를 진행하는 함수
        :param data: Any
            특정 line의 특정 column의 데이터
        :return: List
        """
        adaptive = None
        _cv2 = CV2Utils.get_cv2()
        img = _cv2.cvtColor(data, _cv2.COLOR_BGR2GRAY)
        """"
            block_size : threshold를 지정할 영역 크기(block_size^2)
            C : MEAN 이나 GAUSSIAN 결과에서 차감할 값
        """
        if self.method == 0: # GAUSSIAN을 이용한 이진화
            adaptive = _cv2.ADAPTIVE_THRESH_GAUSSIAN_C
        elif self.method == 1: # MEAN을 이용한 이진화
            adaptive = _cv2.ADAPTIVE_THRESH_MEAN_C
        binary = _cv2.adaptiveThreshold(img, 255, adaptive, _cv2.THRESH_BINARY, block_size=5, C=0)

        return [binary]

if __name__ == "__main__":
    from pycmmn.utils.ImageUtils import ImageUtils
    image_path = "/home/autoAPE"
    __cv2 = CV2Utils.get_cv2()
    with open(f"{image_path}/sobel.jpg", "rb") as img_f:
        img_arr = img_f.read()
        img_data = ImageUtils.load(img_arr)
        # _img = __cv2.imread(f"{image_path}/iris.jpg", __cv2.IMREAD_GRAYSCALE)
        rst = AdaptiveBinarize(stat_dict=None, arg_list=[1]).apply(img_data)

        print(rst[0])
    __cv2.imwrite(f"{image_path}/adaptive_binary_mean_r11st.jpg", rst[0])
