class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'Я издаю звуки'

class Dog(Animal):
    def speak(self):
        return f'Гав'

class Cat(Animal):
    def speak(self):
        return f'Мяу'

cat1 = Cat('Тигр')
dog1 = Dog('Тузик')
print(cat1.speak())
print(dog1.speak())