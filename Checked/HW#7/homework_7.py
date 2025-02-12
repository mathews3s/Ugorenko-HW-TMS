import os
import json
import csv
from datetime import timedelta, datetime


# task 1

numbers: [int] = [1, 2, 3, 1, 1, 2, 1, 1, 1, 1]
numbers_in_string: str = " ".join(map(str, numbers))
input_filename: str = "input.txt"
directory_path: str = "files"
writing_mode: str = "w"
input_file_path: str = os.path.join(directory_path, input_filename)


try:
    with open(input_file_path, writing_mode) as input_source:
        input_source.write(numbers_in_string)
except Exception as e:
    print("Произошла ошибка при работе с файлом. Подробности: ", e)
else:
    print(f"Файл {input_file_path} был успешно создан. Записаны элементы массива: {numbers}")




# task 2

input_filename: str = "input.txt"
output_filename: str = "output.txt"
directory_path: str = "files"
writing_mode: str = "w"
reading_mode: str = "r"
input_file_path: str = os.path.join(directory_path, input_filename)
output_file_path: str = os.path.join(directory_path, output_filename)
input_numbers: [int] = []
numbers_product: int = 1

try:
    with open(input_file_path, reading_mode) as input_source:
        input_numbers = list(map(int, input_source.read().split()))
        for number in input_numbers:
            numbers_product *= number
    with open(output_file_path, writing_mode) as output_source:
        output_source.write(str(numbers_product))
except Exception as e:
    print("Произошла ошибка при работе с файлом. Подробности: ", e)
else:
    print(f"Файл {output_file_path} был успешно создан. "
          f"Записано произведение чисел из {input_file_path}: {numbers_product}")




# task 3


input_filename: str = "stock inventory.txt"
directory_path: str = "files"
reading_mode: str = "r"
input_file_path: str = os.path.join(directory_path, input_filename)
current_date = datetime.today()
filter_date = current_date - timedelta(days=30)
arrived_date = None
arrived_date_string: str = ""
table_header: str = ""
skip_table_header: int = False

print(f"Текущая дата: {current_date.day}.{current_date.month}.{current_date.year}")
print(f"Товары хранящиеся больше месяца и стоящие больше 1000000 \nимеют дату поступления до: "
      f"{filter_date.day}.{filter_date.month}.{filter_date.year}\nСписок товаров:\n")

try:
    with open(input_file_path, reading_mode) as file:
        for line in file:
            if not skip_table_header:
                print(line, end="")
                skip_table_header = True
            else:
                arrived_date_string = line.split()[3]
                arrived_date = datetime.strptime(arrived_date_string, "%d.%m.%Y")
                if arrived_date < filter_date:
                    print(line, end="")
except Exception as e:
    print("Произошла ошибка при работе с файлом. Подробности: ", e)
print('\n')




# task 4

answers_filename: str = "answers.txt"
questions_filename: str = "questions.txt"
directory_path: str = "files"
reading_mode: str = "r"
answers_file_path: str = os.path.join(directory_path, answers_filename)
questions_file_path: str = os.path.join(directory_path, questions_filename)
user_score = 0

try:
    with open(questions_file_path, reading_mode, encoding='utf-8') as q_file:
        questions = q_file.readlines()
    with open(answers_file_path, reading_mode) as a_file:
        answers = a_file.readlines()
except Exception as e:
    print("Произошла ошибка при работе с файлом. Подробности: ", e)
else:
    questions_order = zip(questions, answers)

    for question, correct_answer in questions_order:
        print(question, end="")
        user_answer: str = input("Ваш ответ: ")

        if user_answer.lower() == correct_answer.strip().lower():
            user_score += 1

print(f"Количество верных ответов: {user_score}\n")




#task 5

output_filename: str = "data.json"
directory_path: str = "files"
writing_mode: str = "w"
output_file_path: str = os.path.join(directory_path, output_filename)

some_data = {
    11111: ("Ben", 30),
    22222: ("Andrei", 25),
    33333: ("Matsvei", 28),
    44444: ("Ivan", 22),
    55555: ("Ira", 35)
}

with open(output_file_path, writing_mode, encoding='utf-8') as json_file:
    json.dump(some_data, json_file, indent=2)




# task 6

output_filename: str = "data.csv"
input_filename: str = "data.json"
directory_path: str = "files"
writing_mode: str = "w"
reading_mode: str = "r"
input_file_path: str = os.path.join(directory_path, input_filename)
output_file_path: str = os.path.join(directory_path, output_filename)
some_data = {}

with open(input_file_path, reading_mode) as json_file:
    some_data = json.load(json_file)

with open(output_file_path, writing_mode, newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    for key, value in some_data.items():
        writer.writerow([f'person {key}', value[0], value[1]])