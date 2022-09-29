# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations

from dataconverter.core.ConvertAbstract import ConvertAbstract


class IPNormal(ConvertAbstract):
    _max: int = 255
    _min: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 4

    def apply(self, data: str) -> list[float]:
        if not isinstance(data, (str, bytes)):
            return [0.0, 0.0, 0.0, 0.0]

        ip_split = data.split(".")
        if len(ip_split) != self.num_feat:
            return [0.0, 0.0, 0.0, 0.0]

        norm = self._max - self._min
        try:
            return [(float(ip) - self._min) / norm for ip in ip_split]
        except Exception as e:
            # print log for error
            self.LOGGER.error(str(e))
            return [0.0, 0.0, 0.0, 0.0]


if __name__ == "__main__":
    ip_arr = "192.168.2.236"
    ipnormal = IPNormal()
    print(ipnormal.apply(ip_arr))
