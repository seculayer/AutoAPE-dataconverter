# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
import datetime

from dataconverter.core.ConvertAbstract import ConvertAbstract


class DateDiff(ConvertAbstract):
    def __init__(self, **kwargs):
        super(DateDiff, self).__init__(**kwargs)

        self.num_feat = 1
        self.datetime_format = "%Y-%m-%d"

    @staticmethod
    def date_normalize(x):
        x = x.split('|')
        x = x[-1].strip()
        x = x.split('T')[0]
        x = x.split(' ')[0].strip()
        return x

    def apply(self, data) -> list:
        try:
            if isinstance(data, list):
                for idx, ele in enumerate(data):
                    data[idx] = self.date_normalize(ele)

                return[
                    (datetime.datetime.strptime(data[1], self.datetime_format)
                     - datetime.datetime.strptime(data[0], self.datetime_format)
                     ).days
                ]

        except (ValueError, TypeError) as e:
            return [0.0]
        return [0.0]

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    cvt = DateDiff()
    print(cvt.apply(["2011-01-20T16:48:05.686Z", "2023-01-20T16:48:05.705Z"]))
    print(cvt.apply(["2011-01-20T16:48:05.686Z", "2021-12-13T19:01:59.181Z"]))
