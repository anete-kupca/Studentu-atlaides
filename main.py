from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def iegut_atlaides():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://isic.lv/lv/atlaides/")
    scroll_pause = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    discounts = {}
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'discount-block-item')))
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('a', class_='discount-block-item')

        for i in items:
            title = i.find('span', class_='title')
            discount_span = i.find('span', class_='discount')
            discount = discount_span.get('data-discount') if discount_span else ""

            if title:
                name = title.text.strip()
                discounts[name.lower()] = discount

    except Exception as e:
        print("Neizdevās ielādēt lapu:", e)
    finally:
        driver.quit()

    return discounts

def meklet_atlaidi(discounts):
    nosaukums = input("Ievadi uzņēmuma nosaukumu: ").strip().lower()
    atrasti = {}
    for name, discount in discounts.items():
        if nosaukums in name:
            atrasti[name] = discount

    if atrasti:
        print("\nRezultāti:")
        for name, discount in atrasti.items():
            print(f"{name.title()} – atlaide: {discount}")
    else:
        print("Uzņēmums netika atrasts.")

def paradit_visas(discounts):
    print("\nVisas atlaides:")
    for name, discount in discounts.items():
        print(f"{name.title()} – {discount}")
    print()

def iziet():
    print("Programma tiek izbeigta. Uz redzēšanos!")

if __name__ == "__main__":
    atlaides = iegut_atlaides()

    while True:
        print("\n--- Izvēlne ---")
        print("1 - Meklēt atlaidi pēc uzņēmuma nosaukuma")
        print("2 - Apskatīt visas atlaides")
        print("3 - Iziet")

        izvele = input("Izvēlies darbību (1/2/3): ").strip()

        if izvele == '1':
            meklet_atlaidi(atlaides)
        elif izvele == '2':
            paradit_visas(atlaides)
        elif izvele == '3':
            iziet()
            break
        else:
            print("Nederīga izvēle, mēģini vēlreiz")
