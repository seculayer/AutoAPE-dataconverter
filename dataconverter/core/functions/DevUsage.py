# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations

from typing import SupportsFloat, Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class DevUsage(ConvertAbstract):
    """
    장비의 사용률을 0~1 사이로 Normalize 한다
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_FLOAT

    def apply(self, data: Union[str, float, SupportsFloat]) -> List[float]:
        return [(float(data) / 100.0 - 0.5) * 2]


if __name__ == "__main__":
    payload = "85.4543"
    tokenizer = DevUsage(stat_dict=None, arg_list=None)
    print(tokenizer.apply(payload))
