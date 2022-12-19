#python 3.11.0
#headlessly
import time
import csv
from itertools import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless=chrome")
driver = webdriver.Chrome(service=Service('PATH TO YOUR CHROMEDRIVER'),
                          options=chrome_options)


csvfile = input("Enter the name of the csv input file . . .")

urls = csv.reader(open(csvfile, "r"))
count = 1





for url in urls:
	

		driver.get("URL FOR YOUR SERVER")

		thread_link = driver.find_element(By.ID, "url")

		thread_link.send_keys(url[0])

		reason = driver.find_element(By.ID, "why")
		reason.send_keys(url[0])

		checkbox = driver.find_element(By.ID, "unfold-thread")
		checkbox.click()

		time.sleep(10)


		capture_button = driver.find_element(By.XPATH, value="/html/body/main/form/fieldset[3]/button")
		#using FF inspect => xpath here :) 
		capture_button.click()

		time.sleep(10)

		final_capture_button = driver.find_element(By.XPATH, value="/html/body/main/dialog/button")
		final_capture_button.click()

		time.sleep(40)
		
		#driver.quit()

		print(count , url[0])
		#print(url[0])
		#print(count)
		count += 1
		
	
		


