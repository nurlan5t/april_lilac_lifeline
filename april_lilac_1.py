class Person:
    def __init__(self, fullname: str, age: int, is_married: bool):
        self.fullname = fullname
        if len(fullname.split()) < 2:
            raise Exception("Name and Surname!")
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"fullname: {self.fullname}\nage: {self.age}\nmarried: {self.is_married}")


class Student(Person):
    def __init__(self, fullname: str, age: int, is_married: bool, **kwargs):
        super().__init__(fullname, age, is_married)
        self.marks = kwargs

    def average_rates(self):
        return sum(self.marks.values()) / len(self.marks.values())


class Teacher(Person):
    def __init__(self, fullname: str, age: int, is_married: bool, experience: int):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    salary = 10000

    def salary_with_experience(self):
        if self.experience > 3:
            ranged_years = self.experience - 3
            percents_add = 0.05
            for year in range(ranged_years):
                self.salary += self.salary * percents_add
            return self.salary


def create_students():
    alan = Student("a m", 21, True, math=2, english=4)
    sam = Student("s r", 20, False, math=4, english=5)
    katy = Student("k b", 19, True, math=5, english=5)
    return [alan, sam, katy]


for student in create_students():
    student.introduce_myself()
    print(f"average rate: {student.average_rates()}\n")
