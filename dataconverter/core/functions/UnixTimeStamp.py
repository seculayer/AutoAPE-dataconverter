# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team
from __future__ import annotations

from datetime import datetime
from typing import SupportsInt, Union

from dataconverter.core.ConvertAbstract import ConvertAbstract


class UnixTimeStamp(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, data: Union[int, str, SupportsInt]) -> list[str]:
        if self._isBlank(data):
            return [""]

        try:
            ts = int(data)
            if ts < 0:
                return ['']

            return [datetime.utcfromtimestamp(ts).strftime("%Y%m%d%H%M%S")]
        except Exception as e:
            self.LOGGER.error(e)
            return [""]


if __name__ == "__main__":
    _str = "Hello World"
    print(UnixTimeStamp().apply(_str))
