'''
Author: Nicholas Gardner
Assignment 1: Binary Search
Description: A program to use a binary search algorithm to check for a value
   in an ordered array
Date: April 20, 2018
'''


#-- Binary Search Function --#
def binary_search(list, value):
    list = sorted(list)  #sort list if necessary
    while(True):

        if (len(list) == 0): return False  # check for empty list

        #check for list of one item, either by definition or through loop process
        if (len(list) == 1):
            if (list[0] == value): return True
            else: return False

        i = int(len(list)/2)  # index for middle entry,

        if (list[i] == value): return True #return True if value is found

        #if list entry is larger than value, remove the second half of the list
        elif (list[i] > value):
            for j in range(i, len(list)):
                list.pop(i)

        #if list entry is smaller than the value, remove the first half of the list
        else:
            for j in range(0,i+1):
                list.pop(0)

#-- End Function --#

lstUser = [0,1,2,3,4,5]  #lst to hold user data
fltSearch = 2   #variable for search value


#call the search function and print the output
print(binary_search(lstUser, fltSearch))