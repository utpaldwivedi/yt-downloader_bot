# Youtube Video Downloader Bot

It is designed to get direct download links of Youtube videos with resolution 720p or less. This is a helpful tool when user has a limited connection to internet.</br></br>
`pyTelegramBotAPI` - used to connect to the bot and send and receive data.</br>
`pytubefix` - used to get download links for Youtube videos</br>

Bot link - `https://t.me/yt_downloader_utpal_bot`

To create your own bot -

Firstly go to `BotFather` , an official bot created by Telegram to handle API request for Bot management.</br>
Create a new Bot by giving it a name and username.</br>
Keep the `TOKEN` safe and we will be calling it `TELEBOT_TOKEN` from now.

Then clone the github repo by running -
`git clone https://github.com/utpaldwivedi/yt-downloader_bot.git`

When into the root directory(containing yt_downloader_bot.py) right click and open VS code or Windows Powershell and execute these commands-
1. Create a virtual env using
    `python -m venv .venv`
2. Activate the environment(in Windows Powershell)
   `.venv\Scripts\Activate.ps1`
3. Install required dependencies
   `pip install -r requirements.txt`
4. Create a .env file in the root directory and put your own `TELEBOT_TOKEN` obtained by creating a bot from `BotFather`
5. To start polling (Now the bot responds to all the requests made by any user)
   `python run yt_downloader_bot.py`
6. Close down bot
   `Ctrl+C`
7. Deactivate environment
   `deactivate`
