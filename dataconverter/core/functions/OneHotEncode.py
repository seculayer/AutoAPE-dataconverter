# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, Intelligence R&D Center.

from __future__ import annotations

from typing import Any

from dataconverter.core.ConvertAbstract import ConvertAbstract


class OneHotEncode(ConvertAbstract):
    unique_dict: dict[Any, int]
    unique_count: int

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unique_dict = {}
        self.unique_count = 0

        for idx, key in enumerate(sorted(self.stat_dict.get("unique", {}).keys())):
            self.unique_dict[key] = idx
            self.unique_count += 1

    def apply(self, data: Any) -> list[int]:
        # ZERO
        result: list[int] = [0] * self.unique_count

        # GET INDEX
        index = self.unique_dict.get(data)
        if index:
            result[index] = 1
        else:
            result[0] = 1

        return result

    def get_num_feat(self):
        return self.unique_count


if __name__ == "__main__":
    one_hot_encode = OneHotEncode(
        stat_dict={"unique": "0@COMMA@1", "uniqueCount": 2}, arg_list=[]
    )

    print(one_hot_encode.apply("0"))
    print(one_hot_encode.apply("1"))
