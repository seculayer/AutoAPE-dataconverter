# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2017 AI-TF Team

from __future__ import annotations

import math
from typing import SupportsFloat, Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class DecimalScaleNormal(ConvertAbstract):
    _max: int = 32767

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_FLOAT

    def apply(self, data: Union[str, float, SupportsFloat]) -> List[float]:
        length = (math.log10(self._max) + 1) // 1
        return [float(data) / math.pow(10, length)]


if __name__ == "__main__":
    val = 2543
    decimal_scale = DecimalScaleNormal()
    print(decimal_scale.apply(data=val))
