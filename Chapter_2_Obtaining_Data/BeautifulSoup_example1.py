import requests
from bs4 import BeautifulSoup
link = 'https://icarus.cs.weber.edu/~rball/book_files/example_recipe_page.html'
response = requests.get(link, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'})

soup = BeautifulSoup(response.text, 'html.parser')
ingredients = soup.find_all('span', class_='ingredients-item-name')
for ingredient in ingredients:
    print(ingredient)
