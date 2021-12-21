import requests
import lxml
from bs4 import BeautifulSoup
import time
from time import sleep
import random

def habitalia():
    a = True

    while a == True:
        time.sleep(random.randint(0, 10))
        request = requests.get("https://www.habitaclia.com/viviendas-madrid.htm?ordenar=mas_recientes")
        soup = BeautifulSoup(request.text, "lxml")

        description = soup.find("p", class_="list-item-description").text
        cost = soup.find("span", class_="font-2").text
        habs = soup.find("p", class_="list-item-feature").text
        where = soup.find("p", class_="list-item-location").text
        url = soup.find("h3", class_="list-item-title")
        hab = str(habs.strip())
        urlchild = url.findChild()["href"]
        habb = str(hab.replace("											", ""))

        print(f"""
\U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

{description}
----------------
\U0001F4B5 {cost} 
\U0001F6CF {habb}
\U0001F4CD {where.strip()}
----------------
\U0001F4F2 {urlchild}
""")

        r = requests.post('https://api.telegram.org/bot1713186140:AAHy1GZGmkMj8vY4SpbE4KFs3VZrfu46XfU/sendMessage', data={'chat_id': '-596894934', 'text': f"""
\U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

{description}
----------------
\U0001F4B5 {cost} 
\U0001F6CF {habb}
\U0001F4CD {where.strip()}
----------------
\U0001F4F2 {urlchild}
"""})
habitalia()