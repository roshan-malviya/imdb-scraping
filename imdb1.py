url='https://www.imdb.com/india/top-rated-indian-movies/'

from bs4 import BeautifulSoup as bs
from pprint import pprint 

import json

import requests


data=(requests.get(url)).text

soup=bs(data,'html.parser')


def top_movies_list():
    main_div=soup.find('div',class_="lister")
    tbody=main_div.find('tbody',class_="lister-list")
    tr_div=tbody.find_all('tr')

    movie_name=[]  #

    movie_year=[] #

    movie_rank=[] #

    movie_url=[] #

    movie_rating=[] #
    l=0

    for tr in tr_div:
        position=(tr.find('td',class_="titleColumn").get_text()).strip()
        
        rank=''
        for i in position:
            if '.' not in i:
                rank+=i
            else:
                break

        movie_rank.append(rank) 

        title=tr.find('td',class_="titleColumn").a.get_text()

        movie_name.append(title)  
        year=tr.find('span',class_="secondaryInfo").get_text()
        year=year[1:5]

        movie_year.append(year)

        ratings=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(ratings)

        url_=tr.find('td',class_='titleColumn').a['href']
        movie_url.append(url_)

        # return(year)

    main_movie_list=[]
    ll='https://www.imdb.com/'
    

    for n in range (len(movie_year)):
        main_movie_dict={'name':movie_name[n],'rank':movie_rank[n],'year':int(movie_year[n]),'ratings':float(movie_rating[n]),'url':(ll+movie_url[n])}


        main_movie_list.append(main_movie_dict)

    return(main_movie_list)







if __name__ == '__main__':
    movie_list=(top_movies_list())
    # pprint(top_movies_list())
    with open ('task1.json','w') as w:
        json.dump(movie_list,w,indent=4)







# # print(top_movies_list())











