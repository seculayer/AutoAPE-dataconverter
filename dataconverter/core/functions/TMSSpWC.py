# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.

# -- python basic
import json
from typing import Tuple

# -- data converter
from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants
from dataconverter.core.functions.SpWCAbstract import SpWCAbstract
import re

# class : TMSSpWC
class TMSSpWC(SpWCAbstract):
    VERSION = "1.0"

    def __init__(self, **kwargs):
        ConvertAbstract.__init__(self, **kwargs)

        try:
            self.max_len = int(self.arg_list[0])
        except:
            self.max_len = 1

        self.special_word, self.special_regex = self._load_special_word_dict()

        self.max_val = 255.0
        self.padding_val = len(self.special_word.keys()) + 1
        self.methods = ['GET /', 'POST /', 'HEAD /', 'PUT /', 'DELETE /']

        self.test = kwargs.get("test", False)
        if self.test:
            self.length_stat = dict()

    # --- OVERRIDE 2023/11/06
    # HEADER REMOVE
    def apply(self, data) -> list():
        # remove header
        for m in self.methods:
            if m in data:
                data = data[re.search(m, data).start():]
            else:
                continue
        return super(TMSSpWC, self).apply(data)

    def remove_common_word(self, data) -> list:
        # remove header
        for m in self.methods:
            if m in data:
                data = data[re.search(m, data).start():]
            else:
                continue
        return super(TMSSpWC, self).remove_common_word(data)
    # --- OVERRIDE END 2023/11/06

    @classmethod
    def _load_special_word_dict(cls) -> Tuple[dict, dict]:
        keyword_map_path = "{}/{}".format(
            Constants.DIR_RESOURCES,
            f"TMS_keywords_map_v{cls.VERSION}.json"
        )
        f = open(keyword_map_path, "r")
        special_dict = json.loads(f.read())
        f.close()
        return special_dict["special_keyword"], {}

    def _convert_value(self, data):
        result = list()
        for word in data:
            value = self.special_word.get(word, None)
            if value is not None:
                result.append(float(int(value.get("value", 0))) / self.padding_val * self.max_val)

        if self.test:
            len_res = len(result)
            if self.length_stat.get(len_res, None) is None:
                self.length_stat[len_res] = 1
            else:
                self.length_stat[len_res] += 1
        return result

    def _padding_proc(self, data):
        curr_len = len(data)
        # over
        if curr_len > self.max_len:
            return data[0:self.max_len]
        elif curr_len < self.max_len:
            data += [self.max_val] * (self.max_len - curr_len)
            return data
        else:
            return data


if __name__ == '__main__':
    str_data_list = list()
    str_data_list.append("GET /adv/?rad_nw=jp&rad_site=ichiba&rad_cont=superdeal&rad_type=img_thumb&rad_pos"
                         "=superdeal_kotei_24&rad_total=2&callback=jQuery17205782481206032573_1610426172610&_=string"
                         "-length%28//user%5Bposition%28%29%3D1%5D/child%3A%3Anode%28%29%5Bposition%28%29%3D1%5D%29 "
                         "HTTP/1.1\" 200 1372 \"Mozilla/5.0 (Linux; Android 5.0.1; LG-F350S Build/LRX21Y) "
                         "AppleWebkit/537.36 (KHTML, like Gecko) Chrome/44.0.240.133 Mobile Safari/537.36\"")

    cvt_fn = TMSSpWC(arg_list=[200], stat_dict=dict())

    for str_data in str_data_list:
        print(cvt_fn.apply(str_data))
        print("".join(cvt_fn.remove_common_word(str_data)))
