import random

while True:
    r=random.randint(1,10)
    print(r)
    if r==8:
        break

# dont print multiple of 3 here
c=0  #to check number of times running loop
for i in range(2,100,2):
   if i%3 == 0:
    c=c+1
    continue
   
   print(i,end=' ')
print(c)

num=int(input('put a number'))
isPrime = True
for i in range(2,num):
    if num%i == 0 :
        isPrime= False
        break

if isPrime or num==2 :
    print('its prime number')
else:
    print('its not prime')
