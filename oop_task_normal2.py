'''2 Средний уровень
Задача: Класс для управления расписанием событий
Создай класс Event с атрибутами:
•	name (название события),
•	date (дата события в формате YYYY-MM-DD),
•	participants (список участников, по умолчанию пустой).
Добавь методы:
•	add_participant(participant), который добавляет участника в список.
•	event_info(), который выводит информацию о событии.
🔹 Пример работы в консоли:
Событие: Митап программистов, Дата: 2025-02-10, Участники: []
Добавляем участника "Нурбек"...
Событие: Митап программистов, Дата: 2025-02-10, Участники: ['Нурбек']
'''

class Event:
    def __init__(self, name, date, participants=[]):
        self.name = name
        self.date = date
        self.participants = participants

    def add_participant(self, participant):
        self.participants.append(participant)
        print(f'Добавляем участника {participant}...')
        return self.participants

    def event_info(self):
        return f'Событие: {self.name}, Дата:  {self.date}, Участники: {self.participants}'

even1 = Event('Митап программистов','2025-02-10')
print(even1.event_info())
even1.add_participant('Нурбек')
print(even1.event_info())
even1.add_participant('Бауыржан')
print(even1.event_info())