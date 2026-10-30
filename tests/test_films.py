import sys
import os

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from playwright.sync_api import Page, expect

def test_get_films_returns_a_200():
    client = app.test_client()
    response = client.get("/films")
    assert response.status_code == 200

def test_films_route_returns_list_of_films(page: Page):
    page.goto('http://127.0.0.1:5001/films')
    films=page.locator('li')
    expected_films = [
        'Avatar - 2009',
        'Avengers: Endgame - 2019',
        'Spider-Man: Brand New Day - 2026',
        'Avatar: The Way of Water - 2022',
        'Titanic - 1997'
    ]
    
    actual_films = films.all_inner_texts()
    assert actual_films == expected_films