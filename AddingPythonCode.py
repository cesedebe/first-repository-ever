from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pdb
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://localhost/myEcommSite/')

#seacrh for hoodies on the search bar
search = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search.send_keys('Hoodie')
search.send_keys(Keys.ENTER)
time.sleep(5)