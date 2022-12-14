# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations
from typing import Any, Optional, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class SignEncode(ConvertAbstract):
    _max: int = 1
    _min: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_INT

    def apply(self, data: Any) -> List[Optional[int]]:
        if data not in (self._min, self._max):
            return [0]

        if data == 0:
            return [-1]

        return [1]
