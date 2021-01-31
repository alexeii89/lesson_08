class ZeroDevErr(Exception):
    def __init__(self, txt):
        self.txt = txt
a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

try:
    if b == 0:
        raise ZeroDevErr("На ноль делить нельзя")
except ZeroDevErr as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {a / b}")