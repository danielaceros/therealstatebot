import requests
import lxml
from bs4 import BeautifulSoup
import time
from time import sleep
import random

def fotocasa():
    a = True

    while a == True:
        time.sleep(random.randint(0, 10))
        request = requests.get("https://www.fotocasa.es/es/comprar/pisos/madrid-capital/todas-las-zonas/l?sortType=publicationDate")
        soup = BeautifulSoup(request.text, "lxml")

        description = soup.find("span", class_="re-Card-description").text
        cost = soup.find("span", class_="re-Card-price").text
        habs = soup.find("div", class_="re-CardFeatures-wrapper").text
        where = soup.find("h3", class_="re-Card-title").text
        url = soup.find("a", class_="re-Card-link" )

        print(f"""
\U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

{description}
----------------
\U0001F4B5 {cost} 
\U0001F6CF {habs}
\U0001F4CD {where}
----------------
\U0001F4F2 https://www.fotocasa.es{url["href"]}
""")

        r = requests.post('https://api.telegram.org/bot1889733994:AAGMNq69cUOWnk0RWlC2NMAXbfVFEpvj9DY/sendMessage', data={'chat_id': '-596894934', 'text': f"""
\U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

{description}
----------------
\U0001F4B5 {cost} 
\U0001F6CF {habs}
\U0001F4CD {where}
----------------
\U0001F4F2 https://www.fotocasa.es{url["href"]}
"""})

fotocasa()