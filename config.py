from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29162926")
    API_HASH = environ.get("API_HASH", "717d5ca64b70f7a8b3d2e2ceac60c3e0")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7653119604:AAHLQ89tqRbcA_yBe68CkHVtTv0BbKPrRDE") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7613114681').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
