# task 1

print("\nЗадание 1")

border_value = int(input("Введите число: "))
number, power = 1, 1

while power < border_value:  # O(√n - 1)
    print(power, end=" ")
    number += 1
    power = number ** 2




# task 2

print("\nЗадание 2")

number = int(input("Введите число: "))
remind = number

while remind >= 10:  # O(n - 1)
    remind //= 10

print(f"Первая цифра числа - {remind}\n")




# task 3
# Задание решено с учетом того, что 0 - не натуральное число (где-то считают, что он натурален)

print("Задание 3")

number = int(input("Введите число: "))
min_digit = 9
remind = number

while remind > 0:                 # O(n - 1)
    current_digit = remind % 10
    if min_digit > current_digit:
        min_digit = current_digit
    remind //= 10

print(f"Минимальная цифра в числе - {min_digit}\n")




# task 4
print("Задание 4")

some_str = input("Введите строку: ")

print(f"Третий символ строки: {some_str[2]}")
print(f"Предпоследний символ строки: {some_str[-2]}")
print(f"Первые пять символов строки: {some_str[:5]}")
print(f"Все, кроме последних двух символов: {some_str[:-2]} ")      # 0(n - 2) ?
print(f"Символы с четными индексами: {some_str[::2]}")              # 0(n)
print(f"Символы с нечетными индексами: {some_str[1::2]}")           # O(n / 2)
print(f"Символы через один в обратном порядке: {some_str[-1::-2]}") # O(n / 2)
print(f"Длинна строки: {len(some_str)}\n")




# task 5
print("Задание 5")
# Сложность алгоритма - O(n)

some_str = input("Введите строку из 2-х слов: ")
words = some_str.split()  # O(n)?
words[0], words[1] = words[1], words[0]
new_str = " ".join(words)  # O(n)?

print(new_str)




# task 6
print("\nЗадание 6")

some_str = input("Введите строку: ")

if some_str == some_str[::-1]:
    print("Строка является палиндромом!")
else:
    print("Строка не палиндром!")




# task 7
print("\nЗадание 7")

some_str = input("Введите строку содержащую 'f': ")
f_count = some_str.count('f')
if f_count < 2:
    print(f"Индекс первой 'f': [{some_str.index('f')}]")
elif f_count >= 2:
    print(f"Индекс первой 'f': [{some_str.index('f')}]; Кол-во: {f_count}")




# task 8
print("\nЗадание 8")

first_list = list(map(int, input("Введите элементы 1-го списка через пробел: ").split()))
second_list = list(map(int, input("Введите элементы 2-го списка через пробел: ").split()))
common_elements = []

for num in first_list:
    if num in second_list:
        common_elements.append(num)

if len(common_elements):
    print(f"Минимальный элемент 1-го списка, имеющийся во 2-ом - {min(common_elements)}\n")
else:
    print("Нет общих элементов\n")




# task 9
print("Задание 9")

elements_count = int(input("Введите кол-во элементов списка (k):"))
elements = []
inverse_count = 0

for index in range(0, elements_count):
    elements.append(int(input(f"Введите элемент списка по индексу [{index}]: ")))

for left_index in range(0, len(elements) - 1):
    for right_index in range(left_index + 1, len(elements)):
        if elements[left_index] > elements[right_index]:
            inverse_count += 1

print(f"Количество инверсий: {inverse_count}\n")




# task 10
print("Задание 10")

some_str = input("Введите строку: ")
unic_chars = []

for char in some_str:
    if char not in unic_chars:
        unic_chars.append(char)

result = "".join(unic_chars)
print(f"Строка без повторяющихся символов: {result}\n")




# task 11
print("Задание 11")

some_text = input("Введите текст с числами: ")
min_number = 0
start_index = 0
end_index = 0
found_number = False
found_any_number = False

for index in range(0, len(some_text)):
    if some_text[index].isdigit() and not found_number:
        found_number = True
        start_index = index
    elif (not some_text[index].isdigit()) and found_number:
        found_number = False
        end_index = index
        number = int(some_text[start_index:end_index])
        if not found_any_number:
            found_any_number = True
            min_number = number
        elif number < min_number:
            min_number = number
    else:
        continue
if not found_any_number:
    print("В тексте отсутствуют числа!\n")
else:
    print(f"Минимальное число в тексте - {min_number}\n")




# task 12
print("Задание 12")

some_string = input("Введите строку: ")
unique_chars = ""

for char in some_string:
    if char not in unique_chars:
        unique_chars += char

some_string = unique_chars
print(f"Строка без повторяющихся символов: '{some_string}'\n")

# task 13
print("Задание 13")

numbers = list(map(int, input("Введите элементы списка через пробел: ").split()))
numbers_with_mirror = []

for number in numbers:
    numbers_with_mirror.append(number)
    if number % 2 != 0:
        continue
    mirror_number = 0
    while number != 0:
        mirror_number *= 10
        mirror_number += number % 10
        number //= 10
    numbers_with_mirror.append(mirror_number)
numbers = numbers_with_mirror

print(f"Модернизированный список: {numbers}")
