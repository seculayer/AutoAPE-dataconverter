# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.core.functions.StringConsVowelCounter import StringConsVowelCounter
from dataconverter.core.functions.StringLength import StringLength
from dataconverter.common.Constants import Constants


class DNSDomainPreProcessing(ConvertAbstract):
    def __init__(self, **kwargs):
        super(DNSDomainPreProcessing, self).__init__(**kwargs)
        self.num_feat = 3
        self.return_type = Constants.RETURN_TYPE_INT

        self.cvt_str_len = StringLength()
        self.cvt_cv = StringConsVowelCounter(arg_list=["all"])

    def apply(self, data) -> list:
        return self.cvt_str_len.apply(data) + self.cvt_cv.apply(data)

    def processConvert(self, data):
        pass

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = "www.google.com"
    cvt = DNSDomainPreProcessing()
    print(cvt.apply(_data))
