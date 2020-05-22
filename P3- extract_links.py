#Extracting all the links from a given text file


import re

with open('1.html', encoding='utf-8') as f:
    text = f.read()

href_regex = r'href=[\'"]?([^\'" >]+)'
urls = re.findall(href_regex, text)

print(urls)       

