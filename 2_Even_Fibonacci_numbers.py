#!/usr/bin/env

'''return sum of Fibbonaci numbers below max'''
max=4000000

fib=list()
fib.append(1) #first Fibbonaci number
fib.append(2) #second Fibbonaci number
n=2
stop=False
while(stop==False):
	val=fib[len(fib)-1]+fib[len(fib)-2]
	if(val<max):
		fib.append(val)
	else:
		stop=True

for i in range(0,len(fib)):
	if(fib[i]%2!=0):
		fib[i]=0

print 'Sum of all Fibbonaci numbers below max=%d is %d' %(max,sum(fib))
