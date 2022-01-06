<html>
<div align="center">
<img src="https://primeprofitmedia.com/wp-content/uploads/2021/05/real-estate.jpg" alt="alt text" width="300" height="300"></img>
</div>
<h1 align="center">@danielaceros
<div align="center">
<a href=https://github.com/danielaceros><img src="https://img.shields.io/static/v1?label=&labelColor=505050&message=@danielaceros&color=%230076D6&style=flat&logo=google-chrome&logoColor=%230076D6" alt="website"/></a>
<img src="https://img.shields.io/github/followers/danielaceros?style=social" alt="Star Badge"/>
<a><img src="https://img.shields.io/github/last-commit/danielaceros/therealstatebot" alt="Join Community Badge"/></a>
<a><img src="https://img.shields.io/github/repo-size/danielaceros/therealstatebot" />
</div>
</html>

# therealstatebot
A BOT who allows you to know if there are new flats in sold, in realstate pages such as FotoCasa, TuCasa, Habitaclia and Pisoscom, then it send to you a Telegram for notifying.
## Getting Started
Download the repo and install the necesary modules if you haven't done it before.
```bash
pip/pip3 install requests
pip/pip3 install re
pip/pip3 install bs4
pip/pip3 install time
pip/pip3 install datetime
pip/pip3 install threading
pip/pip3 install tqdm
pip/pip3 install socket
```
## Changing TELEGRAM TOKEN
Open the file 'realstatebot.py' and put your token on the variable 'token' and your chat id on the variable 'chat_id' at the top of the script.
## Running Code
Run the file with PowerShell or CommandPrompt on the running directory by
```bash
python realstatebot.py
python3 realstatebot.py
```
## Functionalities
It automatically checks on Tucasa, Pisoscom, Habitaclia, Fotocasa and send to you a Telegram if there are any new flat.
## License
[GPL](https://choosealicense.com/licenses/gpl-3.0/)
