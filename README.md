# Pk's py Discord copycat

A simple discord bot that repeats what is said in a given channel

## Commands

- *authorize : to allow the bot to function in this channel
- *unauthorize : to unallow the bot to function in this channel
- *unauthorize_all : to unallow the bot to function in all channels
- *is_authorized : says if the bot is allowed to function in the current channel
- *puck : for a surprise

## Prerequisites

- Python (preferably Python 3.11)
- a configured Discord Bot + Token
- a Riot development API Key

## How to install

1. open a shell in the files directory

2. create a virtual environment with : `python -m venv env`  
(or change "python" with the path of Python 3.11, for example on windows : `C:\Users\User\AppData\Local\Programs\Python\Python311\python.exe -m venv env`)

3. activate the environment with : `env\scripts\activate.ps1` on Windows PowerShell  
(or `env\bin\activate` on Linux or `env\scripts\activate.bat` if using the cmd)

4. install the required packages with `pip install -r requirements.txt`

5. create an `.env` file then write inside 
```
BOT_TOKEN=(your token)
```

## How to start

1. open a shell in the files directory

2. activate the environment with : `env\scripts\activate.ps1` on Windows PowerShell  
(or `env\bin\activate` on Linux or `env\scripts\activate.bat` if using the cmd)

3. run the script with `python main.py`