#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Write a Python script to download IMDB 250 Top Rated Movies.
# For each movie, you'll need to retrieve the movie title, the ranking, the initial release year, the casting and 
# the rating.
# Your data must be stored in a proper imdb_top_250.csv file.

import requests, csv
from bs4 import BeautifulSoup

def get_movies(url):
    response = requests.get(url)
    soup_imdb = BeautifulSoup(response.text)

    all_movies = soup_imdb.find_all("td", {"class":"titleColumn"})

    # get movie title :
    titles = []
    for title in all_movies:
        title = title.get_text().strip()
        titles.append(title[1])

    # get ranking :
    all_rankings = soup_imdb.find_all("td", {"class":"titleColumn"})
    rankings = []
    for rank in all_rankings:
        rank = rank.get_text().strip()
        rankings.append(rank[0])

    # get release year :
    list_year = soup_imdb.find_all("td", {"class":"titleColumn"})
    years = []
    for year in list_year:
        year = year.get_text().strip()
        years.append(year[2])

    # get casting :
    castings = soup_imdb.find_all("td", {"class":"titleColumn"})
    casting = []
    for cast in castings:
        casting.append('not sure')

    #get rating :
    list_ratings = soup_imdb.find_all("td", {"class":"ratingColumn imbdRating"})
    ratings = []
    for rating in list_ratings:
        rating = rating.get_text().replace('\n', "")
        ratings.append(rating)
        
    ugly_list = [element.text.strip("\n") for element in list_ratings]
    ratings = [element for element in ugly_list if ugly_list.index(element) % 2 == 0]

    mega_list = list(zip(titles, rankings, years, castings, ratings))
    mega_list = [list(elt) for elt in mega_list]

    # Write csv
    str_lst = [f"{mega_list[i][1]} / {mega_list[i][0]} ({mega_list[i][2]}) / Starring: {mega_list[i][3]}"     for i, val in enumerate(mega_list)]

    res = [elt.split("/") for elt in str_lst]

    with open("imdb_top_250.csv", "w") as f:
        writer = csv.writer(f, delimiter="-")
        writer.writerows(res)


# In[24]:


def main():
    url = "https://www.imdb.com/chart/top"
    get_movies(url)
    

if __name__ == "__main__":
    main()


# In[25]:


import pandas as pd

df = pd.read_csv('imdb_top_250.csv')
df.head(5)
#Read CSV and show the first 5 rows


# In[ ]:




