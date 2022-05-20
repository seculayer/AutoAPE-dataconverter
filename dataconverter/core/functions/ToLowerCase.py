# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team
######################################################################################

from __future__ import annotations

from dataconverter.core.ConvertAbstract import ConvertAbstract


class ToLowerCase(ConvertAbstract):
    """문자열을 소문자화 하는 함수

    Implement com.seculayer.ape.cnvrtr.function.logic.ToLowerCase.java as Python
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, data: str) -> list[str]:
        if self._isBlank(data):
            return [""]

        return [data.lower()]


if __name__ == "__main__":
    string = "Seculayer"
    print(ToLowerCase(stat_dict=None, arg_list=None).apply(string))
