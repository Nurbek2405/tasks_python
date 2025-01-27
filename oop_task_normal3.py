'''3 Средний уровень
Задача: Класс для управления задачами
Создай класс Task с атрибутами:
•	description (описание задачи),
•	priority (приоритет: "низкий", "средний", "высокий"),
•	completed (по умолчанию False).
Добавь методы:
•	mark_completed(), который отмечает задачу выполненной.
•	task_info(), который выводит информацию о задаче.
🔹 Пример работы в консоли:
Задача: "Написать отчет", Приоритет: средний, Выполнена: Нет
Отмечаем выполненной...
Задача: "Написать отчет", Приоритет: средний, Выполнена: Да
'''
class Task:
    def __init__(self, description, priority, completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed

    def mark_completed(self):
        self.completed = True
        print('Отмечаем выполненной...')
        return self.completed

    def task_info(self):
        return f'Задача: {self.description}, Приоритет: {self.priority}, Выполнена: {self.completed}'

task1 = Task('Написать отчет','средний')

print(task1.task_info())
task1.mark_completed()
print(task1.task_info())
