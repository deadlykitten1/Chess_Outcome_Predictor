from cmath import exp
from hashlib import new
from shutil import which
from bs4 import BeautifulSoup
import numpy as np
import requests
import pandas as pd

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
        opening_name = str(chunk.find_all('td')[0].find_all('a')[1].find_all('span')[1].text)
    except:
        print('Opening name nan')
        opening_name = np.nan

    try:
        opening = str(chunk.find_all('td')[0].find_all('a')[1].find_all('span')[0].text)
    except:
        print('Opening nan')
        opening = np.nan

    return white_player, white_player_rating, black_player, black_player_rating, result, game_length, year, opening_name, opening


def player_df_cleanup(row, name):
    """
    Helper function to transform our with our player's name in each column into just a df of their opponents' info
    Returns a row as a list with relevant information
    """
    new_row = []

    if row[0] == name: # player plays white
        new_row.append(row[1]) # opp
        new_row.append(1) # opp color (1 is black)
        new_row.append(row[3]) # opp rating
        new_row.append(row[2]) # player rating
    else: # plyaer plays black
        new_row.append(row[0]) # opp
        new_row.append(0) # opp color (1 is black)
        new_row.append(row[2]) # opp rating
        new_row.append(row[3]) # player rating

    # if wp == name: # player plays white
    #     new_row.append(bp) # opp
    #     new_row.append(1) # opp color (1 is black)
    #     new_row.append(bpr) # opp rating
    #     new_row.append(wpr) # player rating
    # else: # plyaer plays black
    #     new_row.append(wp) # opp
    #     new_row.append(0) # opp color (0 is white)
    #     new_row.append(wpr) # opp rating
    #     new_row.append(bpr) # player rating
    
    return new_row