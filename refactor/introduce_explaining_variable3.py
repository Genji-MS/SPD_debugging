# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05
current_state = ""

def is_cookeding_criteria_satisfied(desired_state):
    if desired_state == 'well-done' and self.current_state >= WELL_DONE: 
        return True
    elif desired_state == 'medium' and self.current_state >= MEDIUM:
        return True
    else:
        return False

def calc_state(time, temperature, pressure)
    self.current_state = time * temperature * pressure * COOKED_CONSTANT