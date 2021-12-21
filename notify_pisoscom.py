import requests
import lxml
from bs4 import BeautifulSoup
import time
from time import sleep
import random

def pisoscom():
    a = True

    while a == True:
        time.sleep(random.randint(0, 10))
        request = requests.get("https://www.pisos.com/venta/pisos-madrid/fecharecientedesde-desc/")
        soup = BeautifulSoup(request.text, "lxml")

        description = soup.find("div", class_="description").text
        cost = soup.find("div", class_="price").text
        habs = soup.find("div", class_="characteristics").text
        where = soup.find("a", class_="anuncioLink").text
        where2 = soup.find("div", class_="location").text
        url = soup.find("a", class_="anuncioLink" )
        hab = str(habs.replace(" ", ""))
        habb = str(hab.replace("""


    """, ""))

        print(f"""
\U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

{description}
----------------
\U0001F4B5 {cost.strip()} 
\U0001F6CF {habb.strip()}
\U0001F4CD {where}
----------------
\U0001F4F2 https://www.pisos.com/{url["href"]}
""")

        r = requests.post('https://api.telegram.org/bot1872637823:AAF3_7CMBKWGZbigjD1vUjFdN6daMb0sqJI/sendMessage', data={'chat_id': '-596894934', 'text': f"""
\U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

{description}
----------------
\U0001F4B5 {cost.strip()} 
\U0001F6CF {habb.strip()}
\U0001F4CD {where}
----------------
\U0001F4F2 https://www.pisos.com/{url["href"]}
"""})
pisoscom()