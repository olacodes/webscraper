import environ

from django.views import View
from django.http import HttpResponse
from selenium.webdriver.common.by import By
from celery import group, shared_task

from config.celery_app import app
from config.selenium_config import Selenium
from webscraper.utils import PDFwriter

env = environ.Env()
WEB_URL = "https://www.greenbooklive.com/search/companysearch.jsp?from=0&partid=10028&sectionid=0&companyName=&productName=&productType=&certNo=&regionId=0&countryId=0&addressPostcode=&certBody=&id=260&results_pp=1000&sortResultsComp"



class WebScraperView(View):
    def get(self, request):
        # Instantiate selenium chrome_driver
        driver = Selenium.chrome_driver()
        # url launch
        driver.get(WEB_URL)
        # browser maximize
        driver.maximize_window()
        
        pdfs = []
        counter = 1
        
        # Get the length of the page
        pages = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div/div[2]')
        pages_len = len(pages.find_elements_by_xpath(".//*"))
        
        for _ in range(pages_len):
            table = driver.find_element(By.XPATH, '//*[@id="search-results"]')
            
            # Fetch pdf contents for each row
            for row in table.find_elements_by_css_selector('tr'):
                if counter > 1:
                    pdf_links = driver.find_elements(
                        By.XPATH, f'//*[@id="search-results"]/tbody/tr[{counter}]/td[4]/a')
                    pdf_urls = [pdf_link.get_attribute(
                        'href') for pdf_link in pdf_links]
                    pdfs.extend(pdf_urls)
                counter += 1
            counter = 1
            # Select the next page
            next_page = driver.find_element_by_xpath(
                '//*[@id="container"]/div/div/div/div[2]/a')
            next_page.click()
            
            # implicit wait for next page to load
            driver.implicitly_wait(0.1)

        # print(pdfs)
        print(len(pdfs))

        jobs = group(PDFwriter.s(url) for url in pdfs)
        result = jobs.apply_async()
        print("Done")

        driver.close()
        driver.quit()
        return HttpResponse("Hello")
