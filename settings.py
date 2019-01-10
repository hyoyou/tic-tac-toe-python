from dotenv import load_dotenv
import os

load_dotenv()

DB_ADDRESS = os.getenv("DB_ADDRESS")
TEST_DB_ADDRESS = os.getenv("TEST_DB_ADDRESS")