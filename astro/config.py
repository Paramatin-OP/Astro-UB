import os 
from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))


class Config(object):
    API_ID = int(os.environ.get("API_ID", 6)) 
    API_HASH = os.environ.get("API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "") 
    HNDLR = os.environ.get("HNDLR", r".")
    SUDO_HNDLR = os.environ.get("SUDO_HNDLR", r"\!")
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True") 
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "") 
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    NAME = os.environ.get("NAME", None)
    A_PIC = os.environ.get("A_PIC", None)
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "AstroUserBot")
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    MAX_MESSAGE_SIZE_LIMIT = 4095
    CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
    A_TEXT = os.environ.get("A_TEXT", None)
    PM_PIC = os.environ.get("PM_PIC", None)
    PM_TEXT = os.environ.get("PM_TEXT", None) 
    PMBOT_START_MSSG = os.environ.get("PMBOT_START_MSSG", None) 
    BOT_PIC = os.environ.get("BOT_PIC", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)
    UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
    PMSECURITY = os.environ.get("PMSECURITY", "ON") 
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
    MAX_SPAM = int(os.environ.get("MAX_SPAM", 4))
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "") 
    DB_URI = os.environ.get("DATABASE_URL", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    UPSTREAM_REPO_URL = "https://github.com/PsychoBots/ASTRO-UB"
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None) 
    if PRIVATE_GROUP_ID is not None:
       try:
           PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
       except ValueError:
           raise ValueError( 
               "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")
    FBAN_GROUP_ID = os.environ.get("FBAN_GROUP_ID", None) 
    if FBAN_GROUP_ID:
         FBAN_GROUP_ID = int(FBAN_GROUP_ID)
    EXCLUDE_FED = os.environ.get("EXCLUDE_FED", None)
      ###--ASTRO-CONFIGS--###
            ###---Astro-UB---###
        # Can be Added Some More Configs.
         

                
