#  tuple is immutable , allow duplicate , hetergeneous ,ordered

tpl=(1,2,3,4,"hello","hii")
print("this is my tuple",tpl)
print("len is my tuple",len(tpl))
print("type of my tuple",type(tpl))
print(tpl.count('hello'))
print(tpl.index('hello'))

# <<<<<< tuple collection >>>>>>>>>>>>>>

a = 1,2,3,4,5,33,4,5,"hello","hi" 
# if we write like this it will be automatically stored as tuple as u can see in op
print(a)
print(type(a))
print(len(a))

#  <<<<<<<< tuple unpacking >>>>>>>>>>>>
a,b,c= (1,2,3)
print(a)
print(b)
print(c)
 
#   typecasting in python 

t=(1,2,3,4)
print(t)
print("type of tuple", type(t))
lst=list(t)
print(lst)
print("type of list", type(lst))
t=tuple(lst)
print("list is now converted back into tupple",t)
print( "type of tuple",type(t))



