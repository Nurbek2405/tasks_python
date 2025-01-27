class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

bird1 = Bird('Орел','2.3м')
print(f'Имя: {bird1.name}')
print(f'Размах крыльев {bird1.wingspan}')
