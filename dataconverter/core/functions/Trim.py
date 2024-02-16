# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations
from typing import List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class Trim(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_STRING

    def apply(self, data: str) -> List[str]:
        if self._isBlank(data):
            return [""]

        return [data.strip()]


if __name__ == "__main__":
    _str = " Aeye-2.0 "
    print(Trim(arg_list=None, stat_dict=None).apply(_str))
