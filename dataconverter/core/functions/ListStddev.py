# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
import numpy as np

from dataconverter.core.ConvertAbstract import ConvertAbstract


class ListStddev(ConvertAbstract):
    def __init__(self, **kwargs):
        super(ListStddev, self).__init__(**kwargs)

        self.num_feat = 1

    def apply(self, data) -> list:
        try:
            if isinstance(data, str):
                data = data.split(" ")
            if isinstance(data, list):
                for idx, v in enumerate(data):
                    data[idx] = float(v)
                stddev = np.std(data)
                return [stddev]
        except Exception as e:
            return [0.0]
        return [0.0]

    def processConvert(self, data):
        pass

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = [
        "521", "300", "300", "521", "300", "521", "300", "21600", "300", "521", "300", "521",
        "300", "521", "300", "300", "521", "300", "300", "521", "12", "300"]

    _str_data = " ".join(_data)

    test = {"d": _data}

    cvt = ListStddev()
    print(cvt.apply(test.get("d")))
    print(cvt.apply(_str_data))
