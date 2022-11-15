# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
from dataconverter.core.ConvertAbstract import ConvertAbstract


class ListFirstValue(ConvertAbstract):
    def __init__(self, **kwargs):
        super(ListFirstValue, self).__init__(**kwargs)

        self.num_feat = 1

    def apply(self, data) -> list:
        try:
            if isinstance(data, str):
                data = data.split(" ")
            if isinstance(data, list):
                return [float(data[0])]
        except Exception as e:
            return [0.0]
        return [0.0]

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = ["200"]

    cvt = ListFirstValue()
    print(cvt.apply(_data))
