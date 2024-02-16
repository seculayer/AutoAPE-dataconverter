# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
import datetime
import json

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class DateRemaining(ConvertAbstract):
    def __init__(self, **kwargs):
        super(DateRemaining, self).__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_INT

    def apply(self, data) -> list:
        remain_date = data
        if isinstance(remain_date, str):
            try:
                remain_date = json.loads(remain_date)
            except:
                return [0]
        if isinstance(remain_date, list):
            if len(remain_date) == 0 or remain_date[0] == '':
                return [0]
            remain_date = remain_date[0]
        remain_date = remain_date.split(" ")[0]
        exp_time = datetime.datetime.strptime(remain_date, "%Y-%m-%d")

        return [(exp_time - datetime.datetime.now()).days]

    def processConvert(self, data):
        return self.apply(data)

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = ["2023-10-08 21:29:19"]
    cvt = DateRemaining()
    print(cvt.apply(_data))
    print(cvt.apply(_data[0]))
