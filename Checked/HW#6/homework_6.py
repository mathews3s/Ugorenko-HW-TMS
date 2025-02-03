import time

# функция для проверки декораторов из 6-7 задания
def example_function(msg: str):
    time.sleep(0.2)
    print(f"Отработка функции. ДОП.ИНФ: {msg}")



# task 1

some_list: [int] = ["Apple", "Banana", "Carrot", "Dog", "Elephant", "Frog", "Grape", "House", "Ice", "Jaguar"]

some_list.sort(key=len, reverse=True)

print(some_list, end="\n\n")




# task 2

some_list: [int] = ["aaaw", "aa", "aaaaaaaaaaa", "a", "Eaaaaf", "aaa"]

some_list.sort(key= lambda word: word.count('a'))

print(some_list, end="\n\n")




# task 3

school = {
    '9a': 24,
    '9б': 28,
    '9в': 30,
    '9м': 20,
    '9ф': 15,
    '9г': 10,
    '9д': 35,
}
print(f"Изначально:                  {school}")
school['9м'] = 27
print(f"Изменено кол-во учеников 9м: {school}")
school['9ж'] = 40
print(f"Новый класс 9ж:              {school}")
del school['9д']
print(f"Расформирован 9д:            {school}")
print(f"Всего учеников:              {sum(school.values())}", end="\n\n")




# task 4

phone_book = {}

while True:
    input_string = input("Введите запрос: ").split()

    if len(input_string) == 1:
        if input_string[0] == '.':
            print("Работа завершена", end="\n\n")
            break
        else:
            if input_string[0] in phone_book:
                print(f"Найден номер контакта: {phone_book[input_string[0]]}")
            else:
                print("Контакт не найден")
    else:
        name: str = input_string[0]
        phone_number: str = input_string[1]
        phone_book[name] = phone_number
        print("Контакт добавлен/изменен")




# task 5

def get_element(elements: list, index: int):
    try:
        return elements[index]
    except IndexError:
        raise IndexError("Ошибка: индекс вне диапазона")


try:
    print(get_element(elements=[1, 2, 3], index=2))
    print(get_element(elements=[1, 2, 3], index=7))
except Exception as error:
    print(error)

print("\n")





# task 6


def retry_on_exception(retries: int):
    def func_decorator(func: callable):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                raise ValueError(f"ValueError: Функция перевыполнится {retries} раз(-а)") # иммитация ValueError для проверки
            except ValueError as error:
                print(error)
                for _ in range(retries):
                    func(*args, **kwargs)

        return wrapper

    return func_decorator


example_function_with_retries = retry_on_exception(retries=2)(func=example_function)
example_function_with_retries(msg="Количество повторений - 2")
print("\n")




# task 7

def timeout(limit: float):
    def func_decorator(func: callable):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            if execution_time > limit:
                raise TimeoutError(f"TimeoutError: Время выполнения функции превысило {limit} секунд")
            return result

        return wrapper

    return func_decorator


try:
    example_function_with_limit = timeout(limit=1)(func=example_function)
    example_function_with_limit_2 = timeout(limit=0.1)(func=example_function)
    example_function_with_limit(msg="Лимит 1 сек., время исполнения функции 0.2 сек.")
    example_function_with_limit_2(msg="Лимит 0.1 сек., время исполнения функции 0.2 сек.")
except Exception as error:
    print(error)
