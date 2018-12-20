
import extract
import os


# for page get get_html
#
start_page = 1
end_page = 2

recipe_page = start_page


output_path = ''

while recipe_page <= end_page:
    try:
        url = 'https://www.brewtoad.com/recipes?page={page}&sort=rank'.format(page=recipe_page)

        response = extract.get_html(url)

        print(url)
    except:
        print('Cannot return url')

    recipe_page = recipe_page + 1



# go to page and get raw html code
# inside the html, get the links for each of the recipes pages
# for each recipe page, get the get_html
# in each recipe html, find the xml file download link
# download the xml into output_path
