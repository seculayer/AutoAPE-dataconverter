# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from dataconverter.core.ConvertAbstract import ConvertAbstract
from pycmmn.tools.DynamicClassLoader import DynamicClassLoader
from dataconverter.core.ConvertFunctionInfo import ConvertFunctionInfo
from dataconverter.common.Common import Common


class ConvertFactory(object):

    @classmethod
    def create_cvt_fn(cls, cvt_fn_info: ConvertFunctionInfo, cvt_dict, logger) -> ConvertAbstract:
        fn_tag = cvt_fn_info.get_fn_str()
        class_nm = cvt_dict.get(
            fn_tag, {'not_normal': {"class": "NotNormal"}}) \
            .get("class", "NotNormal")

        fn_args = cvt_fn_info.get_fn_args()
        stat_dict = cvt_fn_info.get_stat_dict()

        try:
            return DynamicClassLoader.load_multi_packages(
                packages=Common.CNVRTR_PACK_LIST,
                class_nm=class_nm,
                logger=logger
            )(arg_list=fn_args, stat_dict=stat_dict, logger=logger)
        except Exception as e:
            return DynamicClassLoader.load_multi_packages(
                packages=Common.CNVRTR_PACK_LIST,
                class_nm="NotNormal",
                logger=logger
            )(arg_list=list(), stat_dict=dict(), logger=logger)


if __name__ == '__main__':
    pass
