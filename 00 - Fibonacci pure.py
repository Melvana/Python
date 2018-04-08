#Print first Fibonacci greater than 'x' digits long
a,b=1,1
i=1
#change to < for number
while(len(str(a))<=4):
  i=i+1
  a,b=b,a+b
#i=number in the list, str=digits long,a= actual fib number
print i,len(str(a)),a
