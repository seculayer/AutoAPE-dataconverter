# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations

from typing import Any, Optional

from dataconverter.core.ConvertAbstract import ConvertAbstract


class SignEncode(ConvertAbstract):
    _max: int = 1
    _min: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, data: Any) -> list[Optional[int]]:
        if data not in (self._min, self._max):
            self.LOGGER.error("invalid input value")
            return [None]

        if data == 0:
            return [-1]

        return [1]
