class Flyable:
    def fly(self):
        return f'I can fly'

class Swimmable:
    def swim(self):
        return 'I can swim'

class Duck(Flyable,Swimmable):
    pass

duck1 = Duck()
print(duck1.fly())
print(duck1.swim())