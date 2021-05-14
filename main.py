import requests
import html5lib
from bs4 import BeautifulSoup


url = "https://www.imdb.com/list/ls069754038/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html5lib')




tabel = soup.find('div',attrs='article listo')

top_movies = []

for row in tabel.findAll('div',attrs={'class':'lister-item-content'}):
  movie = {}
  movie['movie name'] = row.h3.a.text
  movie['imdb rating'] = row.div.div.find_all('span')[1].text
  movie['movie categary'] = row.find('span',attrs={'class':'genre'}).text.replace("\n"," ")
  movie['casting'] = row.find_all('p')[2].text.replace("\n"," ")
  movie['Sort Description'] = row.find_all('p')[1].text.replace("\n"," ")
  movie['votes'] = row.find_all('p')[3].find_all('span')[1].text
  try:
    movie['Time Duration'] = row.find('span',attrs={'class':'runtime'}).text
  except:
    movie['Time Duration'] = "Web serios"
  
  top_movies.append(movie)

print(len(top_movies))
for i in top_movies:
  print(i)

