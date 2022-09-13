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
from pyrogram import Client, errors
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
from pyrogram.types import Chat, User
from pyromod import listen

# CODE YOUR OWN HERE!
# DON'T ASK GROUP / PM

LOGGER = logging.getLogger('[naruse]')
LOGGER.info("naruse is starting. | Rendy Projects. | Licensed under GPLv3.")
LOGGER.info("Project maintained by: github.com/TeamKillerX (t.me/rencprx)")

# if version < 3.6, stop bot

# SpamWatch

# Load at end to ensure all prev variables have been set
