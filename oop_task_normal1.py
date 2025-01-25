class CurrencyConverter:
    def __init__(self, rates):
        self.rates = {"USD": 460, "EUR": 500}

    def convert(self, amount, currency):
        print(f'Конвертируем {amount} {currency}...')
        sum1 = self.rates[currency] * amount
        return print(f'Итог: {sum1} KZT')

    def show_currencies(self):
        return print(f'Курсы валют: {self.rates}')

#Курсы валют: USD - 460, EUR - 500
#Конвертируем 100 USD...
currency1 = CurrencyConverter(100)
currency1.show_currencies()
currency1.convert(100, "USD")
currency2 = CurrencyConverter(50)
currency2.convert(50, "EUR")



