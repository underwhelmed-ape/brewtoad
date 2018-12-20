#

# List of all recipes can be found at url
# https://www.brewtoad.com/recipes?page=1&sort=rank


# Go to page of recipes
# identify link to each individual recipe on that pages
# within that url, find link for xml file
# download xml
import requests
from contextlib import closing

# download webpage using requests
# this will gather the raw html file for each url specified

def get_html(web_page):
    try:
        with closing(requests.get(web_page)) as response:
            if check_response_is_html(response):
                return response.content
            else:
                return None
    except:
        print('Error during request to {0} : {1}'.format(web_page, str(e)))


# This takes a response and outputs True if html
# This only takes the repsonse and not the content
def check_response_is_html(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)
