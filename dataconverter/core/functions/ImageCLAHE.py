# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : manki.baek@seculayer.com
# Powered by Seculayer © 2023 Service Model Team

from typing import Any, List
import numpy as np

from pycmmn.utils.CV2Utils import CV2Utils
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class ImageCLAHE(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_FLOAT

    def apply(self, data: Any) -> List:
        _cv2 = CV2Utils.get_cv2()
        img = _cv2.cvtColor(data, _cv2.COLOR_BGR2GRAY)
        clahe = _cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        img2 = clahe.apply(img)
        kernel = np.ones((2, 2), np.uint8)
        opening = _cv2.morphologyEx(img2, _cv2.MORPH_OPEN, kernel)

        return [opening]


if __name__ == "__main__":
    from pycmmn.utils.ImageUtils import ImageUtils
    image_path = "/home/autoAPE"
    __cv2 = CV2Utils.get_cv2()
    with open(f"{image_path}/iris.jpg", "rb") as img_f:
        img_arr = img_f.read()
        img_data = ImageUtils.load(img_arr)
        # _img = __cv2.imread(f"{image_path}/iris.jpg", __cv2.IMREAD_GRAYSCALE)
        rst = ImageCLAHE(stat_dict=None, arg_list=["A"]).apply(img_data)

    print(rst[0])
    __cv2.imwrite(f"{image_path}/rst.jpg", rst[0])
