
'''Calculate '''
import time
import numpy

#return the n prime number
def n_prime_number(n):
	prime_numbers=list()
	x=2 #this is the first prime number
	prime_numbers.append(x) #add number two as first prime number
	while(len(prime_numbers)<n):
		isprime=True
		x=x+1
		#print "checking if: ",x," is prime"
		print "percentage calculated: ",float(len(prime_numbers))/float(n)*100
		for i in range(prime_numbers[0],prime_numbers[len(prime_numbers)-1]):
			if(x%i==0):
				isprime=False
				break
		if(isprime==True):prime_numbers.append(x)
	return(prime_numbers)

primes=n_prime_number(99999)
primes=numpy.array(primes)