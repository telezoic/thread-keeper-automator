#python 3.11.0
#headlessly, Firefox
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Set up headless Firefox
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode

# Initialize the Firefox driver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

# Prompt for the CSV file name and open it
csvfile = input("Enter the name of the csv input file . . .")
urls = csv.reader(open(csvfile, "r"))
count = 1

# Process each URL in the CSV
for url in urls:
    driver.get("YOUR SERVER URL HERE")

#using FF inspect => xpath here :) 

    thread_link = driver.find_element(By.ID, "url")
    thread_link.send_keys(url[0])

    reason = driver.find_element(By.ID, "why")
    reason.send_keys(url[0])

    checkbox = driver.find_element(By.ID, "unfold-thread")
    checkbox.click()

    time.sleep(10)

    capture_button = driver.find_element(By.XPATH, "/html/body/main/form/fieldset[3]/button")
    capture_button.click()

    time.sleep(10)

    final_capture_button = driver.find_element(By.XPATH, "/html/body/main/dialog/button")
    final_capture_button.click()

    time.sleep(40)

    print(count, url[0])
    count += 1

# driver.quit()  # Uncomment to close the browser when done
