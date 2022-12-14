# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

import hashlib
from typing import List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class StringToMD5(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_STRING

    def apply(self, data: str) -> List[str]:
        result = ""

        # check blank
        if self._isBlank(data):
            return [result]

        result = self._str_to_md5hash(data)

        return [result]

    @staticmethod
    def _str_to_md5hash(s: str) -> str:
        m = hashlib.md5()
        m.update(s.encode("UTF-8"))
        return m.hexdigest()


if __name__ == "__main__":
    string = "Korea"
    print(StringToMD5().apply(string))
