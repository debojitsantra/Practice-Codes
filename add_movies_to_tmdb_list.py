import pandas as pd
import requests
import time

ACCESS_TOKEN = ""
LIST_ID = ""

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json;charset=utf-8"
}

def search_tmdb_id(title, year):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"query": title, "include_adult": "false"}
    r = requests.get(url, params=params)
    results = r.json().get("results", [])
    
    
    for movie in results:
        if "release_date" in movie and movie["release_date"].startswith(str(year)):
            return movie["id"]
    
   
    if results:
        print(f" Year mismatch for: {title} — using fuzzy match → {results[0]['title']} ({results[0].get('release_date', 'N/A')})")
        return results[0]["id"]

    return None

def add_to_list(movie_id):
    url = f"https://api.themoviedb.org/4/list/{LIST_ID}/items"
    payload = {
        "items": [
            {"media_type": "movie", "media_id": movie_id}
        ]
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    return r.status_code, r.text

df = pd.read_csv("watched.csv")

for i, row in df.iterrows():
    title, year = row["Name"], int(row["Year"])
    print(f" Searching: {title} ({year})")
    tmdb_id = search_tmdb_id(title, year)
    if tmdb_id:
        status, msg = add_to_list(tmdb_id)
        if status == 201:
            print(f" Added: {title}")
        else:
            print(f" Add failed: {title} → {status} {msg}")
    else:
        print(f" Not found on TMDb: {title} ({year})")
    time.sleep(0.3)