# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
import json
from typing import List, Dict

from dataconverter.common.Constants import Constants
from dataconverter.core.ConvertAbstract import ConvertAbstract


class DGAChar2IDX(ConvertAbstract):
    """
    DGA용 도메인 데이터 변환함수
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_len = 28
        self.num_feat = self.max_len
        self.return_type = Constants.RETURN_TYPE_FLOAT
        self.padding_val: float = 0.

        char_map_path = "{}/{}".format(Constants.DIR_RESOURCES, "CHAR2IDX_DGA.json")
        f = open(char_map_path, "r")
        self.idx_dict: Dict = json.loads(f.read())
        f.close()

    def apply(self, data) -> list:
        data = self._convert_value(data)
        data = self._padding_proc(data)
        return data

    def processConvert(self, data):
        return self.apply(data)

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass

    def _convert_value(self, data: str) -> List:
        results = list()
        for c in data:
            value = self.idx_dict.get(c, None)
            if value is not None:
                results.append(float(value))
        return results

    def _padding_proc(self, data: List):
        curr_len = len(data)
        # over
        if curr_len > self.max_len:
            return data[0:self.max_len]
        elif curr_len < self.max_len:
            data += [self.padding_val] * (self.max_len - curr_len)
            return data
        else:
            return data


if __name__ == '__main__':
    converter = DGAChar2IDX()
    domain_data = "www.google.com"
    print(converter.apply(domain_data))
