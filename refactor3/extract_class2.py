# by Kami Bigdely
# Extract class
class Info:
    def __init__(self,first,last,year,email,movie_list)
        first_name = first
        last_name = last
        birth_year = year
        emails = email
        movies = movie_list

def send_hiring_email(email):
    print("email sent to: ", email)

people = []

jim = Info("Jim", "Carrey", 1962, "jim@makeschool.com", ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'])
people.append(jim)
deb = Info("elizabeth", "debicki", 1990, "deb@makeschool.com", ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'])
people.append(deb)

for person in people:
if person.birth_year > 1985:
    print(person.first_names, person.last_names)
    print('Movies Played: ', end='')
    for m in person.movies:
        print(m, end=', ')
    print()
    send_hiring_email(person.emails)