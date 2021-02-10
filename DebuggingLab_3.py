"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
            if j < 0:
                break
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

'''
EXPECTATION: 1, 2, 3, 5, 6
ACTUAL: N/A
ERROR: IndexError: list index out of range
LINE: 26 - 28
ISSUE: while key < arr[j] :
DESCRIPTION: This while loop can continue into negative numbers and does not check if it is a valid index.
FIX: if j<0: break
COMMENT: The loop will quit at j == -1. Which follows with j+1 = 0. Therefore array[0] = key. Which is within bounds as desired
'''