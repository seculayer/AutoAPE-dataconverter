# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations

from typing import SupportsFloat, Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class CalDevUsage(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_FLOAT

    def apply(self, data: Union[str, float, SupportsFloat]) -> List[float]:
        return [float(data) / 100]


if __name__ == "__main__":
    payload = "24.5753"
    tokenizer = CalDevUsage(stat_dict=None, arg_list=None)
    print(tokenizer.apply(payload))
