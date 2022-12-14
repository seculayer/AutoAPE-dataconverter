# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : manki.baek@seculayer.com
# Powered by Seculayer © 2017-2018 AI Core Team, Intelligence R&D Center.

from __future__ import annotations
from typing import Sequence, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class String2ASCII(ConvertAbstract):
    seq_len: int

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_len = int(self.arg_list[0])
        self.seq_len = int(self.arg_list[1])
        self.num_feat = self.max_len
        self.return_type = Constants.RETURN_TYPE_FLOAT

    def apply(self, data: Sequence[str]) -> List[Sequence[float]]:
        try:
            feature = []
            for idx, word in enumerate(data):
                if idx >= self.seq_len:
                    break
                feature.append(self.cvt_ascii(word, self.max_len))

            if len(feature) < self.seq_len:
                interval = self.seq_len - len(feature)
                for idx in range(interval):
                    feature.append([0 for _ in range(self.max_len)])
            return feature

        except Exception as e:
            return [[0.0] * self.max_len] * self.seq_len

    @staticmethod
    def cvt_ascii(data: str, max_length: int) -> Sequence[float]:
        word = []
        for idx, char in enumerate(str(data)):
            if idx >= max_length:
                break

            word.append(ord(char))

        if len(word) < max_length:
            word += [0] * (max_length - len(word))
        return word

    def get_num_feat(self):
        return self.max_len


if __name__ == "__main__":
    # data = "hjg yjhg 6ug679t g6guy g321%!#% $^$Fgsdfha"
    _data = ["0", "53018000", "20140523173202"]
    cvt_fn = String2ASCII(stat_dict=None, arg_list=[5, 3])

    rst = cvt_fn.apply(data=_data)
    print(rst)
    print(len(rst))
