# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.core.functions.StringLength import StringLength
from dataconverter.core.functions.NumberConsecutive import NumberConsecutive
from dataconverter.core.functions.StringEntropy import StringEntropy


class DNSMetaPreProcessing(ConvertAbstract):
    def __init__(self, **kwargs):
        super(DNSMetaPreProcessing, self).__init__(**kwargs)

        self.cvt_str_len = StringLength()
        self.cvt_nc = NumberConsecutive()
        self.cvt_se = StringEntropy()

    def apply(self, data) -> list:
        try:
            result = self.cvt_str_len.apply(data)
            result += self.cvt_nc.apply(data)
            result += self.cvt_se.apply(data)
            return result
        except Exception as e:
            return [0.0, 0.0, 0.0]

    def processConvert(self, data):
        return self.apply(data)

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = "google.com"
    converter = DNSMetaPreProcessing()
    print(converter.apply(_data))
