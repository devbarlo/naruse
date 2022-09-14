# This file is a part of < https://github.com/TeamKillerX/naruse/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamKillerX/naruse/blob/dev22/LICENSE/

import importlib
import re
import threading
from sys import argv
from typing import Optional

from telegram import Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)
from telegram.ext import (
    CallbackContext,
    Filters
)
from telegram.ext.dispatcher import DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

from naruse import (
    NUnit,
    dispatcher,
    updater,
    TOKEN,
    WEBHOOK,
    OWNER_ID,
    CERT_PATH,
    PORT,
    URL,
    log,
    telethn,
    NaruseINIT
)

# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from naruse.modules import ALL_MODULES
# from naruse.modules.helper_funcs.chat_status import is_user_admin
# from naruse.modules.helper_funcs.decorators import 
# from naruse.modules.helper_funcs.misc import paginate_modules
from naruse.modules.language import gs

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []

CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("naruse.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "get_help") and imported_module.get_help:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module
