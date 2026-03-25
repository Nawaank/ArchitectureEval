from collections.abc import Iterable, Iterator


def add_matter_4(cls):
    original_init = cls.__init__
    original_average = cls.average
    original_str = cls.__str__

    def new_init(self, name, math, physics, english, matter_4):
        original_init(self, name, math, physics, english)
        self.matter_4 = matter_4

    def new_average(self):
        return (self.math + self.physics + self.english + self.matter_4) / 4

    def new_str(self):
        return (
            f"{self.name} - Math: {self.math}, Physics: {self.physics}, "
            f"English: {self.english}, Matter 4: {self.matter_4}"
        )

    cls.__init__ = new_init
    cls.average = new_average
    cls.__str__ = new_str
    return cls


@add_matter_4
class Student:
    def __init__(self, name, math, physics, english):
        self.name = name
        self.math = math
        self.physics = physics
        self.english = english

    def average(self):
        return (self.math + self.physics + self.english) / 3

    def __str__(self):
        return f"{self.name}"


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


class StudentIteratorMatter4(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter_4, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


def add_iterator_matter_4(cls):
    def iter_matter_4(self):
        return StudentIteratorMatter4(self.students)

    cls.iter_matter_4 = iter_matter_4
    return cls


@add_iterator_matter_4
class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return StudentIteratorMatter1(self.students)

    def iter_matter_2(self):
        return StudentIteratorMatter2(self.students)

    def iter_matter_3(self):
        return StudentIteratorMatter3(self.students)


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13, 15))
    school_class.add_student(Student('A', 8, 2, 17, 9))
    school_class.add_student(Student('V', 9, 14, 14, 18))

    print("=== Matière 4 ===")
    for student in school_class.iter_matter_4():
        print(student)