#

# List of all recipes can be found at url
# https://www.brewtoad.com/recipes?page=1&sort=rank


# Go to page of recipes
# identify link to each individual recipe on that pages
# within that url, find link for xml file
# download xml

# tabulate information:
# urls
#


from lxml import html
import requests
from requests.exceptions import RequestException
from contextlib import closing
from time import sleep
import json
import argparse
from collections import OrderedDict
from time import sleep
from bs4 import BeautifulSoup

# download webpage using requests
# this will gather the raw html file for each url specified

url = "https://www.brewtoad.com/recipes?page=1&sort=rank"
response = requests.get(url)
response = response.content

print(len(response))
