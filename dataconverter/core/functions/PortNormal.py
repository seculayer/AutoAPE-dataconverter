# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations
from typing import Optional, SupportsFloat, Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class PortNormal(ConvertAbstract):
    _max: int = 65535
    _min: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_FLOAT

    def apply(self, data: Union[SupportsFloat, str, float]) -> List[Optional[float]]:
        norm = self._max - self._min

        # Normalization
        result = (float(data) - self._min) / norm
        # temp_result = float(data) / 65535

        # List return
        return [result]


if __name__ == "__main__":
    port_num = "8080"
    port_normal = PortNormal()
    print(port_normal.apply(data=port_num))
