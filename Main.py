from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "51e387f972011c9dfd8ba1cf27d991b0"
BASE_URL = "https://v3.football.api-sports.io"
headers = {
    "x-apisports-key": API_KEY
}

@app.get("/fixtures/today")
def get_today_fixtures():
    url = f"{BASE_URL}/fixtures?date=2025-10-07"
    response = requests.get(url, headers=headers)
    return response.json()

@app.get("/leagues")
def get_leagues():
    url = f"{BASE_URL}/leagues"
    response = requests.get(url, headers=headers)
    return response.json()

@app.get("/teams")
def get_teams():
    url = f"{BASE_URL}/teams?league=39&season=2025"
    response = requests.get(url, headers=headers)
    return response.json()

@app.get("/news")
def get_sports_news():
    news_api_key = "YOUR_NEWSAPI_KEY"
    news_url = f"https://newsapi.org/v2/top-headlines?category=sports&language=ar&apiKey={news_api_key}"
    response = requests.get(news_url)
    return response.json()

@app.get("/predict")
def predict_match(home: str, away: str):
    outcomes = [f"{home} سيفوز", f"{away} سيفوز", "تعادل"]
    prediction = random.choice(outcomes)
    return {"home": home, "away": away, "prediction": prediction}
