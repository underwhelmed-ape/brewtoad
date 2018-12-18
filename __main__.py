
import extract


# for page get get_html
#
start_page = 1
end_page = 2

page = start_page

output_path = ''

url = 'https://www.brewtoad.com/recipes?page={page}&sort=rank'.format(page=1)

extract.get_html(url)



# go to page and get raw html code
# inside the html, get the links for each of the recipes pages
# for each recipe page, get the get_html
# in each recipe html, find the xml file download link
# download the xml into output_path
