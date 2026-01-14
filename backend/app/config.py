from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MONGODB_URL = os.getenv("URI") 
DB_NAME = "customer_support_kb"

if not GROQ_API_KEY:
    
    print("Warning: GROQ_API_KEY not set. Ensure it provides if using Groq models.")
    if not GOOGLE_API_KEY:
         raise RuntimeError("Neither GROQ_API_KEY nor GOOGLE_API_KEY/GEMINI_API_KEY set")


if not MONGODB_URL:
    raise RuntimeError("URI (MongoDB Connection String) not set. Please add it to .env")
