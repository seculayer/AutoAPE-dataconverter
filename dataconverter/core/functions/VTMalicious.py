# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
import json

from dataconverter.core.ConvertAbstract import ConvertAbstract


class VTMalicious(ConvertAbstract):
    def __init__(self, **kwargs):
        super(VTMalicious, self).__init__(**kwargs)

        self.num_feat = 1

    def apply(self, data) -> list:
        try:
            if isinstance(data, list):
                try:
                    return [float(json.loads(data[0]).get("malicious"))]
                except json.decoder.JSONDecodeError:
                    rpl_data = data[0].replace('\'', '"')
                    return [float(json.loads(rpl_data).get("malicious"))]
        except Exception as e:
            return [0.0]
        return [0.0]

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass


if __name__ == '__main__':
    _data = [
        "{\"malicious\":0,\"undetected\":11,\"suspicious\":0,\"harmless\":84,"
        "\"timeout\":0}"]

    cvt = VTMalicious()
    print(cvt.apply(_data))
