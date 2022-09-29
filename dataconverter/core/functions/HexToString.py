# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

import binascii
from typing import Union

from dataconverter.core.ConvertAbstract import ConvertAbstract


class HexToString(ConvertAbstract):
    _charset: str = "utf-8"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if (
            len(self.arg_list) > 1
            and isinstance(self.arg_list[0], str)
            and not self._isBlank(self.arg_list[0])
        ):
            self._charset = self.arg_list[0].strip()

    def apply(self, data: Union[str, bytes]) -> list[str]:
        if self._isBlank(data):
            return [""]

        # init charset
        if not self._isBlank(self._charset):
            self._charset = "UTF-8"

        # check string
        if isinstance(data, str):      
            data = data.encode(self._charset)

        try:
            result = binascii.unhexlify(data)
            return [result.decode(self._charset)]
        except Exception as e:
            self.LOGGER.error(e)
            return [""]


if __name__ == "__main__":
    _str = "68656c6c6f"  # hello to hex
    print(HexToString(stat_dict=None, arg_list=["UTF-8"]).apply(_str))
