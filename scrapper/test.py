#!/usr/bin/env python

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://es.fifa.com/tournaments/archive/worldcup/index.html')
print driver.title
driver.quit()
