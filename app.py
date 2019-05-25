import requests   #import module

from bs4 import BeautifulSoup  # import beautiful soup libary

url = 'https://www.apple.com/'

r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html)


edited = soup.prettify()  # this edits the website to a readable format



