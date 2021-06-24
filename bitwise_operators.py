# По вот этой статье https://realpython.com/python-bitwise-operators
# разбираем побитовые операции
# Что мне удалось понять?
# что иногда удобно обратиться к двоичному представлению числа (заметим, что в компе они хранятся так)
# так можно манипулировать с каждым битом...
# например, брать значение бита под определенным индексом
def get_normalized_bit(value, bit_index):
    return (value >> bit_index) & 1
# Это не стандартная функция... это способ получить значение определенного бита

#Имеются также способы установить бит в единичку
def set_bit(value, bit_index):
    return value | (1 << bit_index)

#и установить бит в нолик
def clear_bit(value, bit_index):
    return value & ~(1 << bit_index)

#я узнала, что Python по умолчанию показывает числа в десятичном виде.
#при помощи функции bin() мы можем посмотреть двоичное представление
# а при помощи bit_length() узнать сколько бит нам нужно, чтобы хранить число в памяти

for n in range(0, 17):
    print(f"n = {n}")
    print(f"bin(n) = {bin(n)}")
    print(f"n.bit_length() = {n.bit_length()}")
    print("   ")

#задача! Дано число в десятичном виде. Посмотреть сколько в двоичном представлении
#требуется нулей и единиц и составить из них другое максимально возможное число

a = 11

#для начала я просто посчитаю сколько имеется нулей и единиц

len_a = a.bit_length()
one_counter = 0
zero_counter = 0

for i in range(0, len_a):
    if get_normalized_bit(a, i) == 1:
        one_counter += 1
    else:
        zero_counter += 1

print(f"a = {a}")
print(f"bin(a) = {bin(a)}")
print(f"one_counter = {one_counter}")
print(f"zero_counter = {zero_counter}")

#теперь воспользуюсь знанием о том, что число тем больше, чем больше
#единичек в начале этого числа

#просто заполню число единицами с самого начала
#по всей длине
ans = 0
for i in range(0, len_a):
    ans = set_bit(ans, i)

#теперь поставлю нужное количество нулей
#индексация в побитовом виде идет с конца
#как-то так
#  n-1     0
#  |       |
#  100101010

for i in range(0, zero_counter):
    ans = clear_bit(ans, i)

print(f"bin(a) = {bin(a)}")
print(f"bin(ans) = {bin(ans)}")
print(f"ans = {ans}")

#поэтому вот видно как все сработало

#еще задачка!
#Определить, сколько раз встречается 11 в двоичном
#представлении целого положительного числа
#например, в 11110111 оно встречается 5 раз

#и еще задачка
#
#реализовать циклический сдвиг битов вправо
#например c_shift(4, 1)
#4 = 100
#циклический сдвиг на 1 бит делает
#010 (правые биты не исчезают, как при >>, а переставляются в начало)

n = 17

def c_schift(num, schift):
    #идея... взять последний бит
    #применить сдвиг
    #поставить в начало то, что сохранили на первом шаге
    #сделать так schift раз

    len_num = n.bit_length()
    for i in range (0, schift):
        last_bit = get_normalized_bit(num, 0)
        num = num >> 1
        num = set_bit(num, len_num-1)
        if last_bit == 0:
            num = clear_bit(num, len_num-1)

    return num
print(f"bin(n) = {bin(n)}")
n = c_schift(n, 1)
#print(f"n after ideas = {n}")
print(f"bin(n) = {bin(n)}")

'''
a = int(input())
b = int(input())
print(f"You have entered a = {a}")
print(f"You have entered b = {b}")
print("   ")
print(f"bin repr of a - {bin(a)}")
print(f"bin repr of b - {bin(b)}")
len_a = a.bit_length()
len_b = b.bit_length()
print(f"a.bit_length() = {len_a}")
print(f"b.bit_length() = {len_b}")

n = 5
nums = [7, 1, 1, 4, 5, 7]
res = 0
for i in nums:
    res = res ^ i
print(f"res = {res}")
#подумать про два непарных элемента
'''
