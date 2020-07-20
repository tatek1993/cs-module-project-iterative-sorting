# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # for each item in the entire length of the array, starting at i +1
        for x in range(cur_index + 1, len(arr)):
            # if the current index is less than the smallest index
            if arr[x] < arr[smallest_index]:
                #set the smallest index to that current array
                smallest_index = x

        # TO-DO: swap
        # Your code here
        # swap the values of that current array and the smallest index
        # temporarily hold the value of the current index
        temp_hold = arr[i]

        # assign the value of the smallest_index to the current index
        arr[i] = arr[smallest_index]

        # assign the value of the temp_hold to the smallest_index
        arr[smallest_index] = temp_hold
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    # items swapped
    swapped = 0

    while swapped != len(arr):
        # in the range of the length of our array. We want to go through the list as many times as there are elements in the list. We deincrement that length for each item that is swapped
        for i in range(0, len(arr) - swapped - 1):
            # if the current index in the array is greater than the next
            if arr[i] > arr[i + 1]:
                # swap them
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        # increment swapped
        swapped += 1

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
