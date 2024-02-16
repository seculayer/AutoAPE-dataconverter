# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class StringLength(ConvertAbstract):
    def __init__(self, **kwargs):
        super(StringLength, self).__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_INT

    def apply(self, data) -> list:
        return [len(data)]

    def processConvert(self, data):
        return self.apply(data)

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = "www.google.com"
    converter = StringLength()
    print(converter.apply(_data))
