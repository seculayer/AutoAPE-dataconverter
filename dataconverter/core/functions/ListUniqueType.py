# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
import numpy as np

from dataconverter.core.ConvertAbstract import ConvertAbstract


class ListUniqueType(ConvertAbstract):
    def __init__(self, **kwargs):
        super(ListUniqueType, self).__init__(**kwargs)

        self.num_feat = 1

    def apply(self, data) -> list:
        try:
            if isinstance(data, str):
                data = data.split(" ")
            if isinstance(data, list):
                return [len(np.unique(data))]
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
        "NS", "TXT", "TXT", "NS", "TXT", "NS", "TXT", "SOA", "TXT",
        "NS", "TXT", "NS", "TXT", "NS", "TXT", "TXT", "NS", "TXT", "TXT", "NS", "A", "TXT"]

    _str_data = " ".join(_data)

    cvt = ListUniqueType()
    print(cvt.apply(_data))
    print(cvt.apply(_str_data))
