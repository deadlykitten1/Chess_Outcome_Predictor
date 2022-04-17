from cmath import exp
from shutil import which
from bs4 import BeautifulSoup
import numpy as np
import requests

def cook_chess_soup(URL):
    """
    This is a helper function to fetch list entries from chess.com master game pages
    """
    #get html from page
    page = requests.get(URL)
    soup = BeautifulSoup(page._content, "html.parser")

    #get embedded tr divs in the list of games
    broth = soup.html.body.find('div', class_ = "base-layout").find('div', class_ = "base-container").main
    veggies = broth.find('div', class_ = "layout-column-one").find("div", class_ = "v5-section").find('div', class_ = "v5-section-content-wide").find_all('div', class_ = "post-preview-list-component")[2]
    noodles = veggies.find('div', class_ = 'master-games-table-responsive').table.tbody
    meats = noodles.find_all('tr')

    #return the data
    return meats


def get_chess_data(chunk):
    """
    Given a list element from Chess.com's master game webpage, grab and return relevent data in a dictionary
    This function is hella ugly but whatever
    """
    try:
        white_player = str(chunk.find_all('td')[0].find_all('a')[0].find_all('div')[0].find_all('span')[0].string)
    except:
        print('White player nan')
        white_player = np.nan

    try:
        white_player_rating = str(chunk.find_all('td')[0].find_all('a')[0].find_all('div')[0].find_all('span')[1].string)
    except:
        print('White player rating nan')
        white_player_rating = np.nan

    try:
        black_player = str(chunk.find_all('td')[0].find_all('a')[0].find_all('div')[1].find_all('span')[0].string)
    except:
        print('Black player nan')
        black_player = np.nan

    try:
        black_player_rating = str(chunk.find_all('td')[0].find_all('a')[0].find_all('div')[1].find_all('span')[1].string)
    except:
        print('Black player rating nan')
        black_player_rating = np.nan

    try:
        result = str(chunk.find_all('td')[1].find_all('a')[0].string)
    except:
        print('Result nan')
        result = np.nan

    try:
        game_length = str(chunk.find_all('td')[2].find_all('a')[0].string)
    except:
        print('Game length nan')
        game_length = np.nan

    try:
        year = chunk.find_all('td')[3].find('a')['title']
    except:
        print('Year nan')
        year = np.nan

    try:
        game = str(chunk.find_all('td')[0].find_all('a')[1].find_all('span')[1].text)
    except:
        print('Game nan')
        game = np.nan

    return white_player, white_player_rating, black_player, black_player_rating, result, game_length, year, game