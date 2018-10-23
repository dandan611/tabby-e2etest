import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestLoginTest(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280,1024')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://10.0.2.2:18000/admin")

    def teardown_method(self):
        self.driver.close()

    def test_access_admin_site(self):
        self.driver.save_screenshot('screen_admin_site.png')
