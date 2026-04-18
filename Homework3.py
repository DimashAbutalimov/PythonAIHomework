# # Задание 1
# tasks = []

# with open("data/todo.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         if not line:
#             continue
#         tasks.append(line)

# new_task = input("Введите новую задачу: ").strip()

# if new_task:
#     tasks.append(new_task)

# with open("data/todo.txt", "w", encoding="utf-8") as f:
#     for task in tasks:
#         f.write(task + "\n")

# print("Всего задач:", len(tasks))

# # Задание 2
# visits = {}

# with open("data/visits.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         site = line.strip()
#         if not site:
#             continue
#         visits[site] = visits.get(site, 0) + 1

# total = sum(visits.values())

# top_site = max(visits, key=visits.get)

# report_lines = []

# for site, count in visits.items():
#     percent = (count / total) * 100
#     line = f"{site}: {count} ({percent:.1f}%)"
#     report_lines.append(line)
#     print(line)

# top_line = f"TOP SITE: {top_site}"
# report_lines.append(top_line)
# print(top_line)

# with open("data/visits_report.txt", "w", encoding="utf-8") as f:
#     for line in report_lines:
#         f.write(line + "\n")

# import csv

# good_students = []
# total = 0

# with open("data/students.csv", "r", encoding="utf-8", newline="") as f:
#     reader = csv.DictReader(f)
    
#     for row in reader:
#         if not row:
#             continue
        
#         total += 1
        
#         name = row["name"]
#         age = int(row["age"])
#         grade = float(row["grade"])
        
#         if grade >= 85:
#             good_students.append({
#                 "name": name,
#                 "age": age,
#                 "grade": grade
#             })

# with open("data/good_students.csv", "w", encoding="utf-8", newline="") as f:
#     fieldnames = ["name", "age", "grade"]
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
    
#     writer.writeheader()
#     for student in good_students:
#         writer.writerow(student)

# print("Всего студентов:", total)
# print("Прошли фильтр:", len(good_students))