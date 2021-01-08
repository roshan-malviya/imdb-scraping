import json
with open ('task4.json') as r:
    l=json.load(r)
c=[]
for i in l:
    for j in (i['languages']):
        if j not in c:
            c.append(j)
# print(c)
dic={}
for langauge in c:
    count=0
    for n in l:
        b=n['languages']
        if langauge in b:
            count+=1
    dic[langauge]=count
    
print (dic)
