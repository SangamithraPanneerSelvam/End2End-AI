import requests
import scrapy
import selenium
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

class wedding_url():

    def __init__(self):
        self.url=""

    def selenium(self,url):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(
            executable_path=r"C://Users//Sangamithra//Desktop//project//geckodriver-v0.30.0-win64//geckodriver.exe",
            options=options,
        )
        self.driver.get(url)
        time.sleep(3)
        html = self.driver.page_source
        
        # html = BeautifulSoup(html)
        return html
    
    def selection(self):
        i=0
        data=[]
        self.list_of_hrefs = []
        """Since the page contains large amount of pages and this is to demonstarte the code, I have introduced a for loop and selecting the url by rule based.
        The page contains 20,000 + data. Hence here I am focusing on only 1000 datapoints. If you want to collect all the data, then uncomment the 'next_page' line in the function: parse"""
        
        for i in range(0,1000,25):
            self.url='https://cost.wedding.report/index.cfm/action/costest.latest?nr={}&filter='.format(i)
            self.parse(self.url) 
            # print(info)
            # data.append(info)
         
        data_df = pd.DataFrame(self.list_of_hrefs)
        data_df.to_csv(r"C://Users//Sangamithra//Desktop//project//wedding_url.csv")   

        
        

    def parse(self,url):
        dict = {}
        
        # self.list_of_hrefs = []

        soup = self.selenium(url)
        self.response = Selector(text=soup)
        content_blocks = self.driver.find_elements_by_class_name("card-body")

        block=content_blocks[0]
        elements = block.find_elements_by_tag_name("a")
        for el in elements:
            self.list_of_hrefs.append(el.get_attribute("href"))
        
        self.driver.close()
        
       
        
        
        """Use this when you want to extract all the pages."""
        # next_page=self.response.xpath('//a[@class="btn btn-primary m-2"]/@href').get(
        # if next_page:
        #     # yield scrapy.Request(url=next_page,callback=self.parse)
        #     self.parse(url=next_page)
        # else:
            # self.driver.close()
            
    
        


if __name__ == "__main__":
    obj = wedding_url()
    obj.selection()
    # obj.parse()

