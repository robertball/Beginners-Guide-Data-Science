import requests
link = 'https://icarus.cs.weber.edu/~rball/book_files/example_recipe_page.html'
response = requests.get(link, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'})  # get the webpage

lines = response.text.split('\n')  # divide the text into a list
for line in lines:
    line = line.strip()  # strip out the white space
    if '<span class="ingredients-item-name">' in line:
        print(line)
