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
    
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)