from bs4 import BeautifulSoup
import requests


def cook_chess_soup(URL):
    """
    This is a helper function to fetch list entries from chess.com master game pages
    """
    #get html from page
    page = requests.get(URL)
    soup = BeautifulSoup(page._content, "html.parser")

    #get embedded tr divs in the list of games and store in the meats variable
    broth = soup.html.body.find('div', class_ = "base-layout").find('div', class_ = "base-container").main
    veggies = broth.find('div', class_ = "layout-column-one").find("div", class_ = "v5-section").find('div', class_ = "v5-section-content-wide").find_all('div', class_ = "post-preview-list-component")[2]
    noodles = veggies.find('div', class_ = 'master-games-table-responsive').table.tbody
    meats = noodles.find_all('tr')

    #return the data
    return meats
