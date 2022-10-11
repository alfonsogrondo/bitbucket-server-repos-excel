# settings.py
## import the dotenv module
from dotenv import load_dotenv

from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# get all the keys needed for the project
USERNAME = os.getenv("USERNAME")
BB_API_URL = os.getenv("BB_API_URL")
PASSWORD = os.getenv("PASSWORD")
EXCEL_OUTPUT_DIRECTORY = os.getenv("EXCEL_OUTPUT_DIRECTORY")
