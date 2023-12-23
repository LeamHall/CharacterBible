# name    :  test/functional_tests.py
# version :  0.0.1
# date    :  20231205
# author  :  Leam Hall
# desc    :  Functional tests for Character Bible

import unittest
from selenium import webdriver


class TestBasePage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://10.0.0.10:8000")

    def tearDown(self):
        self.browser.quit()

    def test_base_page_hello(self):
        text = self.browser.page_source
        self.assertIn("Hello", text)
