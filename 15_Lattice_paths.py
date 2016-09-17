
'''Calculate combiantions of 40 in 20 and 20'''
import time
import numpy
#write a function first that tells you if a number is divisible by 3
def factorial(n):
	if(n==1):
		return n
	else:
		return(n*factorial(n-1))

factorial(4)

print factorial(40)/(factorial(20)*factorial(20))
