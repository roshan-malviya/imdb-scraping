import json


with open ('task4.json') as r:
    b=json.load(r)

gernes=[]
for i in b:
    gernes+=i['gerne']
sorted_gerne=set(gernes)
ml={}
for j in sorted_gerne:
    ml[j]=gernes.count(j)
print(ml)



    
