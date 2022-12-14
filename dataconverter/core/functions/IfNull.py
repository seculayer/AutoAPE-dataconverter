# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

from typing import Any

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class IfNull(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._replace = self.arg_list[0]
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_STRING

    def apply(self, data: Any) -> list:

        # check blank
        if self._isBlank(data):
            return [self._replace]
        else:
            return [data]


if __name__ == "__main__":
    _str = ""
    print(IfNull(stat_dict=None, arg_list=["A"]).apply(_str))
