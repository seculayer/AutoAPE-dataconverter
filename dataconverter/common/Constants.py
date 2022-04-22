#  -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
#  Powered by Seculayer © 2021 Service Model Team, R&D Center.

import os

from pycmmn.Singleton import Singleton
from pycmmn.utils.FileUtils import FileUtils
from pycmmn.tools.VersionManagement import VersionManagement


class Constants(object, metaclass=Singleton):
    _working_dir = os.getcwd()

    try:
        VERSION_MANAGER = VersionManagement(app_path=_working_dir)
    except Exception as e:
        # DEFAULT
        VersionManagement.generate(
            version="1.0.0",
            app_path=_working_dir,
            module_nm="dataconverter",
        )
        VERSION_MANAGER = VersionManagement(app_path=_working_dir)
    VERSION = VERSION_MANAGER.VERSION
    MODULE_NM = VERSION_MANAGER.MODULE_NM

    # DIRECTORY SETTING
    DIR_RESOURCES = (
            FileUtils.get_realpath(file=__file__)
            + "/../resources"
    )


if __name__ == "__main__":
    print(Constants.__dict__)
