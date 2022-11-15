# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations

import logging
from logging import Logger
from typing import Union


class ConvertAbstract(object):
    num_feat: int
    LOGGER: Logger
    stat_dict: dict
    arg_list: list
    split_separator: str
    max_len: int
    padding_val: int
    error_log_flag: bool

    def __init__(
        self,
        arg_list: list = [],
        stat_dict: dict = {},
        logger: Logger = logging.getLogger(),
    ):
        self.num_feat = 1
        self.LOGGER = logger
        self.stat_dict = stat_dict
        self.arg_list = arg_list

        self.split_separator = ","
        self.max_len = 50
        self.padding_val = 255
        self.error_log_flag = False

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

            res_val_lenth = len(arr_ret)

            if res_val_lenth < self.max_len:
                padding = [self.padding_val] * (self.max_len - res_val_lenth)
                arr_ret.extend(padding)
                return arr_ret

            return arr_ret[: self.max_len]

        except Exception as e:
            self.LOGGER.error("cvt Exception: {}".format(e))

        return arr_ret

    def get_num_feat(self):
        return self.num_feat

    def reverse(self, data, original_data):
        raise NotImplementedError

    def get_original_idx(self, cvt_data, original_data):
        raise NotImplementedError

    @staticmethod
    def _isBlank(_str: Union[str, bytes]) -> bool:
        return not (_str and isinstance(_str, (str, bytes)) and _str.strip())
