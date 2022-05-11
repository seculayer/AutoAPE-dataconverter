# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2017 AI-TF Team

from __future__ import annotations

import math
from typing import SupportsFloat, Union

from dataconverter.core.ConvertAbstract import ConvertAbstract


class DecimalScaleNormal(ConvertAbstract):
    _max: int = 32767

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, data: Union[str, float, SupportsFloat]) -> list[float]:
        length = (math.log10(self._max) + 1) // 1
        try:
            return [float(data) / math.pow(10, length)]
        except Exception as e:
            self.LOGGER.error(str(e))
            return [0.0]


if __name__ == "__main__":
    val = 2543
    decimal_scale = DecimalScaleNormal()
    print(decimal_scale.apply(data=val))
