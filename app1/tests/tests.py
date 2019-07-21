from django.test import TestCase
from django.test.client import RequestFactory
from app1.views.index import hello


class AppTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_func(self):
        print("Run testcase...")
        request = self.factory.get('/app')
        hello(request)
