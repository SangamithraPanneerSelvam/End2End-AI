import scrapy
import requests
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

"""Wrapping it in a class"""
class wedding_info():

    def __init__(self):
        self.url=" "

    """Selenuim is the driver that takes in the url and retrives an HTMl source file"""
    def selenium(self, url):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(
            executable_path=r"C://Users//Sangamithra//Desktop//project//geckodriver-v0.30.0-win64//geckodriver.exe",
            options=options,
        )
        self.driver.get(url)
        time.sleep(3)
        try:
            
            """This is crucial for this website. It differs for each website. so use it accordingly. This website consist of a survey page blocker that appears
            when trying extract the information. Hence we need to wait few seconds, click a button and move to the next page to extract. Refer Readme for details.
            """
            self.driver.execute_script("window.scrollTo(0,1000)") #you can make an adjust 800 or 1000 
            nextButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@role='button']")))
            nextButton.click()
            # print(nextButton)
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='container']/h2/text()")))
            html = self.driver.page_source
            self.driver.close() 
            return html
        except:
            pass
        
    """ This function helps in taking each url from the wedding_url.csv file and pass it as a parameter to the parse function.
    The parse function returns info that is appened to a list and finally result in a csv file with raw data"""
    def selection(self):
        data=[]
                
        info=self.parse(self.url)        
        dataset=pd.read_csv("C://Users//Sangamithra//Desktop//project//wedding_url.csv")["url"]

        for each_url in dataset:
            print(each_url)
            self.url = f"{each_url}"
            try:
                info=self.parse(self.url) 
                if info: 
                    data.append(info)
            except:
                pass
        
        df=pd.DataFrame(data)
        df.to_csv(r"C://Users//Sangamithra//Desktop//project//wedding_info.csv")

    """The parse function gets the input as url and then pass the url to the selenuim function. The selenuim function return HTML page source from 
    which we can extract necessary information. Once done, the information is sent as a dict to the selection function."""
    
    def parse(self,url):

        dict={}
        soup = self.selenium(url)
        try:
            response = Selector(text=soup)


            dict["Summary"]=response.xpath('//div[@class="col-md-6"]/p[1]/text()').get()
            dict["Season"]=response.xpath('//table[@class="table table-striped"]/tbody/tr[2]/td/text()').get()
            dict["Wedding_destination"]=response.xpath('//table[@class="table table-striped"]/tbody/tr[3]/td/text()').get()
            dict["Guest"]=response.xpath('//table[@class="table table-striped"]/tbody/tr[4]/td/text()').get()
            dict["Location"]=response.xpath('//table[@class="table table-striped"]/tbody/tr[6]/td/text()').get()
            dict["Describing_words"]=response.xpath('//table[@class="table table-striped"]/tbody/tr[8]/td/text()').get()
            dict["Priority_1"]=response.xpath('//table[@class="table table-striped"]/tbody/tr[10]/td//ul/li[1]/text()').get()
            dict["Priority_2"]=response.xpath('//table[@class="table table-striped"]/tbody/tr[10]/td//ul/li[2]/text()').get()
            dict["Priority_3"]=response.xpath('//table[@class="table table-striped"]/tbody/tr[10]/td//ul/li[3]/text()').get()
            dict["Estimate"]=response.xpath('//div[@class="container"]/h2/text()').get()


            dict["Attire_Accessories"]=response.xpath('//table[@class="table"]/tbody/tr[2]/td[2]/text()').get()
            dict["Beauty_spa"]=response.xpath('//table[@class="table"]/tbody/tr[3]/td[2]/text()').get()
            dict["Entertainment"]=response.xpath('//table[@class="table"]/tbody/tr[4]/td[2]/text()').get()
            dict["Flowers_Decorations"]=response.xpath('//table[@class="table"]/tbody/tr[5]/td[2]/text()').get()
            dict["Gifts"]=response.xpath('//table[@class="table"]/tbody/tr[6]/td[2]/text()').get()
            dict["invitations"]=response.xpath('//table[@class="table"]/tbody/tr[7]/td[2]/text()').get()
            dict["Photography"]=response.xpath('//table[@class="table"]/tbody/tr[9]/td[2]/text()').get()
            dict["Planner"]=response.xpath('//table[@class="table"]/tbody/tr[10]/td[2]/text()').get()
            dict["venue_Catering_rental"]=response.xpath('//table[@class="table"]/tbody/tr[11]/td[2]/text()').get()

            return(dict)
        except:
            pass

    
        

if __name__=="__main__":
    obj=wedding_info()
    obj.selection()
