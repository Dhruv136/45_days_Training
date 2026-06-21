ls=[1,3,4,]
print(ls)
ls=['d','h','r','u','v']

print(ls[0])

print(ls[0:3])
ls.append(100)

print(ls)

ls.insert(1,'lilani')
print(ls)
ls.pop(0)
print(ls) 

ls.reverse()
print(ls)


# ls.clear()
# print(ls)

ls.copy()
print(ls)

ls2=[2,4,5,4,3,32,3]
ls2.sort()
print(ls2)
print(ls+ls2)

#   << tuple >>>>


tu =(1,2,3,4,5)
print(tu)
#    <<< dictionary >>>>>

di = { "name" : "dhruv", "age" : 18, "phonenumber": "9588230587"}
print(di["name"])
print(di["age"])
print(di["phonenumber"])
print(di.keys())
print(di.values())
print(di.items())
for key,value in di.items():
    print(key,value)
dh={
"dhruv":{
    "age":20,
    "branch":"backchodi"
},"chinu":{
    "age":32,
    "branch":"hueubds"
}
}
print( dh["chinu"]["branch"])
print(dh["dhruv"]["age"])