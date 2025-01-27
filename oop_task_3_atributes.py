class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'Привет, меня зовут {self.name}, мне {self.age} лет.'

class Student(Person):
    def __init__(self, name, age, university ):
        super().__init__(name, age)
        self.university  = university

    def introduce(self):
        return f'Привет, меня зовут {self.name}, мне {self.age} лет, я учусь в {self.university}.'

person1 = Person('Бауыржан','32')
student = Student('Нурбек', '29','Шокановском')

print(person1.introduce())
print(student.introduce())