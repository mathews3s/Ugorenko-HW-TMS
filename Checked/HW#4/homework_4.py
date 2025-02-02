from math import sqrt


# task 1

def minimum(val_1: int, val_2: int) -> int:
    if val_1 < val_2:
        return val_1
    elif val_2 < val_2:
        return val_2
    else:
        return val_1


# task 2
print("Задание 2")

number_1: int
number_2: int
number_3: int
number_4: int

number_1, number_2, number_3, number_4 = map(int, input("Введите 4-е числа: ").split())

minimal_number_1: int = minimum(val_1=number_1, val_2=number_2)
minimal_number_2: int = minimum(val_1=number_3, val_2=number_4)
minimal_number: int = minimum(val_1=minimal_number_1, val_2=minimal_number_2)

print(f"Минимальное из 4-ех чисел: {minimal_number}\n")

# task 3
print("Задание 3")


def distance(x1: float,
             y1: float,
             x2: float,
             y2: float) -> float:
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


distance_between_dots: float
first_dot_coordinate = list(map(float, input("Введите координаты 1-ой точки через пробел (x y): ").split()))
second_dot_coordinate = list(map(float, input("Введите координаты 2-ой точки через пробел (x y): ").split()))

distance_between_dots = distance(x1=first_dot_coordinate[0],
                                 y1=first_dot_coordinate[1],
                                 x2=second_dot_coordinate[0],
                                 y2=second_dot_coordinate[1])

print(f"Расстояние между точками: {distance_between_dots}\n")

# task 4
print("Задание 4")


def is_prime(value: int) -> bool:
    counter_dividers: int = 0
    for num in range(2, value):
        if value % num == 0:
            counter_dividers += 1
            break
    if counter_dividers > 0:
        return False
    else:
        return True


number = int(input("Введите число: "))

if is_prime(number):
    print("YES\n")
else:
    print("NO\n")


# task 5
print("Задание 5")

def fibbonachi(serial_num: int) -> int:
    previous_number: int = 0
    current_number: int = 1
    next_number: int = 0

    while serial_num != 0:
        next_number = current_number + previous_number
        previous_number = current_number
        current_number = next_number
        serial_num -= 1

    return previous_number


number = int(input("Введите число: "))
fibbonachi_number = fibbonachi(number)

print(f"{number}-е число Фибоначи это - {fibbonachi_number}\n")


# task 6
print("Задание 6")

def closet_mod_5(value: int) -> int:
    if value % 5 == 0:
        return value
    else:
        return value + 5 - value % 5


number = int(input("Введите число : "))
result = closet_mod_5(value=number)

print(f"Число n выполняющее условия: {result} (n % 5 = 0, n >= {number})\n")



# task 7
print("Задание 7")

def modify_list(array: list[int], temp: list[int] = []):
    for num in array:
        if num % 2 != 0:
            continue
        else:
            temp.append(num // 2)
    array.clear()
    array.extend(temp)


some_list = list(map(int, input("Введите элементы списка через пробел: ").split()))

modify_list(some_list)
print(f"Модифицированный список: {some_list}\n")




# task 8
print("Задание 8")

invalid_symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')')


def check_variable(v: str) -> bool:
    if v[0].isdigit():
        return False
    else:
        for symbol in v:
            if symbol in invalid_symbols or not (symbol.isdigit() or symbol.isalpha() or symbol == "_"):
                return False
        return True


variable_name: str

while True:
    variable_name = input("Введите имя переменной: ")
    if variable_name == "Поработали, и хватит":
        print("Действительно хватит!")
        break
    else:
        if check_variable(v=variable_name):
            print(f"Можно использовать имя '{variable_name}'!\n")
        else:
            print(f"Нельзя использовать имя '{variable_name}'!\n")
