from turtle import ht
from bs4 import BeautifulSoup # for beautiful soup
import requests

# to prevent a 403 error
headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

print(doc.select('.heading-financier'))