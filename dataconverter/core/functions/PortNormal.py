# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations

from typing import Optional, SupportsFloat, Union

from dataconverter.core.ConvertAbstract import ConvertAbstract


class PortNormal(ConvertAbstract):
    _max: int = 65535
    _min: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, data: Union[SupportsFloat, str, float]) -> list[Optional[float]]:
        norm = self._max - self._min
        result = None
        try:
            # Normalization
            result = (float(data) - self._min) / norm
            # temp_result = float(data) / 65535
        except Exception as e:
            # print log for error
            self.LOGGER.error(str(e))

        # List return
        return [result]


if __name__ == "__main__":
    port_num = "8080"
    port_normal = PortNormal()
    print(port_normal.apply(data=port_num))
