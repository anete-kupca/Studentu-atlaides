from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://isic.lv/lv/atlaides/")

scroll_pause = 1
last_height = driver.execute_script("return document.body.scrollHeight")
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'discount-block-item')))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='discount-block-item')

    print("Atlaides:")
    for i in items:
        t = i.find('span', class_='title')
        if t:
            print("-", t.text.strip())
except:
    print("Neizdevās ielādēt lapu")

driver.quit()