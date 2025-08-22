x=15
if x==5:
    print(x)
if x==9:
    print("yes")
if x== 'Abhi':
    print("yes")
if x==15:
    print('no')

l=['apple','banana','guvava','graps','litchi']
p=[]
for i in l:
    if 'a' in i:
        p.append(i)
print(p)

#tis is one line code for upper code    
newlist=[i for i in l if 'n' in i]
print(newlist)

#To create the list
list=[x for x in range(100)]
print(list)

#to reverse the list 
#we can use the .reverse funvtion also
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

#to copy the list we use this
o=[x for x in range(10)]
u=o.copy()
print(o)

