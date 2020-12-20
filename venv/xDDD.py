from selenium import webdriver
import os
chromeoptions = webdriver.ChromeOptions();
chromeoptions.binary_location = os.environ.get("GOOGLE_CRHOME_BIN")
chromeoptions.add_argument("--headless")
chromeoptions.add_argument("--window-size=1920x1080")
chromeoptions.add_argument("--disable-dev-shm-usage")
chromeoptions.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chromeoptions)

driver.get("https://www.familysearch.org/en/")
driver.implicitly_wait(2)
print(driver.page_source)
acceptCookies = driver.find_element_by_xpath('/html/body/div[8]/div[1]/div/div[2]/div[2]/a[1]')
acceptCookies.click();
# sign_in = driver.find_element_by_xpath('/html/body/div/header/div[2]/div[2]/nav/a[1]');
# sign_in.click()
# print(driver.page_source)
driver.quit()
