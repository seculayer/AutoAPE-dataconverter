# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
import datetime

from dataconverter.core.ConvertAbstract import ConvertAbstract


class DateRemaining(ConvertAbstract):
    def __init__(self, **kwargs):
        super(DateRemaining, self).__init__(**kwargs)
        self.num_feat = 1

    def apply(self, data) -> list:
        try:
            remain_date = data
            if isinstance(data, list):
                remain_date = data[0]
            remain_date = remain_date.split(" ")[0]
            exp_time = datetime.datetime.strptime(remain_date, "%Y-%m-%d")

            return [(exp_time - datetime.datetime.now()).days]

        except Exception as e:
            return [0.0]

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
