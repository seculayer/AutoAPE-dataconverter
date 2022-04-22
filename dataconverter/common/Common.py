#  -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
#  Powered by Seculayer © 2021 Service Model Team, R&D Center.
#

from pycmmn.Singleton import Singleton


class Common(object, metaclass=Singleton):
    CNVRTR_PACK_LIST = [
        "dataconverter.core.functions"
    ]


if __name__ == '__main__':
    Common()
