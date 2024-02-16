# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations

import logging
from logging import Logger
from typing import Union

from dataconverter.common.Constants import Constants


class ConvertAbstract(object):
    def __init__(
        self,
        arg_list: list = [],
        stat_dict: dict = {},
        logger: Logger = logging.getLogger(),
    ):
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_INT
        self.LOGGER = logger
        self.stat_dict = stat_dict
        self.arg_list = arg_list

        self.split_separator = ","
        self.max_len = 50
        self.padding_val = 255

    def processConvert(self, data):
        return self.apply(data)

    def apply(self, data) -> list:
        arr_ret = list()

        try:
            arr_ret = self.processConvert(data=data)
            if -1 == self.max_len:
                return arr_ret

            if 1 == self.num_feat:
                self.num_feat = self.max_len

            res_val_length = len(arr_ret)

            if res_val_length < self.max_len:
                padding = [self.padding_val] * (self.max_len - res_val_length)
                arr_ret.extend(padding)
                return arr_ret

            return arr_ret[: self.max_len]

        except Exception as e:
            self.LOGGER.error("cvt Exception: {}".format(e))

        return arr_ret

    def get_num_feat(self) -> int:
        return self.num_feat

    def get_return_type(self) -> str:
        return self.return_type

    def reverse(self, data, original_data):
        raise NotImplementedError

    def get_original_idx(self, cvt_data, original_data):
        raise NotImplementedError

    @staticmethod
    def _isBlank(_str: Union[str, bytes]) -> bool:
        return not (_str and isinstance(_str, (str, bytes)) and _str.strip())
