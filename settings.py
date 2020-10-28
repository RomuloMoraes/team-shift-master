import os
from dotenv import load_dotenv

load_dotenv()

USER_EMAIL = os.getenv('USER_EMAIL', default='email@email.com')
USER_PASSWORD = os.getenv('USER_PASSWORD', default='password')
SYSTEM_TYPE = os.getenv('SYSTEM_TYPE', default=64)
