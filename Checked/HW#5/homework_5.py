# task 1

odd_numbers: [int] = [number for number in range(11, 100, 2)]
print(f"Нечетные двузначные числа: {odd_numbers}\n")




# task 2

powers_of_two: [int] = [2 ** power for power in range(1, 11)]
print(f"Степени 2-ки: {powers_of_two}\n")




# task 3

three_digits_numbers: [int] = [number for number in range(100, 1000) if number % 15 == 0]

print(f"Трехзначные числа кратные 3-ке и 5-ке: {three_digits_numbers}\n")




# task 4

start_position: int
end_position: int
power: int

start_position, end_position, power = map(int, input(
    "Введите начало, конец диапазона и степень для возведения чисел (через пробел): ").split())
result_numbers = [number ** power for number in range(start_position, end_position + 1)]

print(*result_numbers, end='\n\n')




#task 5

some_list: [int] = map(int, input("Ведите элементы списка через пробел: ").split())

some_list = list(filter(lambda num: '0' in str(num), some_list))

print(f"Отфильтрованный список с числами содержащими 0: {some_list}\n")




#task 6

words_list: [str] = input("Введите слова-элементы списка через пробел: ").split()

a_triple_consists_words: [str] = list(filter(lambda word: word.count('a') > 2 or word.count('а') > 2, words_list))

print(f"Слова имеющие больше 2-х 'а': {a_triple_consists_words}\n")



#task 7

string_list: [str] = input("Введите строки-элементы списка через '/': ").split('/')

string_list = list(map(lambda string_element: string_element.upper(), string_list))

print("Строки списка в верхнем регистре:", *string_list, '\n', sep='\n')




# task 8

def remove_digits_from_str(string: str) -> str:
    temp: str = ""
    for char in string:
        if char.isdigit():
            continue
        else:
            temp += char
    return temp


string_list: [str] = input("Введите строки-элементы списка через '/': ").split('/')

string_list = list(map(remove_digits_from_str, string_list))

print("Строки списка с удаленными цифрами:", *string_list, '\n', sep='\n')


# task 9*

numbers_list: [int] = list(map(int, input("Введите числа через пробел: ").split()))

numbers_list = list(set(filter(lambda num: numbers_list.count(num) > 1, numbers_list)))

print(*numbers_list, end="\n\n")




# task 10*

def is_prime(number: int) -> bool:
    for divisor in range(2, int(number**1/2) + 1):
        if number % divisor == 0:
            return False
    return True


prime_numbers: [int] = [num for num in range(2, 101) if is_prime(num)]

print("Простые числа до 100: ", *prime_numbers, end="\n\n")




# task 11*

some_list: [int] = list(map(int, input("Введите элементы списка через пробел: ").split()))

zero_counts: int = len(some_list) - 1
zero_position: int = 1

for _ in range(zero_counts):
    some_list.insert(zero_position, 0)
    zero_position += 2

print(*some_list, '\n')




# task 12*

some_list = list(map(int, input("Введите элементы списка через пробел: ").split()))

if len(some_list) == 1:
    print(*some_list)
else:
    index_prev: int = len(some_list) - 1
    index_next: int
    result_list: [int] = []
    for index in range(len(some_list)):
        index_next = index + 1
        if index_next == len(some_list):
            index_next = 0
        result_list.append(some_list[index_prev] + some_list[index_next])
        index_prev = index

    print(*result_list)