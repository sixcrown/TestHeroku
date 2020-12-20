import time
print("HELLO LOGS XD ");
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.set_headless()
gChromeOptions.add_argument("window-size=1920x1480")
gChromeOptions.add_argument("disable-dev-shm-usage")
print(gChromeOptions.headless);
gDriver = webdriver.Chrome(
    chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
)
auto = gDriver.get("https://www.python.org/")
time.sleep(2)
print(auto);
gDriver.close()