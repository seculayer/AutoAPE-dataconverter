# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team


from __future__ import annotations

import string
from typing import Union

from dataconverter.core.ConvertAbstract import ConvertAbstract


class BasicNormal(ConvertAbstract):
    _max: int = 32767
    _min: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(
        self, data: Union[int, float, str, bytes, bytearray]
    ) -> list[Union[str, float]]:
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
        result: Union[float, str] = ""
        try:
            result = (float(data) - self._min) / norm
        except Exception as e:
            self.LOGGER.error(e)

        # List return
        return [result]


if __name__ == "__main__":
    _str = "Hello World"
    basic_normal = BasicNormal()
    print(basic_normal.apply(_str))
