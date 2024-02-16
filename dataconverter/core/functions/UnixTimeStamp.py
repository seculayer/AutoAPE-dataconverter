# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team
from __future__ import annotations

from datetime import datetime
from typing import SupportsInt, Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class UnixTimeStamp(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_STRING

    def apply(self, data: Union[int, str, SupportsInt]) -> List[str]:
        if self._isBlank(data):
            return [""]

        ts = int(data)
        if ts < 0:
            return ['']

        return [datetime.utcfromtimestamp(ts).strftime("%Y%m%d%H%M%S")]


if __name__ == "__main__":
    _str = "Hello World"
    print(UnixTimeStamp().apply(_str))
