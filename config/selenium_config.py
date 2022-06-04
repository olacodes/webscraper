import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

env = environ.Env()

class Selenium:
    @classmethod
    def chrome_driver(cls):
        op = webdriver.ChromeOptions()
        op.add_argument('--ignore-ssl-errors=yes')
        op.add_argument('--ignore-certificate-errors')
        op.add_argument('--disable-dev-shm-usage')

        # configure path of downloaded pdf file
        p = {"download.default_directory": "/Downloads"}
        op.add_experimental_option("prefs", p)

        driver = webdriver.Remote(command_executor=env('SELENIUM_ADDRESS'),
                                  options=op)
        return driver
    
    @classmethod
    def firefox_driver(cls):
        # Configuration for firefox driver goes here
        pass
