# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7658357765:AAFNojY3QWjcLUvT17D5RYv1ZQFwhSQHCEA")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26728872"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "96985c2aaea6c75408528909b7e18879")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002343892805"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Itsme123i")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1705634892"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://telegramguy21:tnkIwvbNkJ5U3fZ7@botsuse.bpgag.mongodb.net/?retryWrites=true&w=majority&appName=Botsuse")
DB_NAME = os.environ.get("DATABASE_NAME", "Not2Worry")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "0"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002169827133"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002347470858"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/lllex3.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://files.catbox.moe/uhdylt.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "False") == "True" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 0)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")


HELP_TXT = "<b>Greetings!</b>\n\n𝙸'𝚖 𝚊 𝚜𝚞𝚙𝚎𝚛𝚌𝚑𝚊𝚛𝚐𝚎𝚍 💾 𝚊𝚗𝚒𝚖𝚎 𝚏𝚒𝚕𝚎 𝚋𝚘𝚝, 🤖 𝚑𝚊𝚗𝚍𝚕𝚒𝚗𝚐 𝚞𝚙𝚕𝚘𝚊𝚍𝚜 𝚠𝚒𝚝𝚑 𝚎𝚊𝚜𝚎! ✨ 𝑰'𝒎 𝒑𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 <a href='https://t.me/Animes_Guy'>𝗔𝗻𝗶𝗺𝗲 𝗚𝘂𝘆!!</a> 😉.𝙸 𝚘𝚗𝚕𝚢 𝚜𝚝𝚘𝚛𝚎𝚍 𝚌𝚘𝚖𝚙𝚕𝚎𝚝𝚎𝚍 𝚊𝚗𝚒𝚖𝚎 𝚏𝚒𝚕𝚎𝚜 😁 𝙸𝚗 𝚕𝚘𝚠 𝚖𝚋.\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ"

ABOUT_TXT = "‣ Mʏ ᴜsᴇʀɴᴀᴍᴇ: <a href='https://t.me/ErenXJaegerbot'>𝙴𝚛𝚎𝚗 𝚈𝚎𝚊𝚐𝚎𝚛</a>\n\n‣ Cʜᴀɴɴᴇʟ I ᴡᴏʀᴋ ғᴏʀ: <a href='https://t.me/Animes_Guy'>𝙰𝚗𝚒𝚖𝚎𝚜 𝙶𝚞𝚢!!</a>\n\n‣ Cʀᴇᴀᴛᴏʀ ᴏғ ᴍᴇ: <a href='https://t.me/The_TGguy'>𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙶𝚞𝚢!!</a>\n\n‣ Dᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/'>𝙼𝚘𝚗𝚐𝚘 𝙳𝙱</a>\n\n‣ Pʀᴏɢʀᴀᴍᴍᴇᴅ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>𝙿𝚢𝚝𝚑𝚘𝚗</a>\n\n‣ Hᴏsᴛᴇᴅ Oɴ: <a href='https://www.heroku.com/'>𝙷𝚎𝚛𝚘𝚔𝚞</a>"

START_MSG = os.environ.get("START_MESSAGE", "<b>Greetings!</b>\n\n𝙸𝚖 𝚊 𝚜𝚞𝚙𝚎𝚛𝚌𝚑𝚊𝚛𝚐𝚎𝚍 💾 𝚊𝚗𝚒𝚖𝚎 𝚏𝚒𝚕𝚎 𝚋𝚘𝚝, 🤖 𝚑𝚊𝚗𝚍𝚕𝚒𝚗𝚐 𝚞𝚙𝚕𝚘𝚊𝚍𝚜 𝚠𝚒𝚝𝚑 𝚎𝚊𝚜𝚎! ✨ 𝑰'𝒎 𝒑𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 <a href='https://t.me/Animes_Guy'>𝗔𝗻𝗶𝗺𝗲 𝗚𝘂𝘆!!</a> 😉.𝙸 𝚘𝚗𝚕𝚢 𝚜𝚝𝚘𝚛𝚎𝚍 𝚌𝚘𝚖𝚙𝚕𝚎𝚝𝚎𝚍 𝚊𝚗𝚒𝚖𝚎 𝚏𝚒𝚕𝚎𝚜 😁 𝙸𝚗 𝚕𝚘𝚠 𝚖𝚋.")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "1705634892").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ!\n\nTᴏ ʜᴇʟᴘ ᴘʀᴇᴠᴇɴᴛ sᴘᴀᴍ ᴏɴ ᴏᴜʀ ʙᴏᴛs, ᴏɴʟʏ ᴜsᴇʀs ᴡʜᴏ ᴀʀᴇ ᴍᴇᴍʙᴇʀs ᴏғ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀʀᴇ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ. Tᴏ ᴀᴄᴄᴇss ʏᴏᴜʀ ғɪʟᴇs, ᴘʟᴇᴀsᴇ ɪᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ʟɪsᴛᴇᴅ ʙᴇʟᴏᴡ ᴀɴᴅ ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
