import json
with open ('task4.json') as r:
    l=json.load(r)
c=[]
for i in l:
    for j in (i['diractors']):
        if j not in c:
            c.append(j)
# print(c)
dic={}
for diractor in c:
    count=0
    for n in l:
        b=n['diractors']
        if diractor in b:
            count+=1
    dic[diractor]=count
    
print (dic)
