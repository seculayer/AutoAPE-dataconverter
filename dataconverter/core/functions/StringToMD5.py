# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

import hashlib
from typing import Union

from dataconverter.core.ConvertAbstract import ConvertAbstract


class StringToMD5(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, data: str) -> list[str]:
        result = ""

        # check blank
        if self._isBlank(data):
            return [result]

        result = self._strToMD5hash(data)

        return [result]

    def _strToMD5hash(self, string: str) -> str:
        try:
            m = hashlib.md5()
            m.update(string.encode("UTF-8"))
            return m.hexdigest()
        except Exception as e:
            self.LOGGER.error(e)
            return string


if __name__ == "__main__":
    string = "Korea"
    print(StringToMD5().apply(string))
