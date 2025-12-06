
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Secret key for JWT and other secure operations
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretjwtkey")

# Optional: other configs
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://chanchal:password@localhost:5432/smartnotes")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://chanchal:password@db:5432/smartnotes")
