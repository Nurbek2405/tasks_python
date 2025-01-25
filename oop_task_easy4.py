class FoodOrder:
    def __init__(self, dish, quantity , status='в ожиданий'):
        self.dish = dish
        self.quantity = quantity
        self.status = status

    def prepare(self):
        self.status = 'готовится'
        return print(f'Готовим заказ...  ')

    def complete(self):
        self.status = 'готово'
        return print(f'Заказ готов!  ')

    def show_order(self):
        return print(f'Заказ: {self.dish}, Количество: {self.quantity}, Статус:  {self.status}')

order1 = FoodOrder('Пицца', 3)
order2 = FoodOrder('Суши', 20)

order1.show_order()
order2.show_order()
order1.prepare()
order1.show_order()
order1.complete()
order2.prepare()
order2.show_order()
order1.show_order()
order2.complete()
order2.complete()
order2.show_order()