import requests
import lxml
from bs4 import BeautifulSoup
import time
from time import sleep
import random

def tucasa():
    a = True

    while a == True:
        time.sleep(random.randint(0, 10))
        request = requests.get("https://www.tucasa.com/compra-venta/viviendas/madrid/?r=&idz=0028")
        soup = BeautifulSoup(request.text, "lxml")

        description = soup.find("span", class_="txt-descripcion-listado").text
        cost = soup.find("span", class_="precio-listado hidden-cards").text
        habs = soup.find("li", class_="num-habitaciones visible-xs visible-sm").text
        m2 = soup.find("li", class_="metros-cuadrados").text
        bath = soup.find("li", class_="num-baños").text
        where = soup.find("span", class_="titulo-inmueble").text
        url = soup.find("div", class_="div-btn-detalle visible-xs visible-sm" )
        urlchild = url.findChild()["href"]

        print(f"""
\U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

{description}
----------------
\U0001F4B5 {cost.strip()} 
\U0001F6CF {habs}, {bath}, {m2}
\U0001F4CD {where.strip()}
----------------
\U0001F4F2 https://www.tucasa.com{urlchild}
""")

        r = requests.post('https://api.telegram.org/bot1872545614:AAGJ7ppnL5VkhRoHdJno1xp3M4UvMe1ji4Y/sendMessage', data={'chat_id': '-596894934', 'text': f"""
\U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

{description}
----------------
\U0001F4B5 {cost.strip()} 
\U0001F6CF {habs}, {bath}, {m2}
\U0001F4CD {where.strip()}
----------------
\U0001F4F2 https://www.tucasa.com{urlchild}
"""})
tucasa()