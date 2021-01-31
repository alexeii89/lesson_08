class Warehouse:
    value_w = 10000           #Общий объем склада
    occupied_volume = 0     #Занятый обьем



class OfficeEquipment(Warehouse):
    my_list = [{"название": None, "цена": 0, "количество": 0, "объем": 0, "тип":None}]
    value_w = 10000           #Общий объем склада
    occupied_volume = 0     #Занятый обьем
    def __init__(self, name):
        self.name = name                        #Наименование

    def find_on_Warehouse(self):
        self.type_t = self.__class__.__name__
        add_true = True
        for i in self.my_list:
            if i['название'] == self.name and i['тип'] == self.type_t:
                j = self.my_list.index(i)
                print(f"на складе уже есть {i['название']} в количестве {i['количество']} шт id")
                amount = int(input("Сколько добавить?: "))
                self.readd_on_Warehouse(j, amount)
                #i.['количество'] += self.amount
                add_true = False
                break
        if add_true == True:
            self.add_on_Warehouse()
    def add_on_Warehouse(self): #Добавление на склад
        self.price = int(input("Введите цену"))
        self.value = float(input("Введите обьем 1 шт в кубических метрах"))
        self.amount = int(input("Введите количество штук"))
        a = self.value * self.amount
        self.test(a)
        d = dict(название=self.name, цена=self.price, количество=self.amount, объем=self.value, тип=self.type_t)
        self.my_list.append(d)

    def readd_on_Warehouse(self, j, amount):
        self.amount = self.my_list[j]['объем'] * amount
        self.test(self.amount)
        self.my_list[j]['количество'] += amount

    def test(self, a):
        self.occupied_volume = self.occupied_volume + a
        if self.occupied_volume > self.value_w:
            print("Склад переполнен")

class Printer(OfficeEquipment):
    def __init__(self, name):
        super(Printer, self).__init__(OfficeEquipment)
        self.name = name


class Scaner(OfficeEquipment):
    def __init__(self, name):
        super(Scaner, self).__init__(OfficeEquipment)
        self.name = name

class Copyer(OfficeEquipment):
    def __init__(self, name):
        super(Copyer, self).__init__(OfficeEquipment)
        self.name = name


while True:
    my_command = input("Для добавление введите add [нужное оборудование] (Printer, Scaner, Copyer), для выхода введите 'q': ")
    if my_command == "add Printer":
        name = input("Введите название товара: ")
        Printer(name).find_on_Warehouse()
    elif my_command == "add Scaner":
        name = input("Введите название товара: ")
        Scaner(name).find_on_Warehouse()
    elif my_command == "add Copyer":
        name = input("Введите название товара: ")
        Copyer(name).find_on_Warehouse()
    elif my_command == "q":
        break

print(OfficeEquipment.my_list[1:])