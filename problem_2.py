#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:25:19 2018

@author: Rohit Swami

Question:
Ten students (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10) are going to attend an event. 
There are lots of gift shops, they all are going to the gift shops and randomly
 picking the gifts. After picking the gifts they are randomly arriving in the
 billing counter. The accountant gives the preference to that student who has 
 maximum number of gifts. Create a C program to define order of billed 
 students?
"""

import random
from random import shuffle

# Sorting using Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

gift = []
# Populating list with random numbers (gifts)
gift = (random.sample(range(1, 50), 10))

# sorting items in descending order
bubbleSort(gift)

# Creating students
students = []
s = "s"
students = [s+str(i) for i in range(1, 11)]

# Shuffling items in student (randomly reaching to the billing-counter)
shuffle(students)

# Zipping students with their gifts
mapping = list(zip(students, gift))

print("Order at which accountant gives preference to student who has maximum number of gifts")
print("Sr.\tStudent\t\tNo. of Gifts")
for i in range(10):
    print(i+1,"\t",mapping[i][0],"\t\t",mapping[i][1])
