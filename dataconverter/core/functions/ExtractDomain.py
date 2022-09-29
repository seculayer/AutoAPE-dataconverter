# -*- coding: utf-8 -*-
# Author : Seungyeon Jo
# e-mail : syjo@seculayer.co.kr
# Powered by Seculayer © 2018 AI-Core Team

from __future__ import annotations

import re

from dataconverter.core.ConvertAbstract import ConvertAbstract


class ExtractDomain(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, data) -> list[str]:
        # check blank
        if not isinstance(data, str) and self._isBlank(data):
            return [""]

        # 0. Cut Parameter
        domain_regex = re.compile(
            r"(\?.+)|([https]{4,5}://)", flags=re.ASCII | re.IGNORECASE
        )
        cutDomain = domain_regex.sub("", data)
        # 1. IP is return
        if len(re.sub("[0-9.]", "", cutDomain)) == 0:
            return [cutDomain]

        arr = cutDomain.split(".")  # if cutDomain is empty return `[""]`.
        arr_length = len(arr)

        # 2. if domain is .com/.net
        try:
            if cutDomain.endswith(".com") or cutDomain.endswith(".net"):
                return [".".join(arr[-2:])]
        except Exception as e:
            self.LOGGER.error(e)

        # 3. if .(dot) is one
        if arr_length == 2:
            return [cutDomain]

        # 4. if .(dot) is two
        try:
            if arr_length == 3:
                return [".".join(arr[-2:])]
        except Exception as e:
            self.LOGGER.error(e)

        # 5. if .(dot) is three more
        try:
            if arr_length >= 4:
                return [".".join(arr[-3:])]
        except Exception as e:
            self.LOGGER.error(e)

        return [cutDomain]


if __name__ == "__main__":
    _str = "http://www.seculayer.com/index.html?arg1=0"
    print(ExtractDomain(stat_dict=None, arg_list=None).apply(_str))
