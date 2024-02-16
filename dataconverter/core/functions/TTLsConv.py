# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, Intelligence R&D Center.

from __future__ import annotations

from typing import Optional, Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class TTLsConv(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.num_feat = 3
        self.return_type = Constants.RETURN_TYPE_FLOAT

    def apply(self, data: Union[float, str]) -> List[Optional[float]]:
        split_data: list = data.split(" ")

        if len(split_data) == 0:
            return [0., 0., 0.]
        elif len(split_data) == 1:
            if split_data[0] == '':
                return [0., 0., 0.]
            return [float(split_data[0])] * 3
        elif len(split_data) > 1:
            split_data = list(map(float, split_data))
            return [min(split_data), max(split_data), (sum(split_data) / len(split_data))]
        else:
            return [0., 0., 0.]


if __name__ == "__main__":
    ip = "2.592E+7 321 0 1"
    rst = TTLsConv().apply(ip)
    print(rst)
