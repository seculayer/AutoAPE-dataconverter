# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

import base64
from typing import Union

from dataconverter.core.ConvertAbstract import ConvertAbstract


class DecodeBase64(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, data: Union[str, bytes, bytearray]) -> list[str]:
        charset = 'utf-8'

        if not isinstance(data, (str, bytes, bytearray)):
            return [""]

        if not data.strip():
            return [""]

        if isinstance(data, str):
            data = data.encode(charset)

        try:
            result = base64.b64decode(data)
            return [result.decode(charset)]
        except Exception as e:
            self.LOGGER.error(e)
            return [""]


if __name__ == "__main__":
    _str = "Hello World"
    str_encode = base64.b64encode(_str.encode("UTF-8"))
    print(str_encode)
    print(DecodeBase64(stat_dict=None, arg_list=None).apply(str_encode))
