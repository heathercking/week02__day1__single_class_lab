class Student:
    def __init__(self, student_name, cohort_number):
        self.name = student_name
        self.cohort = cohort_number

    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, language):
        return f"I love {language}"