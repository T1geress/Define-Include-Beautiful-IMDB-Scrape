import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=tv_series,mini_series&num_votes=5000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f85d9bf4-1542-48d1-a7f9-48ac82dd85e7&pf_rd_r=NZR78MD1KBAVXZPG5PKK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_gnr_2'
page = requests.get(url)
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
