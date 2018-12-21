# from the raw html files get thw information
import extract

from bs4 import BeautifulSoup

# at the moent this is just one htmls_list
# will need to loop through a list of htmls

htmls_list = extract.get_html('https://www.brewtoad.com/recipes?page=1&sort=rank')
html = BeautifulSoup(htmls_list, 'html.parser')


def get_recipe_urls_from_html(html):
    for i in html.select('a'):
        if i['class'] == 'recipe-link':
            print(i.text)

get_recipe_urls_from_html(html)
