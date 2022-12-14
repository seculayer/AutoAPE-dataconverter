# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations
from typing import List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class RefererInfo(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_STRING

    def apply(self, data: str) -> List[str]:
        referer = data.strip()
        referer = referer.split("?")[0]
        referer = referer.replace(":", "_")

        return [referer]


if __name__ == "__main__":
    payload_list = ["www.g2b.go.kr:8081/gov/koneps/co.css/base.css"]
    # payload = ["www.g2b.go.kr:8081/pt/menu/selectSubFrame.do"]
    tokenizer = RefererInfo(stat_dict=None, arg_list=[1])
    for payload in payload_list:
        result = tokenizer.apply(payload)
        print(result)
        print(len(result))
