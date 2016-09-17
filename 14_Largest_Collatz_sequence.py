
'''Calculate '''
import time
import numpy
#write a function first that tells you if a number is divisible by 3
def collatz_seq(n):
	#first calculate the sequence
	x=n
	a=list()
	a.append(n)
	while x!=1:
		if(x%2==0):
			a.append(x/2)
			x=x/2
		else:
			a.append(3*x+1)
			x=3*x+1
		#print(a)
		#time.sleep(2)
	return(a) 
solution=collatz_seq(13)

length_seq=list()
for i in range(1,1000000,1):
	length=len(collatz_seq(i))
	length_seq.append(length)
	print(i)

length_seq=numpy.array(length_seq)

#the max is:
length_seq.max()
m = max(length_seq)
[i for i, j in enumerate(length_seq) if j == m]

#the answer is the output number +1
#this is:
#837799