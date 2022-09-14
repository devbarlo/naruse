import asyncio
import logging
import os
import sys
import time
from typing import List
import spamwatch
import telegram.ext as tg
from Python_ARQ import ARQ
from redis import StrictRedis
from telethon import TelegramClient
from telethon.sessions import MemorySession
from configparser import ConfigParser
from ptbcontrib.postgres_persistence import PostgresPersistence
from functools import wraps
from logging.config import fileConfig
from aiohttp import ClientSession
from telethon.sessions import StringSession
from telethon.sessions import MemorySession
# from pyrogram import Client, errors
# from pyrogram.types import Message
# from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
# from pyrogram.types import Chat, User
# from pyromod import listen

# CODE YOUR OWN HERE!
# DON'T ASK GROUP / PM

StartTime = time.time()


flag = """
\033[37m┌─────────────────────────────────────────────┐\033[0m\n\033[37m│\033[44m\033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[0m\033[91;101m#########################\033[0m\033[37m│\n\033[37m│\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m  \033[0m\033[97;107m:::::::::::::::::::::::::\033[0m\033[37m│\n\033[37m│\033[44m\033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[0m\033[91;101m#########################\033[0m\033[37m│\n\033[37m│\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m  \033[0m\033[97;107m:::::::::::::::::::::::::\033[0m\033[37m│\n\033[37m│\033[44m\033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[0m\033[91;101m#########################\033[0m\033[37m│\n\033[37m│\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m  \033[0m\033[97;107m:::::::::::::::::::::::::\033[0m\033[37m│\n\033[37m│\033[44m\033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[97m★\033[0m\033[44m \033[0m\033[91;101m#########################\033[0m\033[37m│      \033[1mUnited we stand, Divided we fall\033[0m\n\033[37m│\033[97;107m:::::::::::::::::::::::::::::::::::::::::::::\033[0m\033[37m│ \033[1mKigyo Project, a tribute to USS Enterprise.\033[0m\n\033[37m│\033[91;101m#############################################\033[0m\033[37m│\n\033[37m│\033[97;107m:::::::::::::::::::::::::::::::::::::::::::::\033[0m\033[37m│\n\033[37m│\033[91;101m#############################################\033[0m\033[37m│\n\033[37m│\033[97;107m:::::::::::::::::::::::::::::::::::::::::::::\033[0m\033[37m│\n\033[37m│\033[91;101m#############################################\033[0m\033[37m│\n\033[37m└─────────────────────────────────────────────┘\033[0m\n
"""

def get_user_list(key):
    # Import here to evade a circular import
    from naruse.modules.sql import nation_sql
    royals = nation_sql.get_royals(key)
    return [a.user_id for a in royals]

# enable logging

fileConfig('logging.ini')

LOGGER = logging.getLogger('[naruse]')
LOGGER.info("naruse is starting. | Rendy Projects. | Licensed under GPLv3.")
LOGGER.info("Project maintained by: github.com/TeamKillerX (t.me/rencprx)")

# if version < 3.6, stop bot
if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    log.error(
        "[NARUSE] You MUST have a python version of at least 3.7! Multiple features depend on this. Bot quitting."
    )
    quit(1)

parser = ConfigParser()
parser.read("config.ini")
nuconfig = parser["nuconfig"]


class NaruseINIT:
    def __init__(self, parser: ConfigParser):
        self.parser = parser
        self.SYS_ADMIN: int = self.parser.getint('SYS_ADMIN', 0)
        self.OWNER_ID: int = self.parser.getint('OWNER_ID')
        self.OWNER_USERNAME: str = self.parser.get('OWNER_USERNAME', None)
        self.APP_ID: str = self.parser.getint("APP_ID")
        self.API_HASH: str = self.parser.get("API_HASH")
        self.TOKEN: str = self.parser.get("TOKEN")
        self.DB_URI: str = self.parser.get("SQLALCHEMY_DATABASE_URI")
        self.LOAD = self.parser.get("LOAD").split()
        self.LOAD: List[str] = list(map(str, self.LOAD))
        self.MESSAGE_DUMP: int = self.parser.getint('MESSAGE_DUMP', None)
        self.GBAN_LOGS: int = self.parser.getint('GBAN_LOGS', None)
        self.NO_LOAD = self.parser.get("NO_LOAD").split()
        self.NO_LOAD: List[str] = list(map(str, self.NO_LOAD))
        self.WEBHOOK: bool = self.parser.getboolean('WEBHOOK', False)
        self.URL: str = self.parser.get('URL', None)
        self.CERT_PATH: str = self.parser.get('CERT_PATH', None)
        self.PORT: int = self.parser.getint('PORT', None)
        self.INFOPIC: bool = self.parser.getboolean('INFOPIC', False)
        self.DEL_CMDS: bool = self.parser.getboolean("DEL_CMDS", False)
        self.STRICT_GBAN: bool = self.parser.getboolean("STRICT_GBAN", False)
        self.ALLOW_EXCL: bool = self.parser.getboolean("ALLOW_EXCL", False)
        self.CUSTOM_CMD: List[str] = ['/', '!']
        self.spamwatch_api: str = self.parser.get('spamwatch_api', None)
        self.CASH_API_KEY: str = self.parser.get('CASH_API_KEY', None)
        self.TIME_API_KEY: str = self.parser.get('TIME_API_KEY', None)
        self.WALL_API: str = self.parser.get('WALL_API', None)
        self.LASTFM_API_KEY: str = self.parser.get('LASTFM_API_KEY', None)
        self.CF_API_KEY: str =  self.parser.get("CF_API_KEY", None)
        self.bot_id = 0 #placeholder
        self.bot_name = "Naruse" #placeholder
        self.bot_username = "RendyTapiBot" #placeholder
        self.DEBUG: bool = self.parser.getboolean("IS_DEBUG", False)
        self.DROP_UPDATES: bool = self.parser.getboolean("DROP_UPDATES", True)
        self.BOT_API_URL: str = self.parser.get('BOT_API_URL', "https://api.telegram.org/bot")
        self.BOT_API_FILE_URL: str = self.parser.get('BOT_API_FILE_URL', "https://api.telegram.org/file/bot")

# SpamWatch

def init_sw(self):
        if self.spamwatch_api is None:
            log.warning("SpamWatch API key is missing! Check your config.ini")
            return None
        else:
            try:
                sw = spamwatch.Client(spamwatch_api)
                return sw
            except:
                sw = None
                log.warning("Can't connect to SpamWatch!")
                return sw

# nothing

sw = NUnit.init_sw()

# Variables 

NUnit = NaruseINIT(parser=nuconfig)

SYS_ADMIN = NUnit.SYS_ADMIN
OWNER_ID = NUnit.OWNER_ID
OWNER_USERNAME = NUnit.OWNER_USERNAME
APP_ID = NUnit.APP_ID
API_HASH = NUnit.API_HASH
WEBHOOK = NUnit.WEBHOOK
URL = NUnit.URL
CERT_PATH = NUnit.CERT_PATH
PORT = NUnit.PORT
INFOPIC = NUnit.INFOPIC
DEL_CMDS = NUnit.DEL_CMDS
ALLOW_EXCL = NUnit.ALLOW_EXCL
CUSTOM_CMD = NUnit.CUSTOM_CMD
# BAN_STICKER = NUnit.BAN_STICKER
TOKEN = NUnit.TOKEN
DB_URI = NUnit.DB_URI
LOAD = NUnit.LOAD
MESSAGE_DUMP = NUnit.MESSAGE_DUMP
GBAN_LOGS = NUnit.GBAN_LOGS
NO_LOAD = NUnit.NO_LOAD
SUDO_USERS = [OWNER_ID] + get_user_list("sudos")
DEV_USERS = [OWNER_ID] + get_user_list("devs")
SUPPORT_USERS = get_user_list("supports")
SARDEGNA_USERS = get_user_list("sardegnas")
WHITELIST_USERS = get_user_list("whitelists")
SPAMMERS = get_user_list("spammers")
spamwatch_api = NUnit.spamwatch_api
CASH_API_KEY = NUnit.CASH_API_KEY
TIME_API_KEY = NUnit.TIME_API_KEY
WALL_API = NUnit.WALL_API
LASTFM_API_KEY = NUnit.LASTFM_API_KEY
CF_API_KEY = NUnit.CF_API_KEY

# updater bot

from naruse.modules.sql import SESSION

if not NUnit.DROP_UPDATES:
    updater = tg.Updater(token=TOKEN, base_url=NUnit.BOT_API_URL, base_file_url=NUnit.BOT_API_FILE_URL, workers=min(32, os.cpu_count() + 4), request_kwargs={"read_timeout": 10, "connect_timeout": 10}, persistence=PostgresPersistence(session=SESSION))
    
else:
    updater = tg.Updater(token=TOKEN, base_url=NUnit.BOT_API_URL, base_file_url=NUnit.BOT_API_FILE_URL, workers=min(32, os.cpu_count() + 4), request_kwargs={"read_timeout": 10, "connect_timeout": 10})
    
telethn = TelegramClient(MemorySession(), APP_ID, API_HASH)
dispatcher = updater.dispatcher

# Load at end to ensure all prev variables have been set
from naruse.modules.helper_funcs.handlers import CustomCommandHandler

if CUSTOM_CMD and len(CUSTOM_CMD) >= 1:
    tg.CommandHandler = CustomCommandHandler


def spamfilters(text, user_id, chat_id):
    # print("{} | {} | {}".format(text, user_id, chat_id))
    if int(user_id) not in SPAMMERS:
        return False

    print("This user is a spammer!")
    return True
