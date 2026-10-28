
import pandas as pd

url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"

df = pd.read_csv(url)

df.to_csv("titanic.csv", index=False)
#Task 1
print("Ilk 7 setir:")
print(df.head(7))

print("Son 3 setir:")
print(df.tail(3))

print(f"Setir ve sutun sayi: {df.shape}")

print(f"Sutun adlari: {df.columns.tolist()}")

print("Dataset melumatlari:")
df.info()

print("Statistik melumatlar:")
print(df.describe())

print(f"Age sutununda bos olmayan deyerlerin sayi: {df['Age'].count()}")

print("5-ci, 6-ci ve 7-ci movqelerdeki sernisinler:")
print(df.iloc[4:7])

print("Index label-i 10 olan sernisinin Name, Age ve Fare melumatlari:")
print(df.loc[10, ["Name", "Age", "Fare"]])

selected_columns = df[["Name", "Age", "Survived"]]

print("Name, Age ve Survived sutunlari:")
print(selected_columns.head(10))

# task 2 

# Part A - Adult Passengers

adult_passengers = df[
    (df["Age"] >= 18) &
    (df["Pclass"] == 3)
]

adult_result = adult_passengers[["Name", "Age", "Pclass", "Fare"]]

print("18 ve daha yuxari yasi olan, 3-cu sinifde seyahet eden sernisinler:")
print(adult_result.head(10))

print(f"Umumi sernisin sayi: {len(adult_result)}")


# Part B - Young Passengers

young_passengers = df[
    (df["Age"] < 18) &
    ((df["Pclass"] == 1) | (df["Pclass"] == 2))
]

young_result = young_passengers[["Name", "Age", "Pclass", "Survived"]]

print("18 yasdan kicik, 1-ci ve ya 2-ci sinifde seyahet eden sernisinler:")
print(young_result.head(10))

print(f"Umumi sernisin sayi: {len(young_result)}")

# Part A - Survived Passengers

survived_passengers = df[
    (df["Pclass"] == 1) &
    (df["Age"] >= 18) &
    (df["Survived"] == 1)
]

survived_result = survived_passengers[["Name", "Age", "Sex", "Fare"]]

print("Xilas olan sernisinler:")
print(survived_result.head(10))

survived_count = len(survived_result)
survived_average_fare = survived_result["Fare"].mean()

print(f"Xilas olan sernisinlerin sayi: {survived_count}")
print(f"Xilas olan sernisinlerin orta bilet qiymeti: {survived_average_fare:.2f}")


# Part B - Non-Survived Passengers

non_survived_passengers = df[
    (df["Pclass"] == 1) &
    (df["Age"] >= 18) &
    (df["Survived"] == 0)
]

non_survived_result = non_survived_passengers[["Name", "Age", "Sex", "Fare"]]

print("Xilas olmayan sernisinler:")
print(non_survived_result.head(10))

non_survived_count = len(non_survived_result)
non_survived_average_fare = non_survived_result["Fare"].mean()

print(f"Xilas olmayan sernisinlerin sayi: {non_survived_count}")
print(f"Xilas olmayan sernisinlerin orta bilet qiymeti: {non_survived_average_fare:.2f}")


# Part C - Final Report

print("TITANIC SURVIVAL REPORT")
print(f"Xilas olanlar: {survived_count} sernisin, orta bilet qiymeti: {survived_average_fare:.2f}")
print(f"Xilas olmayanlar: {non_survived_count} sernisin, orta bilet qiymeti: {non_survived_average_fare:.2f}")
