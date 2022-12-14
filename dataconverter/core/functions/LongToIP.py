# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations
from typing import List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class LongToIP(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_STRING

    def apply(self, data: int) -> List[str]:
        result = ""

        result = self._long_to_ip(int(data))

        return [result]

    @staticmethod
    def _long_to_ip(ipint: int) -> str:
        return ".".join([str(ipint >> (i << 3) & 0xFF) for i in range(4)[::-1]])


if __name__ == "__main__":
    _ipint = 16909060  # 1.2.3.4
    print(LongToIP(stat_dict=None, arg_list=[]).apply(_ipint))
