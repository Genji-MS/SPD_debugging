# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


user_name = input('Please enter your username: ')
save_into_db(user_name)
user_age = int(input('Please enter your birth year: '))
age = 2020 - user_age
print("You are",age, "years old.")