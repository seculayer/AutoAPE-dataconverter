# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
from dataconverter.core.ConvertAbstract import ConvertAbstract


class NumberConsecutive(ConvertAbstract):
    def __init__(self, **kwargs):
        super(NumberConsecutive, self).__init__(**kwargs)

    def apply(self, data) -> list:
        counts = []
        count = 1

        start = data[0]
        for c in data[1:]:
            if start == c:
                count += 1
            else:
                counts.append(count)
                start = c
                count = 1

        return [max(counts)]

    def processConvert(self, data):
        pass

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = "google.com"
    converter = NumberConsecutive()
    print(converter.apply(_data))
