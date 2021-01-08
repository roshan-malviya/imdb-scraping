from imdb1 import top_movies_list 
import json
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

b=top_movies_list()
# print (b)



def movie_details_dict(url):
    b=(requests.get(url)).text
    soup=bs(b,'html.parser')
    movie={}

    div_4_n_t_g=soup.find('div',class_='title_wrapper')
    name=div_4_n_t_g.find('h1').get_text(strip=True)

    l=''
    for i in name:
        if i=='(':
            break
        else:
            l+=i
    name_=l
    sub=div_4_n_t_g.find('div',class_='subtext')
    a_tag=sub.find_all('a')

    time=(sub.find('time').text).strip()
    # print (time)

    gern=[(a_tag[n].text) for n in range(len(a_tag)-1)]

    # print (gern)

    div_4_s_d=soup.find('div',class_='plot_summary')
    summar=(div_4_s_d.find('div',class_='summary_text').text).strip()

    # print(summar)

    diractor_div=(div_4_s_d.find('div',class_='credit_summary_item')).find_all('a')

    diractor=[i.get_text() for i in diractor_div]

    # print(diractor)

    poster_div=(soup.find('div',class_='poster')).find('img')['src']

    # print (poster_div)




    div_4_c_l=soup.find('div',id='titleDetails')

    c=div_4_c_l.find_all('div',class_="txt-block")
    langauges=[]
    for i in range(len(c)):
        if (c[i].find('h4').text)=='Country:':
            Country=c[i].find('a').text
            langauge=c[i+1].find_all('a')
            for kl in langauge:
                langauges.append(kl.text)

            break



    movie['name']=name_
    movie['run time']=time
    movie['gerne']=gern
    movie['summary']=summar
    movie['diractors']=diractor
    movie['poster']=poster_div
    movie['Country']=Country
    movie['languages']=langauges


    return movie


# url='https://www.imdb.com/title/tt0066763/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=DR4DYTMQTQW8AS60SQC2&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_17'

# print (movie_details_dict(url))







# print(movie_detail_list)



if  __name__ == "__main__":
    movie_detail_list=[]
    p=1
    for i in b:
        data=i['url']

        movie_info=movie_details_dict(data)
        movie_detail_list.append(movie_info)
        print(p)
        # pprint(movie_detail_list)
        p+=1
        # break

    with open ('task4.json','w') as bb:
        json.dump(movie_detail_list,bb,indent=4)

    print ('done')


