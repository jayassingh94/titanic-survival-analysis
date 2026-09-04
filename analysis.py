
import pandas as pd
df= pd.read_csv(r"C:\Users\Jaya Singh\talkback_podcast\lib\core\constants\train.csv")
print (df.head())
print(df.shape)
print(df.columns)
print(df.isnull() .sum())
print(df["Survived"] . mean())
print(df.groupby("Sex")["Survived"].mean())
print(df.groupby("Pclass")["Survived"].mean())
print(df.groupby(["Sex", "Pclass"])["Survived"].mean() *100)
print(df.groupby("Sex")["Survived"].mean()*100)
import matplotlib.pyplot as plt
survival_by_sex = df.groupby("Sex")["Survived"].mean()*100
plt.bar(survival_by_sex.index, survival_by_sex.values)
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate(%)")
plt.savefig("Survival_by_Gender.png")
plt.show()
survival_by_class = df.groupby("Pclass")["Survived"].mean()*100
plt.bar(survival_by_class.index, survival_by_class.values, color = "green")
plt.title("Survival Rate by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate(%)")
plt.savefig("Survival_by_Class.png")
plt.show()
