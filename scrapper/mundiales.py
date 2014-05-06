#!/usr/bin/env python

from selenium import webdriver
import csv
import re

driver = webdriver.Firefox()
driver.get('http://es.fifa.com/tournaments/archive/worldcup/index.html')

mundiales = driver.find_elements_by_css_selector('li.jcarousel-item a')

f = open('mundiales.csv', 'wt')
w = csv.writer(f)
w.writerow([
  'anio', 'pais', 'url'
])

for mundial in mundiales:
  title = mundial.get_attribute('title')
  m = re.search(r'Copa Mundial de la FIFA (.*) (.*?)', title, re.M|re.I)
  pais = m.group(1)
  print ('%s, %s, %s, %s') % (title, mundial.text, pais, mundial.get_attribute('href'))
  # w.writerow([
  #   mundial.text, pais, mundial.get_attribute('href')
  # ])

f.close()

driver.quit()
