#!/usr/bin/env
# -*- coding: utf-8 -*-
"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

import numpy as np

def ispalindrome(number):
	'''Function that takes a number and returns true if it is palindrome'''
	number=str(number)
	if number==number[::-1]:
		return True
	else:
		return False

#compute all products starting by 999 x 999 and then get the max.

def largest_palindrome(longitude):
	palindromes=[]
	nums_involved=[]
	n2=int(''.join([str(9) for x in range(0,longitude)]))
	n1=int(''.join([str(9) for x in range(0,longitude-1)]))
	for i in range(n2,n1,-1):
		for j in range(n2,n1,-1):
			num=i*j
			if ispalindrome(num):
				palindromes.append(num)
				nums_involved.append([i,j])
	pal=np.array(palindromes,dtype=np.int64)
	return pal.max()
#906609
#[993, 913]


n=3 #three digit
print "Largest palindrome number made from product of %d digit numbers is %d" %(n,largest_palindrome(n))