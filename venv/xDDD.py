from selenium import webdriver
import os
chromeoptions = webdriver.ChromeOptions();
chromeoptions.binary_location = os.environ.get("GOOGLE_CRHOME_BIN")
chromeoptions.add_argument("--headless")
chromeoptions.add_argument("--disable-dev-shm-usage")
chromeoptions.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chromeoptions)

driver.get("https://www.familysearch.org/pl/")
print(driver.page_source)
driver.quit()
