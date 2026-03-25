class Student:
    def __init__(self, name, math, physics, english):
        self.name = name
        self.math = math
        self.physics = physics
        self.english = english

    def average(self):
        return (self.math + self.physics + self.english) / 3

    def __str__(self):
        return f"{self.name} - Math: {self.math}, Physics: {self.physics}, English: {self.english}"
    
class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def rank_matter_1(self):
        return sorted(self.students, key=lambda s: s.math, reverse=True)

if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    ranked = school_class.rank_matter_1()
    for student in ranked:
        print(student)