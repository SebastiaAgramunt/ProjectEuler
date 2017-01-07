#!/usr/bin/env python 

'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

#I'm going to use a backpropagation algorithm
import math

steps = []
#steps.append(np.array([4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]))
steps.append([63,66,04,68,89,53,67,30,73,16,69,87,40,31])
steps.append([91,71,52,38,17,14,91,43,58,50,27,29,48])
steps.append([70,11,33,28,77,73,17,78,39,68,17,57])
steps.append([53,71,44,65,25,43,91,52,97,51,14])
steps.append([41,48,72,33,47,32,37,16,94,29])
steps.append([41,41,26,56,83,40,80,70,33])
steps.append([99,65,04,28,06,16,70,92])
steps.append([88,02,77,73,07,63,67])
steps.append([19,01,23,75,03,34])
steps.append([20,04,82,47,65])
steps.append([18,35,87,10])
steps.append([17,47,82])
steps.append([95,64])
steps.append([75])

#let the previous step be the second row
prev = [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

for i,step in enumerate(steps):
	aux = []
	for j,step_elem in enumerate(step):

		#find maximum number we can sum
		candidate1 = prev[j] + step_elem
		candidate2 = prev[j+1] + step_elem

		if(candidate1>candidate2):
			aux.append(candidate1)
		else:
			aux.append(candidate2)
		#print len(aux)
	prev = aux

print "final %d" %(aux[0])















