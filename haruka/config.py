
    


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1097031467:AAE0OH98dJ7SZVMAeDoY_hogfDVwNEQZOOk"
    OWNER_ID = "919262859" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Okay_retard"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://vjtzasvojzhwyf:f99e1fe2dacf75dc0c3c24de653a4ccee5e135784e935186f07e4ce21e597985@ec2-52-2-43-242.compute-1.amazonaws.com:5432/d515j6o8sbsj3d'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAQADCAADeuD5KZxa-Wzm9HeqAg'  # banhammer marie sticker
    STRICT_GBAN = True
    STRICT_GMUTE = True
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = None # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
