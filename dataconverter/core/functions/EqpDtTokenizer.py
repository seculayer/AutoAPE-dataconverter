# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations
from typing import List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class EqpDtTokenizer(ConvertAbstract):
    """
    장비 발생 시각에서 시간과 분을 추출한다.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 2
        self.return_type = Constants.RETURN_TYPE_FLOAT

    # 토크나이징 하는곳
    def apply(self, data: str) -> List[float]:
        return [float(data[8:10]), float(data[10:12])]


if __name__ == "__main__":
    payload = "201812062106001"
    tokenizer = EqpDtTokenizer(stat_dict=None, arg_list=None)
    print(tokenizer.apply(payload))
