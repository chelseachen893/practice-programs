"""
Assignment: Given a list [1,5,4,8,11,13,18], print even numbers and their index in the List
Date created: 07/06/2020
Author: Chelsea Chen
"""
values = [1,5,4,8,11,13,18]
for i in values:
    value = int(i)
    if value%2 == 0:
        print("even value: " + str(i))
        print("even value index: " + str(values.index(i)))