# import time
# print("HELLO LOGS XD ");
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# gChromeOptions = webdriver.ChromeOptions()
# gChromeOptions.set_headless()
# gChromeOptions.add_argument("window-size=1920x1480")
# gChromeOptions.add_argument("disable-dev-shm-usage")
# gDriver = webdriver.Chrome(
#     chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
# )
# print("EMPTY");
from selenium import webdriver
import os
chromeoptions = webdriver.ChromeOptions();
chromeoptions.binary_location = os.environ.get("GOOGLE_CRHOME_BIN")
chromeoptions.add_argument("--headless")
chromeoptions.add_argument("--disable-dev-shm-usage")
chromeoptions.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chromeoptions)

driver.get("https://www.google.com")
print(driver.page_source)
