# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

ingredients = ['sodium benzoate']
s_nitrate = 'sodium nitrate' in ingredients
s_benzoate = 'sodum benzoate' in ingredients
s_oxide = 'sodium oxide' in ingredients
if s_nitrate or s_benzoate or s_oxide:
    print('!!!\nthere is a toxin in the food!\n!!!')
    make_alert_sound()
else:
    print('***\nToxin Free\n***')
    make_accept_sound()