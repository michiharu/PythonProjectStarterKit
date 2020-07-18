from unittest import TestCase

from package.hello_module import hello


class TestHello(TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "hello world!")
