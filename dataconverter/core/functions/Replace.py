# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

from typing import Any, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class Replace(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_STRING

    def apply(self, data: Any) -> List[str]:
        result = ""

        # check blank
        if self._isBlank(data):
            return [result]

        str_old = ""
        str_new = ""
        if len(self.arg_list) >= 2:
            str_old = self.arg_list[0]
            str_new = self.arg_list[1]
        else:
            return [result]

        result = data.replace(str_old, str_new)

        return [result]


if __name__ == "__main__":
    _str = "Korea"
    print(Replace(stat_dict=None, arg_list=["K", "C"]).apply(_str))
