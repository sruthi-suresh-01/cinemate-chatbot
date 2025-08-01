import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# TMDB & OpenAI API keys
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_movie_recommendations(query):
    """
    Fetch movie suggestions from TMDB based on query.
    """
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "en-US",
        "page": 1,
        "include_adult": False
    }
    response = requests.get(url, params=params)
    results = response.json().get("results", [])
    return [movie["title"] for movie in results[:5]]

def generate_response(message_history):
    """
    Get AI response based on full chat history using OpenAI's ChatCompletion.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    return response.choices[0].message.content.strip()
