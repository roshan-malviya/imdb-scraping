
# task8 and task 9 is in this file only

from imdb1 import top_movies_list
import os,requests,json,time,random
from bs4 import BeautifulSoup as bs

from task4 import movie_details_dict


b=top_movies_list()

for i in b:
    c=i['url']
    file_name=c[27:(len(c)-1)]+'.json'
    path=os.path.isfile('/home/navgurukul/Desktop/imdb scraper/chache'+file_name)
    if path:
        with open ('/home/navgurukul/Desktop/imdb scraper/chache'+file_name) as tr:
            n=json.load(tr)
            print (n)
    else:
        ti=random.randint(1,3)
        time.sleep(ti)
        d=movie_details_dict(c)
        with open ('/home/navgurukul/Desktop/imdb scraper/chache'+file_name,'w') as wr:
            json.dump(d,wr,indent=4)


print ("done")