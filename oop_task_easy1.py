class Ticket:
    def __init__(self, movie, seat, price):
        self.movie = movie
        self.seat = seat
        self.price = price

    def show_ticket(self):
        return f'Билет на фильм: {self.movie}, Место: {self.seat}, Цена: {self.price}'

ticket1 = Ticket('Титаник','A12', 1500)
ticket2 = Ticket('Аватар','B12',1800)

print(ticket1.show_ticket())
print(ticket2.show_ticket())