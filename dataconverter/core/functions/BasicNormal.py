# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team


from __future__ import annotations

import string
from typing import Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class BasicNormal(ConvertAbstract):
    _max: int = 32767
    _min: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_FLOAT

    def apply(
        self, data: Union[int, float, str, bytes, bytearray]
    ) -> List[Union[str, float]]:
        if not data:
            data = 0

        if isinstance(data, str) and data.isalpha():
            lower_text = data.replace(" ", "").lower()
            data = sum(map(lambda x: string.ascii_lowercase.find(x), lower_text))

        if isinstance(data, (bytes, bytearray)) and data.isalpha():
            lower_bytes = data.replace(b" ", b"").lower()
            data = sum(
                map(lambda x: string.ascii_lowercase.encode().find(x), lower_bytes)
            )

        norm = self._max - self._min
        result: Union[float] = (float(data) - self._min) / norm

        # List return
        return [float(result)]


if __name__ == "__main__":
    _str = "Hello World"
    basic_normal = BasicNormal()
    print(basic_normal.apply(_str))
