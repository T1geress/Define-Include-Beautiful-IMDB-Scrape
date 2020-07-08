import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=tv_series,mini_series&num_votes=5000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f85d9bf4-1542-48d1-a7f9-48ac82dd85e7&pf_rd_r=NZR78MD1KBAVXZPG5PKK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_gnr_2'
csvfile = open("top50animated.csv", "w")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
csv_writer = csv.writer(csvfile)
csv_writer.writerow(['rank', 'name', 'length', 'genre', 'rating'])
results = soup.find("div", class_ = "lister-list")
movies = results.find_all("div", class_ = "lister-item")
for movie in movies:
  rank_elem = movie.find("span", class_ = "lister-item-index")
  names = movie.find("h3", class_ = "lister-item-header")
  name_elem = names.find("a")
  length_elem = movie.find("span", class_ = "runtime")
  genre_elem = movie.find("span", class_ = "genre")
  ratingbar = movie.find("div", class_ = "ratings-bar")
  rating_elem = ratingbar.find("strong")
  if None in (rank_elem, name_elem, length_elem, genre_elem, rating_elem):
      continue
  rank = rank_elem.text
  name = name_elem.text
  length = length_elem.text
  genre = genre_elem.text
  rating = rating_elem.text
  csv_writer.writerow([rank, name, length, genre, rating])
  print(rank, name, length, genre, rating)
  print()
csvfile.close()
