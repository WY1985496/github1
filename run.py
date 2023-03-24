# -*- coding: utf-8 -*-
# @time: 2023-02-24 16:51
import os
import pytest


if __name__ == '__main__':
    pytest.main(['./sendhttp/test_sendhttp.py',
                 '--html=./htmlreport/report.html',
                 '--alluredir', './report', '--clean-alluredir'])
    os.system('allure generate ./report -o ./allure_report/ --clean')