"""
让 setup.py 支持 Django test cases
"""
import os, sys
from django.test.utils import get_runner
from django.conf import settings

import DjangoExample.settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoExample.settings'
test_dir = os.path.dirname(__file__) + "/../app1/tests"
sys.path.insert(0, test_dir)


def run_tests():
    """ 获得 Django test runner """
    test_runner = get_runner(settings)

    """ 执行 test runner"""
    report = test_runner([], verbosity=1, interactive=True)

    sys.exit(report)


if __name__ == '__main__':
    run_tests()
