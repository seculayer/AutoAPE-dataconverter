# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

import base64
from typing import Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class DecodeBase64(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_STRING

    def apply(self, data: Union[str, bytes, bytearray]) -> List[str]:
        charset = 'utf-8'

        if not isinstance(data, (str, bytes, bytearray)):
            return [""]

        if not data.strip():
            return [""]

        if isinstance(data, str):
            data = data.encode(charset)

        result = base64.b64decode(data)
        return [result.decode(charset)]


if __name__ == "__main__":
    _str = "Hello World"
    str_encode = base64.b64encode(_str.encode("UTF-8"))
    print(str_encode)
    print(DecodeBase64(stat_dict=None, arg_list=None).apply(str_encode))
