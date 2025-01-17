#task 1

print("Задание 1. Результаты:")
print(17/2*3 + 2)                #27.5
print(2 + 17/2*3)                #27.5
print(19 % 4 + 15/2*3)           #25.5
print(15 + 6 - 10*4)             #-19
print(17/2 % 2 * 3**3)           #13.5


#task 2

print("\nЗадание 2. Результаты:")
print((17 / 2) * (3 + 2))        # 42.5
print(2 + (17 / 2) * 3)          # 28.5
print((19 % 4) + (15 / 2) * 3)   # 0.0
print(15 + (6 - 10) * 4)         # 44
print((17 / 2) % (2 * 3**3))     # 8.5


#task 3
print("\nЗадание 3.")
bread_count = 3
bread_price = 1.5
anna_cash = 11

remaining_cash = anna_cash - (bread_price * bread_count)
print(f"У анны осталось {remaining_cash} рублей после покупки хлеба")


#task 4
print("\nЗадание 4.")
anna_apples = 2
paul_apples = 5

print(f"У Анны {anna_apples} яблока, у Пола {paul_apples} яблок.")


#task 5
print("\nЗадание 5.")

days = 5
print(f"{days} суток = {days * 24} часов = {days * 24 * 60} "
      f"минут = {days * 24 * 60 ** 2} секунд")


#task 6
print("\nЗадание 6.")

days_count = 182
weeks_count = days_count // 7
print(f"За период в {days_count} дней(дня) прошло {weeks_count} целых недель")


#task 7
print("\nЗадание 7.")

side_1 = 150
side_2 = 65
square_side = 30

squares_count = (side_1 // square_side) * (side_2 // square_side)
print(f"Можно отрезать {squares_count} квадратов.")


#task 8
print("\nЗадание 8.")

seconds = 4000
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"{hours} часов")
print(f"{minutes} минут")
print(f"{remaining_seconds} секунд")


#task 9*
print("\nЗадание 9*.")

cash = 361

hundreds = cash // 100
cash %= 100
fifties = cash // 50
cash %= 50
tens = cash // 10
cash %= 10
ones = cash

print(f"{hundreds} купюры по 100 рублей")
print(f"{fifties} купюры по 50 рублей")
print(f"{tens} купюры по 10 рублей")
print(f"{ones} купюры по 1 рублю")


#task 10*
print("\nЗадание 10*.")

height = 10
up = 3
down = 1
pseudo_ceil = up - down
day = (height - up + pseudo_ceil)//(up - down) + 1
print(f"Улитка заползет на столб на {day} день")


#task 11*
print("\nЗадание 11*.")

track_length = 56
speed = 20
hours = 2
minutes = 30

hours += minutes / 60
distance_covered = speed * hours
mkad_mark = distance_covered % track_length

print(f"Байкер остановится на отметке {mkad_mark} километра МКАД-а.")