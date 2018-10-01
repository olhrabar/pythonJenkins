from selenium import webdriver
import time
import os
import jenkins

driver = webdriver.Chrome()
driver.get("https://www.asus.com/Laptops/ASUS-VivoBook-Pro-15-N580GD/HelpDesk_Download")
driver.find_element_by_xpath("//*[@id='btn-close-ck']").click()

driver.find_element_by_xpath("//*[@id='osbar']/select").click()
driver.find_element_by_xpath("//*[@id='osbar']/select/option[2]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='Drivers-Download']/div[2]/div[2]/div[2]/div/section[4]/div/div[2]/a/span").click()
time.sleep(5)
