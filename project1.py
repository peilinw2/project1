"""
Math 560
Project 1
Fall 2021

Partner 1: Amy Wang (pw137)
Partner 2: Lu Liu (ll394)
Date: October 29th, 2021
"""

"""
SelectionSort
The function is the implementation of the Selection sorting algorithm.
The function sorts an array in an ascending order by selecting the smallest element
from the unsorted array and moving it to the front of th array.
Inputs: listToSort ( a list of numbers)
Outpus: listTosort (a list of sorted numbers)
"""

def SelectionSort(listToSort):
    #Iterate over the index of the list
    for i in range(len(listToSort)-1):
	#Select the first unsorted number as the minimum
        min_index = i
	#Check the element to be the minimum
        for j in range(i+1, len(listToSort)):
            if listToSort[j] < listToSort[min_index]:
                min_index = j
	#Swap the minimum element with the current element
        if i != min_index:
            listToSort[i], listToSort[min_index] = listToSort[min_index], listToSort[i]
    return listToSort


"""
InsertionSort
The function is the implementation of the Insertion sorting algorithm.
The function sorts an array in an ascending order by separating the array into the sorted
and unsorted component, iteratively inserting the elements into the sorted component to make sure
that the left-side elements are smaller than the right-side elements.
Inputs: listToSort ( a list of numbers)
Outpus: listTosort (a list of sorted numbers)
"""

def InsertionSort(listToSort):
    #Traverse through the list
    for i in range(1, len(listToSort)):
        value = listToSort[i]
	#Move elements of the list and compare the element in front of it with the current element
        i = i - 1
	#Swap them if the preceding element is larger than the current element
        while i >= 0:
            if value < listToSort[i]:
                listToSort[i + 1] = listToSort[i]
                listToSort[i] = value
                i = i - 1
            else:
                break
    return listToSort


"""
BubbleSort
The function is the implementation of the Bubble sorting algorithm.
The function sorts an array in an ascending order by repeatedly comparing two adjacent elements if 
they are in wrong order and swap them.
Inputs: listToSort ( a list of numbers)
Outpus: listTosort (a list of sorted numbers)
"""

def BubbleSort(listToSort):
    #Iterate through the list and compare every two adjacent elements
    for i in range(len(listToSort)-1):
        swapped = False
	# The last i elements are in place
        for j in range(len(listToSort)-1-i):
	#If the elements are out of order, swap them
            if listToSort[j] > listToSort[j+1]:
                x = listToSort[j]
                listToSort[j] = listToSort[j+1]
                listToSort[j+1] = x
                swapped = True
	# Repeat until no more swaps are made and we can make sure that all elemets are sorted
        if not swapped:
            return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    if len(listToSort) > 1:
        mid = len(listToSort)//2
        left = listToSort[:mid]
        right = listToSort[mid:]

        MergeSort(left)
        MergeSort(right)
        i = j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                listToSort[k] = left[i]
                i += 1
                k += 1
            else:
                listToSort[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            listToSort[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            listToSort[k] = right[j]
            j += 1
            k += 1
    return listToSort



"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""


def partition(listToSort, l, r, pivot):
    while l <= r - 1:
        while listToSort[l] < pivot and l <= r - 1:
            l += 1
        while listToSort[r - 1] > pivot and l <= r - 1:
            r -= 1
        if l <= r - 1:
            listToSort[l], listToSort[r - 1] = listToSort[r - 1], listToSort[l]
            r -= 1
            l += 1
    return l, r

def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    if i >= j:
        return
    else:
        l = i
        r = j
        pivot = listToSort[(l + r) // 2]
        i, j = partition(listToSort, l, r, pivot)
    QuickSort(listToSort, i, r)
    QuickSort(listToSort, l, j)
    return listToSort




"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
