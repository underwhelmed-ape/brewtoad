# from the raw html files get the information
import extract

from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# at the moment this is just one htmls_list
# will need to loop through a list of htmls

htmls_list = extract.get_html('https://www.brewtoad.com/recipes?page=1&sort=rank')

def get_recipe_urls_from_html(htmls_list):
    for link in BeautifulSoup(htmls_list, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            print(link['href'])

get_recipe_urls_from_html(htmls_list)
