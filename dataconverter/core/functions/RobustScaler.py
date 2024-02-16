# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : manki.baek@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, Intelligence R&D Center.

from __future__ import annotations

from typing import SupportsFloat, Union, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class RobustScaler(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.median = float(self.stat_dict["median"])
            self.quantile_1 = float(self.stat_dict["quantile_1"])
            self.quantile_3 = float(self.stat_dict["quantile_3"])
        except:
            self.median = 0
            self.quantile_1 = 0
            self.quantile_3 = 0
        self.IQR = self.quantile_3 - self.quantile_1
        self.num_feat = 1
        self.return_type = Constants.RETURN_TYPE_FLOAT

    def apply(self, data: Union[SupportsFloat, str, float]) -> List[float]:
        if self.IQR == 0:
            self.IQR = 1
            self.LOGGER.warn("IQR val is zero")
        result = (float(data) - float(self.median)) / float(self.IQR)

        return [result]


if __name__ == "__main__":
    minmax_normalization = RobustScaler(
        stat_dict={"median": 128, "quantile_1": 64, "quantile_3": 192}, arg_list=None
    )
    ip = "192.168.0.256.-128"
    ip_split = ip.split(".")

    for _data in ip_split:
        print(minmax_normalization.apply(data=_data))
