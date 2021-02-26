from imdb1 import top_movies_list
from pprint import pprint 
import json

def movie_list_by_year(b):
	sorted_year=[]

	for i in range (len(b)):
		if i not in sorted_year:
			sorted_year.append(b[i]['year'])

	# sorted_year=list(set(c))

	sorted_movie_list=[]

	movies={}
	# print (b)
	for ii in sorted_year:
		item_list=[]
		for movie in b:
			if ii == movie['year']:
				item_list.append(movie)
		movies[ii]=item_list
	return(movies)






if __name__ == "__main__":
	l=[]
	b=top_movies_list()
	
	c=(movie_list_by_year(b))
	# l.append(c)
	with open ('task22.json','w') as w:
		json.dump(c,w,indent=4)
		w.close()
# pprint(movie_list_by_year(b))







		

