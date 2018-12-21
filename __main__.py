import extract
import transform
import os

start_page = 1
end_page = 1

current_recipe_page = start_page

# create empty list for individual recipe urls to be saved in
recipe_links = []

# local path for xml files to be saved in
#print(output_path)

# Loop through each `all_recipe_pages`
while current_recipe_page <= end_page:

    # add current recipe page to url
    all_recipe_pages = 'https://www.brewtoad.com/recipes?page={page}&sort=rank'.format(page=current_recipe_page)

    # at each page use `get request` to bring back raw html
    response = extract.get_html(all_recipe_pages)

    # extract links to each recipe from recipe-container
    recipe_link = 'test'
    # append this information to recipe_links list
    recipe_links = recipe_links.append(recipe_link)

    for i in recipe_links:
        output_path = 'base_path/{i}'.format(i)
        if not os.path.isfile(output_path): # if file is not in the given dir
            print('Downloading data at ' + output_path)
            try:
                # bring back
                extract.get_html()
                # inside the html, get the links for each of the recipes pages
                recipe_links = transform.get_recipe_urls_from_html(response)
                transform.save_output_to_file(response, output_path)
            except:
                print('Recipe file for ' + str(i) + ' not found')
        else: # if file is in given dir
            print('File already exists')

# increase page number by one before returning to start of loop
current_recipe_page = current_recipe_page + 1


print(recipe_links)


# for each recipe page, get the get_html
# in each recipe html, find the xml file download link
# download the xml into output_path
