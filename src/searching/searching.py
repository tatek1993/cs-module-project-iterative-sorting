def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        cur = arr[i]
        if cur == target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left, right = 0, len(arr) - 1

    while len(arr) >= 1:

        middle = int(left + right / 2)

        # if the current node == target, return current node
        if arr[middle] == target:
            return middle

        # if current node is less than target, set current node.right to current node
        elif arr[middle] < target:
            left, right = middle + 1, right

        # else if current node is greater than target, set current node.left to current node
        elif arr[middle] > target:
            left, right = left, middle

    return -1  # not found
