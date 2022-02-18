from student import Student


class HighSchoolStudent(Student):
    high_school = "Springfield High School"

    def get_school_name(self):
        return "High School name"

    def get_name_capitalize(self):
        origanal_value = super().get_name_capitalize()
        return origanal_value + "-HS"
