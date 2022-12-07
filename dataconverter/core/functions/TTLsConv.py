# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, Intelligence R&D Center.

from __future__ import annotations

from typing import Optional, Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract


class TTLsConv(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.num_feat = 3

    def apply(self, data: Union[float, str]) -> List[Optional[int]]:
        try:
            split_data: list = data.split(" ")
            if len(split_data) == 1:
                return [int(split_data[0]), int(split_data[0]), int(split_data[0])]
            elif len(split_data) > 1:
                split_data = list(map(int, split_data))
                return [min(split_data), max(split_data), (sum(split_data) / len(split_data))]
            else:
                return [0, 0, 0]
        except Exception as e:
            return [0, 0, 0]


if __name__ == "__main__":
    ip = "192.168.2.236"
    ip_split = ip.split(" ")
    print(ip_split)
