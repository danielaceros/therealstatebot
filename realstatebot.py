import requests
import re
from bs4 import BeautifulSoup
import time
from time import sleep
from datetime import datetime
import datetime
import threading
from tqdm import tqdm
import socket

print("""
██████╗ ███████╗ █████╗ ██╗     ███████╗████████╗ █████╗ ████████╗███████╗██████╗  ██████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██║     ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝█████╗  ███████║██║     ███████╗   ██║   ███████║   ██║   █████╗  ██████╔╝██║   ██║   ██║   
██╔══██╗██╔══╝  ██╔══██║██║     ╚════██║   ██║   ██╔══██║   ██║   ██╔══╝  ██╔══██╗██║   ██║   ██║   
██║  ██║███████╗██║  ██║███████╗███████║   ██║   ██║  ██║   ██║   ███████╗██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝  ╚═════╝    ╚═╝   
                                                                                                    
Press ENTER key to start RealStateBOT©... """)
a = input("> ")
c = True
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

# set-up your bot on TELEGRAM
global token 
token = "change" # bot TOKEN ej. "bot1293186140:AAHy1CZGmkNj8vY4SzbE4KFs3VZrfu46XsU"
global chat_id
chat_id = "change" # your CHAT ID ej. "-8000225000194"

for i in tqdm(range(0, 100)):
    time.sleep(0.000000001)

print("""
""")

def tucasa():
    a = True

    while a == True:
        request = requests.get("https://www.tucasa.com/compra-venta/viviendas/madrid/madrid/todos/?r=&idz=0028.0001.9999.0001")
        soup = BeautifulSoup(request.text, "lxml")
        cost = soup.find("span", class_="precio-card").text
        
        request2 = requests.get("https://www.tucasa.com/compra-venta/viviendas/madrid/madrid/todos/?r=&idz=0028.0001.9999.0001")
        soup2 = BeautifulSoup(request2.text, "lxml")

        description2 = soup2.find("span", class_="txt-descripcion-listado").text
        cost2 = soup2.find("span", class_="precio-card").text
        habs2 = soup2.find("li", class_="num-habitaciones visible-xs visible-sm").text
        m2_2 = soup2.find("li", class_="metros-cuadrados").text
        bath2 = soup2.find("li", class_="num-baños").text
        where2 = soup2.find("span", class_="titulo-inmueble").text
        url2 = soup2.find("div", class_="div-btn-detalle visible-xs visible-sm" )
        urlchild2 = url2.findChild()["href"]

        if cost != cost2:
            r = requests.post(f'https://api.telegram.org/{token}/sendMessage', data={'chat_id': chat_id, 'text': f"""
 \U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

 {description2.strip()}
 ----------------
 \U0001F4B5 {cost2.strip()} 
 \U0001F6CF {habs2}, {bath2}, {m2_2}
 \U0001F4CD {where2.strip()}
 ----------------
 \U0001F4F2 https://www.tucasa.com{urlchild2}
 """})

def pisoscom():
    a = True

    while a == True:
        request = requests.get("https://www.pisos.com/venta/pisos-madrid_capital/ascensor/fecharecientedesde-desc/")
        soup = BeautifulSoup(request.text, "lxml")
        
        cost = soup.find("span", class_="ad-preview__price").text
        
        request2 = requests.get("https://www.pisos.com/venta/pisos-madrid_capital/ascensor/fecharecientedesde-desc/")
        soup2 = BeautifulSoup(request2.text, "lxml")

        description2 = soup2.find("a", class_="ad-preview__title").text
        cost2 = soup2.find("span", class_="ad-preview__price").text
        habs2 = soup2.find("p", class_="ad-preview__char p-sm").text
        where2_2 = soup2.find("p", class_="p-sm").text
        url2 = soup2.find("div", class_="ad-preview ad-preview--has-desc")
        hab2 = str(habs2.replace(" ", ""))
        habb2 = str(hab2)
        habss2 = re.sub(r'[\ \n]{2,}', '', habb2)

        if cost != cost2:
            r = requests.post(f'https://api.telegram.org/{token}/sendMessage', data={'chat_id': chat_id, 'text': f"""
 \U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

 {description2.strip()}
 ----------------
 \U0001F4B5 {cost2.strip()} 
 \U0001F6CF {habss2.strip()}
 \U0001F4CD {where2_2.strip()}
 ----------------
 \U0001F4F2 https://www.pisos.com{url2['data-lnk-href']}
 """})

def habitalia():
    a = True

    while a == True:
        request = requests.get("https://www.habitaclia.com/viviendas-ascensor-madrid.htm?ordenar=mas_recientes")
        soup = BeautifulSoup(request.text, "lxml")

        cost = soup.find("span", class_="font-2").text

        request2 = requests.get("https://www.habitaclia.com/viviendas-ascensor-madrid.htm?ordenar=mas_recientes")
        soup2 = BeautifulSoup(request2.text, "lxml")

        description2 = soup2.find("p", class_="list-item-description").text
        cost2 = soup2.find("span", class_="font-2").text
        habs2 = soup2.find("p", class_="list-item-feature").text
        where2 = soup2.find("p", class_="list-item-location").text
        url2 = soup2.find("h3", class_="list-item-title")
        hab2 = str(habs2.strip())
        urlchild2 = url2.findChild()["href"]
        habb2 = str(hab2.replace("											", ""))
        habbsss2 = re.sub(r'[\ \n]{2,}', '', habb2)

        if cost != cost2:
            r = requests.post(f'https://api.telegram.org/{token}/sendMessage', data={'chat_id': chat_id, 'text': f"""
 \U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

 {description2.strip()}
 ----------------
 \U0001F4B5 {cost2} 
 \U0001F6CF {habbsss2.strip()}
 \U0001F4CD {where2.strip()}
 ----------------
 \U0001F4F2 {urlchild2}
 """})

def fotocasa():
    a = True

    while a == True:
        request = requests.get("https://www.fotocasa.es/es/comprar/pisos/madrid-capital/todas-las-zonas/ascensor/l?sortType=publicationDate&latitude=40.4096&longitude=-3.68624&conservationStatusIds=4&combinedLocationIds=724,14,28,173,0,28079,0,0,0&gridType=3")
        soup = BeautifulSoup(request.text, "lxml")

        cost = soup.find("span", class_="re-CardPrice").text

        request2 = requests.get("https://www.fotocasa.es/es/comprar/pisos/madrid-capital/todas-las-zonas/ascensor/l?sortType=publicationDate&latitude=40.4096&longitude=-3.68624&conservationStatusIds=4&combinedLocationIds=724,14,28,173,0,28079,0,0,0&gridType=3")
        soup2 = BeautifulSoup(request2.text, "lxml")

        description2 = soup2.find("span", class_="re-CardDescription-text").text
        cost2 = soup2.find("span", class_="re-CardPrice").text
        habs2 = soup2.find("li", class_="re-CardFeatures-feature").text
        where2 = soup2.find("span", class_="re-CardTitle").text
        url2 = soup2.find("a", class_="re-CardPackMinimal-info-container" )

        if cost != cost2:
            r = requests.post(f'https://api.telegram.org/{token}/sendMessage', data={'chat_id': chat_id, 'text': f"""
 \U0001F3E1 ¡NUEVO PISO ENCONTRADO! \U0001F3E1

 {description2.strip()}
 ----------------
 \U0001F4B5 {cost2} 
 \U0001F6CF {habs2}
 \U0001F4CD {where2}
 ----------------
 \U0001F4F2 https://www.fotocasa.es{url2["href"]}
 """})

threading.Thread(target=tucasa).start()
threading.Thread(target=pisoscom).start()
threading.Thread(target=habitalia).start()
threading.Thread(target=fotocasa).start()

while c == True:   
    print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "]" + " " + f"RealStateBOT© connected successfully at {ip} on port 443, looking for some new Real State, check your Telegram...", end="\r" )


