# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class CookingDish:
    def __init__(self,desire, time, temp, pressure)
    desired_state = desire
    temp = temp # [celcius]
    pressure = pressure # [psi]

def is_cookeding_criteria_satisfied(dish):
    if dish.desired_state == 'well-done' and 
        get_cooking_progress(dish.time, dish.temp, dish.pressure) >= WELL_DONE
        return True
    elif dish.desired_state == 'medium' and 
        get_cooking_progress(dish.time, dish.temp, dish.pressure) >= MEDIUM
        return True
    return False

def get_cooking_progress(time, temperature, pressure):
    return time * temperature * pressure * COOKED_CONSTANT


time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

dish = CookingDish(desired_state, time, temp, pressure)

if is_cookeding_criteria_satisfied(dish):
    print('cooking is done.')
else:
    print('ongoing cooking.')