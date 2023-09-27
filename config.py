from os import getenv
from data import THE_ALTS


#----------------------------------- REQUIRED CODES --------------------------------------#

API_ID = int(getenv("API_ID", "21188581"))
API_HASH = getenv("API_HASH", "039f5147df0a29288b48dda1a9c01ec5")
SESSION1 = getenv("SESSION")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/50131d5f2ff665829effe.jpg")
OWNER_ID = int(getenv("OWNER_ID", "5129320633"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")


#-------------------------------- OPTIONAL -------------------------------------#

SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")
SESSION6 = getenv("SESSION6")
SESSION7 = getenv("SESSION7")
SESSION8 = getenv("SESSION8")
SESSION9 = getenv("SESSION9")
SESSION10 = getenv("SESSION10")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", "1918848221").split(" ")))
SUDO_USERS.append(OWNER_ID)

for x in THE_ALTS:
    SUDO_USERS.append(x)

SESSIONS = [SESSION1, SESSION2, SESSION3, SESSION4, SESSION5, SESSION6, SESSION7, SESSION8, SESSION9, SESSION10]
