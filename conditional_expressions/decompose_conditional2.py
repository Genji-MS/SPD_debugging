# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

rating_triglyceride = "good"
if 150 >= triglyceride < 200:
    rating_triglyceride = "TLC"
else:
    rating_triglyceride = "high"

rating_ldl = "good"
if 100 >= ldl < 160:
    rating_ldl = "TLC"
else:
    rating_ldl = "high"

rating_cholostrol = "good"
if 200 >= total_cholostrol < 240:
    rating_cholostrol = "TLC"
else:
    rating_cholostrol = "high"

if rating_triglyceride == "high" or rating_ldl == "high" or rating_cholostrol == "high":
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
elif rating_triglyceride == "TLC" or rating_ldl == "TLC" or rating_cholostrol == "TLC":
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
elif rating_triglyceride == "good" and rating_ldl == "good" and rating_cholostrol == "good": 
    print('*** Good level of cholestrol ***')
else:
    print('Error: unhandled case.')