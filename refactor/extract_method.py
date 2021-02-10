# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

def print_stat():
    # Get the inputs from the user
    grade_list = user_inputted_grades(5)
    # Calculate the mean and standard deviation of the grades
    mean = calc_mean(grade_list)
    sd = calc_std_dev(grade_list, mean)
    
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

def user_inputted_grades(n_student):
    grade_list = []
    for _ in range(0,n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calc_std_dev(grade_list, mean):
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd

def calc_mean(grade_list):
    # Calculate the mean and standard deviation of the grades
    total = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        total += grade
    mean = total / len(grade_list)
    return mean

print_stat()