from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
IIKO_URL = os.getenv('IIKO_URL', '')
IIKO_TOKEN = os.getenv('IIKO_TOKEN', '')
COMPANY_ID = os.getenv('COMPANY_ID', '')
