
import extract
import transform
import os

start_page = 1
end_page = 1

recipe_page = start_page

# create empty list for individual recipe urls to be saved in
recipe_links = []

# local path for xml files to be saved in
output_path = ''
print(output_path)

while recipe_page <= end_page:
# go to page and get raw html code
    url = 'https://www.brewtoad.com/recipes?page={page}&sort=rank'.format(page=recipe_page)
    response = extract.get_html(url)

    print(len(response))
    print(type(response))
    print(url)

# inside the html, get the links for each of the recipes pages
    recipe_links = transform.get_recipe_urls_from_html(response)
    recipe_links = recipe_links.append()

# increase page number by one before returning to start of loop
    recipe_page = recipe_page + 1





# for each recipe page, get the get_html
# in each recipe html, find the xml file download link
# download the xml into output_path
