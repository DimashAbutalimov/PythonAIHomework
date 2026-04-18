import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = {
    "student_id": [101,102,103,104,105,106,107,108],
    "name": ["Ali", "Aruzhan", "Mansur", "Dana", "Dana", None, "Nurlan", "Aizhan"],
    "age":[17,18,np.nan,17,17,19,"18",20],
    "city":["aktobe", "Astana", "Aktobe",None,None,"Aktobe","Almaty", "astana"],
    "math_score": [85,90,78,None,None,92,88,"91"],
    "attendance": [95,99,70,100,100,None,85,93],
    "passed": ["yes","yes","no","yes","yes","yes","no","yes"]
}

df = pd.DataFrame(data)

# -----------------------------
# 1. Очистка данных
# -----------------------------
df_clean = df.copy()

df_clean["age"] = pd.to_numeric(df_clean["age"], errors="coerce")
df_clean["math_score"] = pd.to_numeric(df_clean["math_score"], errors="coerce")
df_clean["attendance"] = pd.to_numeric(df_clean["attendance"], errors="coerce")

df_clean["city"] = df_clean["city"].fillna("unknown").str.lower()

# заполняем пропуски средними значениями
df_clean["age"] = df_clean["age"].fillna(df_clean["age"].mean())
df_clean["math_score"] = df_clean["math_score"].fillna(df_clean["math_score"].mean())
df_clean["attendance"] = df_clean["attendance"].fillna(df_clean["attendance"].mean())

print("Очищенные данные:")
print(df_clean)
print()

# -----------------------------
# 2. Выбираем числовые признаки
# -----------------------------
features = df_clean[["age", "math_score", "attendance"]]

# -----------------------------
# 3. Min-Max Normalization (0–1)
# -----------------------------
minmax = MinMaxScaler()
scaled_minmax = minmax.fit_transform(features)

df_minmax = pd.DataFrame(scaled_minmax, columns=features.columns)

print("Min-Max нормализация:")
print(df_minmax)
print()

# -----------------------------
# 4. Standardization (mean=0, std=1)
# -----------------------------
standard = StandardScaler()
scaled_std = standard.fit_transform(features)

df_std = pd.DataFrame(scaled_std, columns=features.columns)

print("Standardization:")
print(df_std)

# -----------------------------
# 5. Визуализация сравнения
# -----------------------------
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.title("Original")
plt.hist(df_clean["math_score"])

plt.subplot(1,3,2)
plt.title("MinMax")
plt.hist(df_minmax["math_score"])

plt.subplot(1,3,3)
plt.title("Standard")
plt.hist(df_std["math_score"])

plt.tight_layout()
plt.show()