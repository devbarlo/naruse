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
