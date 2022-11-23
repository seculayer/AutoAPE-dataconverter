# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
import json
from logging import Logger

import numpy as np

from dataconverter.core.ConvertAbstract import ConvertAbstract


# DNS VT Meta
class VTPopularityRank(ConvertAbstract):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.site_key = self._site_key_map(self.arg_list[0])

    @staticmethod
    def _site_key_map(site_key):
        site_dict = {
            "majestic": "Majestic",
            "cisco": "Cisco Umbrella",
            "statvoo": "Statvoo",
            "alexa": "Alexa",
            "quantcast": "Quantcast"
        }
        return site_dict.get(site_key, None)

    def apply(self, data) -> list:
        try:
            if isinstance(data, list):
                try:
                    data_dict = json.loads(data[0])
                except json.decoder.JSONDecodeError:
                    rpl_data = data[0].replace('\'', '"')
                    data_dict = json.loads(rpl_data)

                return [int(data_dict.get(self.site_key, {}).get("rank", 9999999))]
        except Exception as e:
            return [0.0]

        return [0.0]

    def processConvert(self, data):
        return self.apply(data)

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = {"query": "aka.ms", "query_ip": "104.87.239.185", "tag_ctas_ti": "N", "anal_simhash_score": 0.0,
            "mal_similr:": "N", "anal_jaro_score": 0.47, "anal_leven_score": 8.0,
            "vt_whois_createDate": "2011-01-20T16:48:05.686Z", "not_before": ["2022-10-13 21:29:19"],
            "vt_whois_updateDate": "2021-12-13T19:01:59.181Z", "vt_whois_regist_country": "US",
            "dns_recode_type": ["NS", "TXT", "TXT", "NS", "TXT", "NS", "TXT", "SOA", "TXT", "NS", "TXT", "NS", "TXT",
                                "NS", "TXT", "TXT", "NS", "TXT", "TXT", "NS", "A", "TXT"],
            "not_after": ["2023-10-08 21:29:19"], "vt_whois_registrar": "CSC Corporate Domains",
            "malicious": ["{\"malicious\":0,\"undetected\":11,\"suspicious\":0,\"harmless\":84,\"timeout\":0}"],
            "total_votes": ["{\"malicious\":6,\"harmless\":1}"], "popularity_ranks": [
            "{\"Quantcast\":{\"rank\":1088,\"timestamp\":1585841763},\"Cisco Umbrella\":{\"rank\":6967,\"timestamp\":1667321881},\"Alexa\":{\"rank\":189512,\"timestamp\":1667235484},\"Statvoo\":{\"rank\":10679,\"timestamp\":1667408281},\"Majestic\":{\"rank\":1250,\"timestamp\":1667408281}}"],
            "resolutions_count": ["200"], "vt_whois_expiryDate": "2023-01-20T16:48:05.705Z",
             "dns_recode_recode_ttl": ["521", "300", "300", "521", "300", "521", "300", "21600", "300", "521", "300",
                                      "521", "300", "521", "300", "300", "521", "300", "300", "521", "12", "300"]}

    converter = VTPopularityRank(arg_list=["alexa"], stat_dict={}, logger=None)
    print(converter.apply(_data.get("popularity_ranks")))
