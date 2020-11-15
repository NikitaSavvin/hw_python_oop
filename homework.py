import datetime as dt

class Record:


    date_format = '%d.%m.%Y'
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        self.date = (dt.date.today() if date is None 
                     else dt.datetime.strptime(date, '%d.%m.%Y').date())


class Calculator:
    

    def __init__(self, limit):
        self.limit = limit    
        self.records = []

    def add_record(self, record):
        self.records.append(record)  

    today_date = dt.datetime.now().date() 
    delta_date = dt.timedelta(days=7)

    def get_today_stats(self):
        today_stats = sum(record.amount for record in self.records if 
                          record.date == self.today_date)
        return today_stats

    def get_week_stats(self):
        last_week_date = self.today_date - self.delta_date       
        week_stats = sum(record.amount for record in self.records 
                         if record.date <= self.today_date and 
                         record.date >= last_week_date)      
        return week_stats
        
    
class CaloriesCalculator(Calculator):


    def __str__(self):
         self.limit
    
    def add_record(self, record):
        super().add_record(record)

    def get_calories_remained(self):
        today_calories = super().get_today_stats()
        remains = self.limit - today_calories
        if self.limit > today_calories:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remains} кКал"
        else:
            return f"Хватит есть!"   

class CashCalculator(Calculator):


    USD_RATE =float(60)
    EURO_RATE =float(70)

    currencies = {
        'rub' : [1, 'руб'],
        'eur' : [EURO_RATE, 'Euro'],
        'usd' : [USD_RATE, 'USD']
        }

    def currency_conversion(self, money, currency):
        value_RATE = self.currencies[currency]
        conversion = round(money/value_RATE[0], 2)
        return [conversion, value_RATE[1]]

    def get_today_cash_remained(self, currency):
        today_cash = super().get_today_stats()
        remains = self.limit - today_cash
        conversion_remains = self.currency_conversion(remains, currency)
        conversion_money = conversion_remains[0]
        monetary_currency = conversion_remains[1]
        if self.limit > today_cash:
            return f"На сегодня осталось {conversion_money} {monetary_currency}"
        elif self.limit == today_cash:
            return f"Денег нет, держись"
        elif remains <0:
            conversion_debt = conversion_money * -1
            return f"Денег нет, держись: твой долг - {conversion_debt} {monetary_currency}"






        




