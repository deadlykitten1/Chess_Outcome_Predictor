from cmath import exp
from hashlib import new
from shutil import which
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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

    try:
        game_link = str(chunk.find_all('td')[0].find_all('a')[0]['href'])
    except:
        print('Game link nan')
        game_link = np.nan

    return white_player, white_player_rating, black_player, black_player_rating, result, game_length, year, opening_name, opening, game_link


def cook_chess_game_soup(URL):
    """
    This is a helper function to fetch information from a chess.com game page
    """
    # #get html from page
    # page = requests.get(URL)
    # soup = BeautifulSoup(page._content, "html.parser")

    # #fetch the data from the page
    # broth = soup.html.body.find('div', id = 'board-layout-sidebar')#.find_all('div')[0].find_all('div')[1].find_all('div')


    driver = webdriver.Chrome('./chromedriver') 
    driver.get(URL)

    time.sleep(10) # to ensure the page and analysis loads 
    
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")

    #fetch the data from the page
    broth = soup.html.body.find('div', id = 'board-layout-sidebar').find_all('div')[0].find_all('div')[1]
    veggies = broth.find_all('div')[0].find('div', class_ = 'review-view-main review-scroll-container')
    meats = veggies.section.div

    # white_acc = float(meats.find('div', class_ = 'accuracy-score-component accuracy-score-white').div.div.text)
    # black_acc = float(meats.find('div', class_ = 'accuracy-score-component accuracy-score-black').div.div.text)

    white_acc = meats.find_all('div')[0]#.div.div.text)
    black_acc = meats.find_all('div')[1]#.div.div.text)

    print(white_acc)
    print(black_acc)