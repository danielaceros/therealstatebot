# therealstatebot
A BOT who allows you to know if there are new flats in sold, in realstate pages such as FotoCasa, TuCasa, Habitaclia and Pisoscom, then it send to you a Telegram for notifying.
# Getting Started
Download the repo and install the necesary modules if you haven't done it before
* pip install requests
* pip install re
* pip install bs4
* pip install time
* pip install datetime
* pip install threading
* pip install tqdm
* pip install socket
# Changing TELEGRAM TOKEN
Open the file 'realstatebot.py' and put your token on the variable 'token' and your chat id on the variable 'chat_id' at the top of the script.
# Running Code
Run the file with PowerShell or CommandPrompt on the running directory by
* python realstatebot.py
* python3 realstatebot.py
# Functionalities
It automatically checks on Tucasa, Pisoscom, Habitaclia, Fotocasa and send to you a Telegram if there are any new flat.
