import requests
from bs4 import BeautifulSoup 

url = "https://isic.lv/lv/atlaides/"
lapa = requests.get(url)

if lapa.status_code == 200:
    lapas_saturs = BeautifulSoup(lapa.text, "html.parser")
    print(lapas_saturs.prettify())