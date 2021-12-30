# -*- coding: utf-8 -*-
"""
### Bot ###
Getting out GRGLMPROD NOAA date utilizing
a list of date and time
Sattelite: G16
Fix the names and variables to you use
@author: TalDoMorgan
"""

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
table_date = pd.read_excel(r"C:\[...]\date.xlsx") # .xlxs = excel, u can use others types of tables switching the type in all others lines.

for i in range (QUANTITY_OF_THE_LINES_OF_DATES): 
# Date of the event
    date = str(table_date['D'][i])
    date = date.replace(" 00:00:00","") # if your date are in format datetime
#implementar hora do inicio e hora do fim
    hora = str(table_date['H'][i])

    path = Service(r"C:\Users\pc\Documents\PIBIC_PY\geckodriver.exe") # install the driver following the selenium's guide
    browser = webdriver.Firefox(service=path)
    browser.get('https://www.avl.class.noaa.gov/saa/products/search?sub_id=0&datetype_family=GRGLMPROD&submit.x=25&submit.y=3')
    time.sleep(5)

    browser.find_element_by_xpath('//*[@id="start_date"]').clear()
    browser.find_element_by_xpath('//*[@id="start_date"]').send_keys(date) # (format: YYYY-MM-DD)

    browser.find_element_by_xpath('//*[@id="end_date"]').clear()
    browser.find_element_by_xpath('//*[@id="end_date"]').send_keys(date) # (format: YYYY-MM-DD)

    browser.find_element_by_xpath('//*[@id="start_time"]').clear()
    browser.find_element_by_xpath('//*[@id="start_time"]').send_keys(hora) # (format: HH:MM:SS)

    browser.find_element_by_xpath('//*[@id="end_time"]').clear()
    browser.find_element_by_xpath('//*[@id="end_time"]').send_keys(hora) # (format: HH:MM:SS)

    browser.find_element_by_xpath('//*[@id="advanced"]/table/tbody/tr/td[1]/input').click()

    browser.find_element_by_id('G16').click()

    browser.find_element_by_xpath('//*[@id="searchbutton"]').click()

    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="contentArea"]/page/div[2]/form[2]/table[2]/tbody/tr[2]/td[2]/input').click()
# If for this date exist more than one data, this step will select both them -----
    print("##########################################################")
    try:
        browser.find_element_by_xpath('//*[@id="contentArea"]/page/div[2]/form[2]/table[2]/tbody/tr[3]/td[2]/input').click()
    except NoSuchElementException:
        print("The element " + str(i) + " from the table has no 2 time.")
    print("##########################################################")
    #####-------------#####
    browser.find_element_by_xpath('//*[@id="contentArea"]/page/div[2]/form[2]/table[1]/tbody/tr/td[2]/input[1]').click()
    time.sleep(4)
# Faz o login
    browser.find_element_by_xpath('//*[@id="midNavElements"]/li[2]/a').click()
    time.sleep(2)
    browser.find_element_by_name('j_username').send_keys("yourName") # insert your name between ""
    browser.find_element_by_name('j_password').send_keys("yourPassword") # insert your password between ""
    browser.find_element_by_xpath('//*[@id="contentArea"]/div/form/input[3]').click()

# Finaliza pedido
    browser.find_element_by_xpath('//*[@id="contentArea"]/form[2]/div[2]/input[1]').click()
    time.sleep(5)
    browser.close()