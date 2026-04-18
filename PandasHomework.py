import pandas as pd
import numpy as np

data = {
    "student": ["Aliya", "Dias", "Arman", "Aruzhan", "Nursultan", "Ayan", "Madi", "Dana"],
    "age": [19, 20, 18, 21, 22, 19, 20, 18],
    "math": [85, 70, 90, 60, 75, 88, 92, 66],
    "physics": [80, 65, 95, 55, 78, 85, 91, 60],
    "programming": [90, 75, 88, 62, 80, 92, 94, 70]
}

df = pd.DataFrame(data)
print("\n--- Исходная таблица ---")
print(df)

print("\n--- head(3) ---")
print(df.head(3))


print("\n--- columns ---")
print(df.columns)

print("\n--- math column ---")
print(df["math"])

print("\n--- iloc[2:5, 0:3] ---")
print(df.iloc[2:5, 0:3])

print("\n--- math > 80 ---")
print(df[df["math"] > 80])

print("\n--- sort by physics ---")
print(df.sort_values(by="physics", ascending=False))

df["average"] = df[["math", "physics", "programming"]].mean(axis=1)
print("\n--- таблица с average ---")
print(df)

print("\n--- средние значения предметов ---")
print(df[["math", "physics", "programming"]].mean())

print("\n--- groupby age (average) ---")
print(df.groupby("age")["average"].mean())

print("\n--- Выводы ---")
print("1. Лучшие результаты у студентов с высокими баллами по всем предметам.")
print("2. Madi имеет один из самых высоких средних баллов.")
print("3. Есть значительный разброс между студентами по успеваемости.")
print("4. Физика в среднем немного сложнее других предметов.")
print("5. Возраст не сильно влияет на успеваемость.")