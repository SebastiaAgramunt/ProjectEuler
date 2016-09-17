'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''

import numpy as np

def palindrome(number):
	number=str(number)
	if number==number[::-1]:
		return True
	else:
		return False

palindromes=[]
nums_involved=[]
for i in range(999,99,-1):
	for j in range(999,99,-1):
		num=i*j
		if palindrome(num):
			print (i,j,num)
			palindromes.append(num)
			nums_involved.append([i,j])
pal=np.array(palindromes)
print pal.max()
#906609

pal=pal.tolist().index(pal.max())
print nums_involved[pal]
#[993, 913]

	



