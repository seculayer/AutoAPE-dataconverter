# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

import json
from typing import Tuple

import logging

from dataconverter.common.Constants import Constants
from dataconverter.core.functions.SpWCAbstract import SpWCAbstract


class SISpWC(SpWCAbstract):
    @staticmethod
    def _load_special_word_dict() -> Tuple[dict, dict, dict]:
        keyword_map_path = "{}/{}".format(Constants.DIR_RESOURCES, "SI_keywords_map.json")
        f = open(keyword_map_path, "r")
        tmp_dict = json.loads(f.read())
        special_dict = tmp_dict[0]
        reverse_dict = tmp_dict[1]
        f.close()
        return special_dict, reverse_dict, {}

    def processConvert(self, data):
        return self.apply(data)


if __name__ == '__main__':
    str_data_list = list()
    str_data_list.append("/Fashion/Styleonvmd/Default.asp?YearSeason=2019^Spring&searchPlace=&searchSeason=Spring&searchYear=2019\"&cat /etc/passwd&\"")

    cvt_fn = SISpWC(arg_list=[200, 255], stat_dict=dict(), logger=logging.getLogger())

    for str_data in str_data_list:
        print(cvt_fn.apply(str_data))
        print("".join(cvt_fn.remove_common_word(str_data)))
