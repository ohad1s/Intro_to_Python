l_d=[{"name":"shrek1","director":"yossi","rank":9},
     {"name":"shrek2","director":"yossi","rank":7}
     ,{"name":"barbie","director":"dani","rank":2}]

res={}
for dicti in l_d:
    director=dicti["director"]
    movie_name=dicti["name"]
    if director not in res.keys():
        res[director]=[movie_name]
    else:
        res[director].append(movie_name)

print(res)

lst=["ohad","oaaao","aa","paaa"]
dicti2={}
for word in lst:
    dicti2[word]=0
    for char in word:
        if char=="a":
            dicti2[word]+=1
print(dicti2)


# for k, v in dicti2.items():
#     if v==maxi:
#         maxi_str.append(k)
#     elif v>maxi:
#         maxi_str=[k]
#         maxi = v

# print(maxi_str)

lst=["ohad","oaaao","aa","paaa"]
maxi=0
maxi_str=[]
for word in lst:
    counter=0
    for char in word:
        if char=="a":
            counter+=1
    if counter == maxi:
        maxi_str.append(word)
    elif counter > maxi:
        maxi_str = [word]
        maxi = counter
print(maxi_str)




