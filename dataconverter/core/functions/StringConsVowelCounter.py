# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
from dataconverter.core.ConvertAbstract import ConvertAbstract


class StringConsVowelCounter(ConvertAbstract):
    def __init__(self, **kwargs):
        '''
        :param kwargs:
            arg_list[0] = option
                options
                    cows = 모음
                    vowel = 자음
                    all = 모음 + 자음

        '''
        super(StringConsVowelCounter, self).__init__(**kwargs)

        self.option = self.arg_list[0]
        self.cow_dict = {"a": 1, "e": 1, "o": 1, "i": 1, "u": 1}

    def apply(self, data) -> list:
        count = 0
        length = 0
        try:
            for s in data:
                count += self.cow_dict.get(s, 0)
                length += 1
            if self.option == "cows":
                return [count]
            elif self.option == "vowel":
                return [length - count]
            else:
                return [count, length-count]
        except Exception as e:
            return [count, length]

    def processConvert(self, data):
        pass

    def reverse(self, data, original_data):
        pass

    def get_original_idx(self, cvt_data, original_data):
        pass
