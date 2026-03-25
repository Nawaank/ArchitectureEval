from collections.abc import Iterable, Iterator

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


class StudentIteratorMatter1(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.math, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class StudentIteratorMatter2(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.physics, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class StudentIteratorMatter3(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.english, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def rank_matter_1(self):
        return sorted(self.students, key=lambda s: s.math, reverse=True)

    def rank_matter_2(self):
        return sorted(self.students, key=lambda s: s.physics, reverse=True)

    def rank_matter_3(self):
        return sorted(self.students, key=lambda s: s.english, reverse=True)

    def __iter__(self):
        return StudentIteratorMatter1(self.students)

    def iter_matter_2(self):
        return StudentIteratorMatter2(self.students)

    def iter_matter_3(self):
        return StudentIteratorMatter3(self.students)


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("=== Matière 1 ===")
    for student in school_class:
        print(student)

    print("\n=== Matière 2 ===")
    for student in school_class.iter_matter_2():
        print(student)

    print("\n=== Matière 3 ===")
    for student in school_class.iter_matter_3():
        print(student)