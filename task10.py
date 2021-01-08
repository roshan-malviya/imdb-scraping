from task4 import movie_details_dict
from pprint import pprint 
# from imdb1 import top_movies_list


import json
def lanAndDir_analysis():
    with open ('task4.json') as r:
        b=json.load(r)
    diractor=[]
    for i in b:
        for j in i['diractors']:
            if j not in diractor:
                diractor.append(j)
    main_dic={}
    for l in diractor:
        o=[]
        for di in b:
            if l in di['diractors']:
                o+=di['languages']
            else:
                continue
        pd=set(o)
        main_dic[l]={mn:o.count(mn) for mn in pd}
    return (main_dic)
if  __name__ == "__main__":
    klpd=lanAndDir_analysis()
    with open ('task10.json','w') as wr:
        json.dump(klpd,wr,indent=3)