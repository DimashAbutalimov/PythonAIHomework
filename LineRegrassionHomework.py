import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# =========================
# 1. Пример: Study Hours → Score
# =========================

data1 = {
    "hours_study": [1, 2, 3, 4, 5, 6, 7, 8],
    "score": [42, 48, 55, 61, 67, 72, 79, 85]
}

df1 = pd.DataFrame(data1)

X1 = df1[["hours_study"]]
y1 = df1["score"]

model1 = LinearRegression()
model1.fit(X1, y1)

pred1 = model1.predict(X1)

# предсказание
new_hours = pd.DataFrame({"hours_study": [9]})
print("Predicted score for 9 hours:", model1.predict(new_hours)[0])

print("Coefficient:", model1.coef_[0])
print("Intercept:", model1.intercept_)

# график
plt.scatter(X1, y1, label="Real data")
plt.plot(X1, pred1, label="Regression line")
plt.xlabel("Hours of study")
plt.ylabel("Score")
plt.title("Linear Regression: Study vs Score")
plt.legend()
plt.show()


# =========================
# 2. Пример: Experience → Salary
# =========================

data2 = {
    "exp_years": [1, 2, 3, 4, 5, 6, 7],
    "salary": [180000, 220000, 260000, 300000, 340000, 390000, 430000]
}

df2 = pd.DataFrame(data2)

X2 = df2[["exp_years"]]
y2 = df2["salary"]

model2 = LinearRegression()
model2.fit(X2, y2)

pred2 = model2.predict(X2)

print("\nSalary model coefficient:", model2.coef_[0])
print("Salary intercept:", model2.intercept_)

# предсказание
new_exp = pd.DataFrame({"exp_years": [8]})
print("Predicted salary for 8 years:", model2.predict(new_exp)[0])

# график
plt.scatter(X2, y2, label="Real data")
plt.plot(X2, pred2, label="Regression line")
plt.xlabel("Experience (years)")
plt.ylabel("Salary")
plt.title("Linear Regression: Experience vs Salary")
plt.legend()
plt.show()