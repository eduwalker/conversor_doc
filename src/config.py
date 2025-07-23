import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TOKEN_API_CONVERSAO", "TOKEN_PADRAO_SEGURO")
