# # Задача 1
# numbers = [3, 8, 15, 6, 2, 9]

# sum_even = 0
# for num in numbers:
#     if num % 2 == 0:
#         sum_even += num

# print("Сумма чётных чисел:", sum_even)

# # Задача 2
# numbers = [3, 8, 15, 6, 2, 9]

# sum_even = sum(num for num in numbers if num % 2 == 0)

# print("Сумма чётных чисел:", sum_even)

# # Задача 3
# products = {
#     "Хлеб": 50,
#     "Молоко": 80,
#     "Сыр": 120,
#     "Яблоки": 90
# }

# most_expensive = max(products, key=products.get)

# print("Самый дорогой товар:", most_expensive)
# print("Цена:", products[most_expensive])

# grades = [8, 12, 15, 7, 10, 9, 14]

# count = sum(1 for grade in grades if grade >= 10)

# print("Количество оценок ≥ 10:", count)

# # Задача 4
# student = {
#     "Имя": "Иван",
#     "Возраст": 16,
#     "Класс": 10,
#     "Средний балл": 11.4
# }

# print("Анкета ученика:")
# for key, value in student.items():
#     print(f"{key}: {value}")

# # Задача 5
# numbers = []

# for i in range(5):
#     num = int(input("Введите число: "))
#     numbers.append(num)

# print("Вы ввели:", numbers)
# print("Максимум:", max(numbers))
# print("Минимум:", min(numbers))
# print("Среднее:", sum(numbers) / len(numbers))