# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, Intelligence R&D Center.

from __future__ import annotations
from typing import Any, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class LabelEncode(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unique_dict = {}

        for idx, key in enumerate(self.stat_dict.get("unique", {}).get("unique", {}).keys()):
            self.unique_dict[key] = idx

        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_INT

    def apply(self, data: Any) -> List[int]:
        # GET INDEX
        index = self.unique_dict.get(data)

        return [index]

    def get_num_feat(self):
        return self.num_feat


if __name__ == "__main__":
    one_hot_encode = LabelEncode(
        stat_dict={"unique": {"unique": {"0": 12, "1": 24}, "uniqueCount": 2}}, arg_list=[]
    )

    print(one_hot_encode.apply("0"))
    print(one_hot_encode.apply("1"))
