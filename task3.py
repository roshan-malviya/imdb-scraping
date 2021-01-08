from imdb_task2 import movie_list_by_year
from imdb1 import top_movies_list
import json
from pprint import pprint

# defining funtion for 

def movies_by_decate(c):

    years=list(c.keys())
    first_decate_year=years[0]-(years[0]%10)

    decate_year=[]
    ll=0
    while ll<=len(years) :
        first_decate_year+=10

        decate_year.append(first_decate_year)
        if first_decate_year==years[-1]:
            break
        
        ll+=1
    # print(decate_year)

    main_dict={}

    for i in range(len(decate_year)-1):
        li=[]
        for j,valu in c.items():
            if j in range(decate_year[i],decate_year[i+1]):
                if type(valu)==list:
                    for ii in valu:
                        li.append(ii)
                else:
                    li.append(valu)
            main_dict[decate_year[i]]=li
    return(main_dict)


if __name__ == "__main__":
    b=top_movies_list()
    d=(movie_list_by_year(b))


    with open ('task3.json','w') as fl:
        k=movies_by_decate(d)
        json.dump(k,fl,indent=3)

        
