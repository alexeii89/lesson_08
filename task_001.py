class Date:
    def __init__(self, date):
        Date.list = date.split('-')

    @classmethod
    def convert_date(cls):
        cls.year = int(cls.list[2])
        cls.control_dict = cls.f_year(cls.year)
        cls.month = cls.f_month(int(cls.list[1]))
        cls.day = cls.f_day(int(cls.list[0]), cls.control_dict[cls.month])
        if cls.month == None or cls.day == None:
            cls.year = "Error!"
            cls.month = "Error!"
            cls.day = "Error!"
    @staticmethod
    def f_year(year):
        control_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if year % 4 == 0:
            control_dict[2] = 29
        return control_dict

    @staticmethod
    def f_month(month):
        if 1 <= month <= 12:
            return month
        else:
            print("Месяц не может быть меньше 1 или больше 12")

    @staticmethod
    def f_day(day, control_day):
        if 0 < day <= control_day:
            return day
        else:
            print(f"ошибка в в этом месяце всего {control_day} дней")


d_1 = Date('29-02-2021')
d_1.convert_date()
print(f'{d_1.day}.{d_1.month}.{d_1.year}')
d_2 = Date('29-02-2020')
d_2.convert_date()
print(f'{d_2.day}.{d_2.month}.{d_2.year}')
