# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code. If required, use
#       'replace temp variable with query' technique to make it easier to extract methods.
class Employer:    
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students
        self.MIN_GPA = 2.5
    def process_graduation(self):
        # Process the students in the school who have successfully graduated.
        passed_students = self.process_graduated_students()    
        # Find the top 10% of them and send their contact to the top employers
        self.top_10_percent(passed_students)

    def process_graduated_students(self):
        passed_students = []
        print('*** Student who graduated *** ')
        for s in self.students:
            if s.get_gpa() > self.MIN_GPA:
                passed_students.append(s) #add to list
                print(s.name) # print student's name who graduated.                
                s.send_congrat_email() # Send congrat emails to them.
        print('****************************')
        return passed_students

    def top_10_percent(self, passed_students):
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)

students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'), 
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students)
school.process_graduation()