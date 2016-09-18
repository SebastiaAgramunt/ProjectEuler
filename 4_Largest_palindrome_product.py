#!/usr/bin/env
# -*- coding: utf-8 -*-
"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

import numpy as np

def palindrome(number):
	'''Function that takes a number and returns true if it is palindrome'''
	number=str(number)
	if number==number[::-1]:
		return True
	else:
		return False

#compute all products starting by 999 x 999 and then get the max.

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
#[993, 913]