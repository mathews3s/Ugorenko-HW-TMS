#task 1
print("\nЗадание 1.")

number = int(input("Введите число: "))
if number % 10 == 3:
    print(True)
else:
    print(False)

#task 2
print("\nЗадание 2.")

number_1, number_2, number_3 = map(int, input("Введите три числа: ").split())
if number_1 < 0 or number_2 < 0 or number_3 < 0:
    print(True)
else:
    print(False)

#task 3
print("\nЗадание 3.")

number_1, number_2 = map(int, input("Введите два числа: ").split())
if (number_1 % 2 == number_2 % 2):
    print(True)
else:
    print(False)

#task 4
print("\nЗадание 4.")

side_a, side_b, side_c  = map(int, input("Введите длинны трех сторон треугольника: ").split())
if side_a == side_b == side_c:
    print("equilateral")
elif side_a == side_b or side_b == side_c or side_a == side_c:
    print("isosceles")
else:
    print("scalene")

#task 5
print("\nЗадание 5.")

even_counter = 0
number_1, number_2, number_3 = map(int, input("Введите три числа: ").split())
if number_1 % 2 == 0:
    even_counter += 1
if number_2 % 2 == 0:
    even_counter += 1
if number_3 % 2 == 0:
    even_counter += 1
print(even_counter)

#task 6
print("\nЗадание 6.")

number = int(input("Введите двузначное число: "))
digits_sum = (number // 10) + (number % 10)
if 10 <= digits_sum < 100:
    print(True)
else:
    print(False)

#task 7
print("\nЗадание 7.")

number_str = str(input("Введите четырехзначное число: "))
if number_str[0] == number_str[1] == number_str[2] == number_str[3]:
    print(True)
else:
    print(False)

#task 8
print("\nЗадание 8.")

year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Високосный")
else:
    print("Не високосный")

#task 9
print("\nЗадание 9.")

for _ in range(20):
    print(10)

#task 10
print("\nЗадание 10.")

start = int(input("Введите стартовое число: "))
stop = int(input("Введите конечное число: "))
for num in range(start, stop + 1):
    print(num)

#task 11
print("\nЗадание 11.")

for num in range(100, -101, -1):
    print(num, end=' ')
print("\n")

#task 12
print("\nЗадание 12.")
sum = 0
for num in range(100, 501):
    sum += num

print(sum)

#task 13
print("\nЗадание 13.")

product = 1
for num in range(5, 21):
    product *= num
print(product)

#task 14
print("\nЗадание 14.")

n = int(input("Введите натуральное число: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
