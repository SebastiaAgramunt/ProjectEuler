#User Sebas12


'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''


#write a function first that tells you if a number is divisible by 3
def divthree(num):
	if(num%3==0):
		new=num;
	else:
		new=0;
	return(new);

def divfive(num):
	if(num%5==0):
		new=num;
	else:
		new=0;
	return(new);

def sumofnumbers(number):
	result=0
	for i in range(0,number):
		#print(i)
		if(i%5==0 or i%3==0):
			print(i)
			result=result+i
	return(result)








