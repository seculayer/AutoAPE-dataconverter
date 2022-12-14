# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations
from typing import List
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class IPTransferDivide(ConvertAbstract):
    """
    ip 주소를 '.'으로 split하여 반환한다
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 4
        self.return_type = Constants.RETURN_TYPE_STRING

    # 토크나이징 하는곳
    def apply(self, data: str) -> List[str]:
        row = data.split(".")[:4]

        return row


if __name__ == "__main__":
    payload = "192.168.1.110"
    tokenizer = IPTransferDivide(stat_dict=None, arg_list=None)
    print(tokenizer.apply(payload))
