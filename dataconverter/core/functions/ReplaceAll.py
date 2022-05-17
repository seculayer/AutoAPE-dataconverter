# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

import re

from dataconverter.core.ConvertAbstract import ConvertAbstract


class ReplaceAll(ConvertAbstract):
    _pattern: str = ""
    _repl: str = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if len(self.arg_list) >= 2:
            self._pattern = self.arg_list[0]
            self._repl = self.arg_list[1]

    def apply(self, data: str) -> list[str]:
        result = ""

        # check blank
        if self._isBlank(data):
            return [result]

        if isinstance(data, (str, bytes)):
            result = re.sub(self._pattern, self._repl, data)

        return [result]


if __name__ == "__main__":
    _str = "Korea"
    print(ReplaceAll(arg_list=["[a-z]", ""]).apply(_str))
