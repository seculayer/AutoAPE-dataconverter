# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team
######################################################################################

from __future__ import annotations
from typing import List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class ToUpperCase(ConvertAbstract):
    """문자열을 대문자화하는 함수

    Implement com.seculayer.ape.cnvrtr.function.logic.ToUpperCase.java as Python
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_STRING

    def apply(self, data: str) -> List[str]:
        if self._isBlank(data):
            return [""]

        return [data.upper()]


if __name__ == "__main__":
    string = "Seculayer"
    print(ToUpperCase(stat_dict=None, arg_list=[]).apply(string))
