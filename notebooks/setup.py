import os 
import sys 
from pathlib import Path 
from dotenv import load_dotenv 
# ----------------------------- 
# PROJECT ROOT CONFIG 
# ----------------------------- 
PROJECT_ROOT = Path().resolve().parent 
os.chdir(PROJECT_ROOT) 
sys.path.append(str(PROJECT_ROOT)) 
# ----------------------------- 
# ENV VARIABLES 
# -----------------------------
load_dotenv() 
api_key = os.getenv("GOOGLE_API_KEY") 
# ----------------------------- 
# DATA LOADER 
# ----------------------------- 
from src.utils.loader import load_all 
data = load_all()

print("Setup done ✔") 
print("Current dir:", os.getcwd())