####
# Quicksort Iterative algorithm taken from: https://www.geeksforgeeks.org/iterative-quick-sort/
# Quicksort Recursive algorithm taken from: https://www.geeksforegeeks.org/quick-sort/


# accessed on 01/27/22
# License: none given
# Authors: Palak Jain, Adnan Aliakbar

###
# CHANGELOG:
# -added if __name__== "__main__" to driver code
# modify the driver code to use a list of tuple, and print array
# Modify the def quicksort(array): function to use the mid-index as pivot "pivot = array[int(len(array)/2)]"
# ####

import math


# Python3 implementation of QuickSort

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l --> Starting index,
# h --> Ending index
def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


#  Quicksort iterative algorithm
def quicksort(array):
    # We define our 3 arrays
    less = []
    equal = []
    greater = []

    # if the length of our array is greater than 1
    # we perform a sort
    if len(array) > 1:
        # Select our pivot. This doesn't have to be
        # the first element of our array
        pivot = array[math.floor(len(array) / 2)]
        # print("pivot is " + str(pivot))
        # recursively go through every element
        # of the array passed in and sort appropriately
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        # recursively call quicksort on gradually smaller and smaller
        # arrays until we have a sorted list.
        return quicksort(less) + equal + quicksort(greater)

    else:
        return array


def main():
    # Driver code to test above
    arr = [('aye', "hey"), ('jug', 'ayo'), ('kong', 'err'), ('plate', 'man'), ('zeal', 'abs')]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    print(f'Sorted array is:  {arr}')


if __name__ == "__main__":
    main()
# This code is contributed by Mohit Kumra
