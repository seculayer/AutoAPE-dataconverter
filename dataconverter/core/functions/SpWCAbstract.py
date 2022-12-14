# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.
import math
import urllib.parse as decode
import re
from typing import Tuple, List

from dataconverter.core.ConvertAbstract import ConvertAbstract
from dataconverter.common.Constants import Constants


class SpWCAbstract(ConvertAbstract):
    def __init__(self, **kwargs):
        """
        :param kwargs:
        ConvertAbstract(arg_list, stat_dict)
        kwargs["arg_list"], kwarg["stat_dict"]

        arg_list[0] = max length

        must
        """
        super().__init__(**kwargs)
        try:
            self.max_len = int(self.arg_list[0])
        except:
            self.max_len = 1
        self.num_feat = self.max_len
        self.return_type = Constants.RETURN_TYPE_FLOAT

        """
        special word type : json
        ex)
        {
            "key1" : {"value" : "a", "info1" : ""}, "key2" : {"value" : "b"},
        }
        usage - convert: special_word[key][value]
        usage - get extra info : special_word[key][info1]
        """

        self.special_word, self.reverse_dict, self.special_regex = self._load_special_word_dict()

        """
        arg_list[1] = padding value
        """
        try:
            self.padding_val = int(self.arg_list[1])
        except:
            self.padding_val = 0

    @staticmethod
    def _load_special_word_dict() -> Tuple[dict, dict, dict]:
        raise NotImplementedError

    def apply(self, data) -> list:
        data = self._replace_basic(data)
        data = self._url_decode(data)
        data = self._repl_regex(data)
        data = self._tokenize(data)
        data = self._convert_value(data)
        return self._padding_proc(data)

    def reverse(self, data, original_data) -> List:
        rst_list = list()
        find_from = 0
        original_data = original_data.replace("\\/", "/")
        for _ in range(5):
            original_data = decode.unquote(original_data)
        original_data = original_data.lower()

        for i, feature in enumerate(data):
            if feature == self.padding_val:
                rst_list.append(f"{i}_PADDING")
            else:
                origin_word_list = self.reverse_dict[str(int(feature))]
                min_sidx = math.inf
                accept_token = None
                backup_find_from = find_from
                for word in origin_word_list:
                    search_idx = original_data.find(word, backup_find_from)

                    if min_sidx > search_idx > -1:
                        min_sidx = search_idx
                        find_from = search_idx + len(word)
                        accept_token = word

                if accept_token is not None:
                    rst_list.append(accept_token)
                else:
                    continue

        return rst_list

    def get_original_idx(self, cvt_data, original_data):
        rst_list = list()
        column_list = list()
        find_from = 0
        data = original_data.replace("\\/", "/")
        for _ in range(5):
            data = decode.unquote(data)
        data = data.lower()

        for token in self.reverse(cvt_data, original_data):
            s_idx = data.find(token, find_from)

            if s_idx == -1:
                if "PADDING" not in token:
                    self.LOGGER.error(f"Can't find token : [{token}], original_data : [{data}]")
                continue

            e_idx = s_idx + len(token) - 1
            rst_list.append([s_idx, e_idx])
            find_from = e_idx + 1

        return rst_list, data

    def remove_common_word(self, data) -> list:
        data = self._replace_basic(data)
        data = self._url_decode(data)
        data = self._repl_regex(data)
        data = self._tokenize(data)
        return self._remove_common_word(data)

    @staticmethod
    def _replace_basic(data):
        data = data.replace("\\/", "/")
        data = data.replace("\r\n", " ").replace("\n", " ").replace("\t", " ").replace("  ", " ").replace("  ", " ")
        data = data.replace("CCOMMAA", ",")
        return data

    @staticmethod
    def _url_decode(data):
        try:
            cnt = 0
            val = ""
            while val != data or cnt <= 5:
                val = data
                data = decode.unquote(data.upper())
                cnt += 1
            dec_data = data.lower()
        except Exception as e:
            dec_data = str(data).lower()

        dec_data = dec_data.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
        return dec_data

    def _repl_regex(self, data):
        if len(self.special_regex) > 0:
            for regex in self.special_regex:
                data = re.sub(regex, self.special_regex[regex]["value"], data)

        return data

    @staticmethod
    def _tokenize(data: str) -> list:
        key_set = list(set(re.findall(r'[^a-zA-Z0-9]|[_]', data)))
        for key in key_set:
            if key != " ":
                data = data.replace(str(key), ' ' + str(key) + ' ').replace("  ", " ")
        data = data.strip()
        data = data.split(" ")
        return data

    def _convert_value(self, data):
        result = list()
        for word in data:
            value = self.special_word.get(word, None)
            if value is not None:
                result.append(float(int(value.get("value", 0))))
        return result

    def _remove_common_word(self, data):
        result = list()
        for word in data:
            value = self.special_word.get(word, None)
            if value is not None:
                result.append(word)
        return result

    def _padding_proc(self, data):
        curr_len = len(data)
        # over
        if curr_len > self.max_len:
            return data[0:self.max_len]
        elif curr_len < self.max_len:
            data += [float(self.padding_val)] * (self.max_len - curr_len)
            return data
        else:
            return data

    def processConvert(self, data):
        return self.apply(data)

    def get_num_feat(self):
        return self.max_len
