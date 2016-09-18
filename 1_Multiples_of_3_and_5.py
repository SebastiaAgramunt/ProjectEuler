#User Sebas12


'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''

#function that outputs sum of numbers divisible by 3 or 5 that are less than "number"
def sumofnumbers(number):
	result=0
	for i in range(0,number):
		#print(i)
		if(i%5==0 or i%3==0):
			result=result+i
	return(result)

print "sum of all the multiples of 3 or 5 below 1000 is: %d" %(sumofnumbers(1001))







