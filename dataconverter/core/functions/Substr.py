# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

from dataconverter.core.ConvertAbstract import ConvertAbstract


class Substr(ConvertAbstract):
    _start_index: int = 0
    _end_index: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if len(self.arg_list) >= 2:
            self._start_index = int(self.arg_list[0])
            self._end_index = int(self.arg_list[1])

    def apply(self, data: str) -> list[str]:
        result = ""

        # check blank
        if self._isBlank(data):
            return [result]

        if self._start_index > len(data):
            self._start_index = 0
        if self._end_index > len(data):
            self._end_index = len(data)

        if self._end_index == 0:
            result = data[self._start_index :]
        else:
            result = data[self._start_index : self._end_index]

        return [result]


if __name__ == "__main__":
    _str = "Korea"
    print(Substr(arg_list=[0, 1]).apply(_str))
