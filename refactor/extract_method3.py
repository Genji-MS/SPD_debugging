# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math
xc1 = 4
yc1 = 4.25

xc2 = 53
yc2 = -5.35
# Calculate the distance between the two circle
distance = calc_distance(xc1, xc2, yc1, yc2)
print('distance', distance)
# *** somewhere else in your program ***
xa = -36
ya = 97

xb = .34
yb = .91
# calcualte the length of vector AB vector which is a vector between A and B points.
length = calc_length(xa, xb, ya, yb)
print('length', length)

def calc_distance(xa, xb, ya, yb):
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

def calc_length(xa, xb, ya, yb):
    return math.sqrt((xa - xb) * (xa - xb) + (ya - yb) * (ya - yb))