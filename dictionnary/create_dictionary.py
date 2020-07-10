"""
This example to show how to create a dictionary
Author : Tapas
Date   : 10-07-2020

"""

dict1 = []
#print(type(dict1))
dict1 ={7: "Kholi",
        2: "Dhoni",
        3: "Rohit"} # creating dict1

dict1[1]="Rohan" # adding  key:value pair to the end of the dictionary
del dict1[3]     # remove specific key:value pair
dict2 = dict1.copy()   # copy first dictionary to the second
print(dict2)

print(dict2.keys())     #extract all the keys and print
print(dict2.values())
print(dict2.items())


