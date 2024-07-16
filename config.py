from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("29305295"))
API_HASH = getenv("6838cc67172f18fe5f302c158ce2fbfa")

BOT_TOKEN = getenv("6427389576:AAE3GnIV4azq8o0uY8v2TptmP9LXFj4QB5U")
OWNER_ID = int(getenv("7083782157"))

MONGO_DB_URI = getenv("mongodb+srv://jarij2216:buburayam1@cluster0.uueck7c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("BestieVirtual", "Nenen_degrees")
