"""
Exercise 1
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

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)


'''
EXPECTATION: 4
ACTUAL: N/A
ERROR: IndexError: list index out of range
LINE: 23
ISSUE: list_of_nums[i+1]
DESCRIPTION: The for loop interates the entire length of the list, eventually i == end of the list. Therefore i+1 is out of range
FIX: line 22    for i in range(len(list_of_nums) -1):
COMMENT: the list will stop short of the end of the list yet check i+1 == end of the list.
'''