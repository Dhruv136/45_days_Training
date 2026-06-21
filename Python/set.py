s={1,2,3,3,4,"hello","hii","dkpsycho"}
print(s)
print("this is my set :-",s)
print("type of my set:-",type(s))
print("len of my set:-",len(s))
s.add(202)
print(s)
a={1,2,3,4}
b={2,3,42}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))
# s[0]=10 this will give error because item assignment is not supporetd in set
# print(s)