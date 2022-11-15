# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
import math

from dataconverter.core.ConvertAbstract import ConvertAbstract


class StringEntropy(ConvertAbstract):
    def __init__(self, **kwargs):
        super(StringEntropy, self).__init__(**kwargs)

    def apply(self, data) -> list:
        data_len = len(data)
        word_count = dict()

        for c in data:
            word_count[c] = word_count.get(c, 0) + 1

        return [
            sum([-(c / data_len) * math.log2(c / data_len) for _, c in word_count.items()])
        ]

    def processConvert(self, data):
        pass

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = "google.com"
    converter = StringEntropy()
    print(converter.apply(_data))
