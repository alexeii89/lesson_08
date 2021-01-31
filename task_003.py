class OnlyNumbers:
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def is_digit(n):
        try:
            int(n)
            return True
        except ValueError:
            return False

my_list = []
while True:
    nubmer = input("введите число, для выхода введите stop: ")
    if nubmer == 'stop':
        break
    elif OnlyNumbers.is_digit(nubmer) == False: #Обычный isdigit при вводе отрицательного числа возвращает False
        print(OnlyNumbers("Вы ввели не число").txt)
    else:
        my_list.append(int(nubmer))

print(f'Сформированыый список: {my_list}')



