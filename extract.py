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

import requests
from requests.exceptions import RequestException
from contextlib import closing


# download webpage using requests
# this will gather the raw html file for each url specified


def get_html(web_page):
    try:
        request = requests.get(web_page)
        response = request.content
        print('HTML request code: ' + str(request.status_code))
        print(len(response))
        return response
    except:
        log_error()

def check_response_is_html(response):
    content_type = response.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)
