# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, Intelligence R&D Center.

from __future__ import annotations
from typing import Optional, Union, List
import numpy as np

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class MinMaxNormal(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_FLOAT

        try:
            self.max = float(self.stat_dict["basic"]["max"])
            self.min = float(self.stat_dict["basic"]["min"])
        except Exception as e:
            self.max = 0
            self.min = 0

    def apply(self, data: Union[float, str]) -> List[float]:
        norm = self.max - self.min
        # zero-division protection
        if norm == 0:
            # self.LOGGER.warn("Min val is same Max val (Min val == Max val)")
            norm = 1

        # temp_result = float(data) / 255
        # temp_result = (float(data) - self.min) / (self.max - self.min)
        result = (data - self.min) / norm
        return [result]

    def reverse(self, data: float) -> Optional[float]:
        result = None
        norm = self.max - self.min
        # zero-division protection
        if norm == 0:
            # self.LOGGER.warn("Min val is same Max val (Min val == Max val)")
            norm = 1

        try:
            temp_result: np.ndarray = np.array(data, dtype=np.float32) * norm + self.min
            result = temp_result.tolist()
        except Exception as e:
            # print log for error
            self.LOGGER.error(
                "[MinMaxNormal] Convert error !!! self.min : {}, self.max : {}, data : {}".format(
                    self.min, self.max, data
                )
            )
            self.LOGGER.error(e, exc_info=True)

        return result


if __name__ == "__main__":
    minmax_normalization = MinMaxNormal(stat_dict={"min": 0, "max": 255}, arg_list=None)
    ip = "192.168.2.236"
    ip_split = ip.split(".")

    for data in ip_split:
        print(minmax_normalization.apply(data=data))
