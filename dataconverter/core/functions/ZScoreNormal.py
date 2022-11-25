# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2017 AI-TF Team

from __future__ import annotations
from typing import List

from dataconverter.core.ConvertAbstract import ConvertAbstract


class ZScoreNormal(ConvertAbstract):
    # mean: float
    # stddev: float

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            # the mean of the normal distribution
            self.mean = float(self.stat_dict["avg"])
            # the standard deviation of the normal distribution
            self.stddev = float(self.stat_dict["stddev"])
        except:
            self.mean = 0
            self.stddev = 0

    def apply(self, data: float) -> List[float]:
        try:
            if self.stddev == 0:
                self.stddev = 1
            return [(float(data) - float(self.mean)) / float(self.stddev)]
        except Exception as e:
            return [0.0]


if __name__ == "__main__":
    val = 2
    zscr_normal = ZScoreNormal(stat_dict={"avg": 1, "stddev": 0.1})
    print(zscr_normal.apply(val))
