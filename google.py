#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

search_query = input("Enter whatever you want to google : ")
browser = webdriver.Firefox()
browser.get('http://google.com/')

searchBox =  browser.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[1]/div/div[1]/input')
searchBox.send_keys(search_query)
searchBox.send_keys(Keys.RETURN)
results = []
time.sleep(4)
results = browser.find_elements_by_class_name('r')
results[0].click()
