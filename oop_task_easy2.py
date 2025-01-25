class User:
    def __init__(self, username, email, is_active=True):
        self.username = username
        self.email = email
        self.is_active = is_active

    def deactivate(self):
        self.is_active = False
        return f'Деактивируем...'

    def show_user(self):
        return f'Пользователь: {self.username}, Email: {self.email}, Активен: {self.is_active}'

user1 = User('user1', '<EMAIL>')
user2 = User('user2', '<EMAIL>')
print(user1.show_user())
print(user1.deactivate())
print(user1.show_user())
print(user2.show_user())