students = []


class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, last_name, student_id=323):
        self.name = name
        self.student_id = student_id
        self.last_name = last_name
        students.append(self)

    def __str__(self):
        return "Students: " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
