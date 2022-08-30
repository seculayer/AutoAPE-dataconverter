# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

import json
from typing import Tuple

from dataconverter.common.Constants import Constants
from dataconverter.core.functions.SpWCAbstract import SpWCAbstract


class XSSpWC(SpWCAbstract):
    @staticmethod
    def _load_special_word_dict() -> Tuple[dict, dict, dict]:
        keyword_map_path = "{}/{}".format(Constants.DIR_RESOURCES, "XS_keywords_map.json")
        f = open(keyword_map_path, "r")
        tmp_dict = json.loads(f.read())
        special_dict = tmp_dict[0]
        reverse_dict = tmp_dict[1]
        f.close()
        return special_dict, reverse_dict, {}

    def processConvert(self, data):
        return self.apply(data)


if __name__ == '__main__':
    str_data = "/main/product/product_view.asp %00--%3E%3C/script%3E%3Cscript%3Ealert(313)%3C/script%3E?seq=87 Mozilla/5.0+(Windows+NT+6.1;+WOW64;+Trident/7.0;+rv:11.0)+like+Gecko"
    cvt_fn = XSSpWC(arg_list=[50, 255], stat_dict=dict())
    print(cvt_fn.apply(str_data))
    print("".join(cvt_fn.remove_common_word(str_data)))

