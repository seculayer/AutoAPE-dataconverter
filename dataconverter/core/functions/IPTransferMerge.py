# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations

from typing import Union

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class IPTransferMerge(ConvertAbstract):
    """
    두개의 ip 주소를 하나의 필드로 합한 문자열을 반환한다.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 6
        self.return_type = Constants.RETURN_TYPE_STRING

    # 토크나이징 하는곳
    def apply(self, data: Union[tuple, list]):
        data1 = data[0]
        data2 = data[1]

        row = data1 + "." + data2
        row = [row] * 6

        return row


if __name__ == "__main__":
    payload = ["192.168.1.110", "192.168.1.111"]
    tokenizer = IPTransferMerge(stat_dict=None, arg_list=None)
    print(tokenizer.apply(payload))
