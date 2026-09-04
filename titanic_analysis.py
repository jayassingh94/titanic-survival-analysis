def greet ():
    print("Hello!")
greet()
def greet (Jaya):
    print("Hello" ,Jaya)
greet("Jaya")
greet("Manu")
def greet (Manu):
    print("Hello", Manu)
greet("Manu")
greet("Jaya")
greet("Amit")
def count_passed(marks_list):
    count = 0
    for i in range(len(marks_list)):
        if marks_list[i] >= 75:
            count = count + 1
    return count
marks = [90, 80, 85,95,70]
result = count_passed (marks)
print ("students who passed", result)
def find_highest(marks_list):
  highest = marks_list [0]
  for i in range (len(marks_list)):
      if marks_list [i] > highest:
          highest = marks_list[i]
          return highest
marks = [ 90,80,85,95,70]
result = find_highest(marks)
print ("highest:" , result)
def find_lowest(marks_list):
    lowest = marks_list[0]
    for i in range (len(marks_list)):
        if marks_list[i] < lowest:
            lowest = marks_list[i]
    return lowest
marks = [ 70,86,89,95]
result = find_lowest(marks)
print ("lowest:" , result)
def count_failed(marks_list):
    count = 0
    for i in range (len(marks_list)):
        if marks_list [i] < 75:
            count = count +1
    return count
marks = [65,80,75,98]
result = count_failed(marks)
print ("students who failed", result)
def add_bonus(marks_list, bonus):
    new_marks = []
    for i in range (len(marks_list)):
        new_marks.append (marks_list[i] + bonus )
    return new_marks
marks = [65,80,75,98]
result = add_bonus (marks, 5)
print ("New_Marks:" , result)
def greet (Manu):
 print ("Hello", Manu)
greet("JAya")
greet("Riya")
greet("Aman")
def count_passed(marks_list):
    count = 0
    for i in range (len(marks_list)):
      if marks_list [i] >= 50:
         count= count +1
    return count
marks = [40,50,70,89,67]
result = count_passed(marks)
print("students who passed", result)
def add_bonus(marks_list, bonus):
    list = []
    for i in range(len(marks_list)):
        list.append(marks_list[i] + bonus)
    return list
marks= [50,70,60,70]
result = add_bonus(marks,5)
print("list", result)
file = open ("marks.txt", "w")
file.write ("Amit - 90\n")
file.write ("Priya - 80\n")
file.close()
file = open("marks.txt", "r")
content = file.read()
print(content)
file.close()
file= open("marks.txt" , "r")
lines = file.readlines()
print(lines)
file.close()
file = open("marks.txt", "r")
lines= file.readlines()
file.close()

for line in lines:
    print(line.strip())

students = {
    "name" : ["amit", "priya", "Manu"],
    "marks" : [90, 80, 70]
}
    
import pandas as pd
df = pd.DataFrame(students)     
print(df)  
print (df[df["marks"] >= 75])    


data = {
    "name" :["Prem", "Manu","Priya"],
    "marks" : [90,None , 80]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.dropna())
print(df.fillna(0))
Data = {
    "name": ["suresh","suresh", "mohit","mohit"],
    "subject": ["maths","science", "maths","science"],
    "marks" : [70,80,90,70]
}
df= pd.DataFrame(Data)
print(df)
print(df.groupby("subject") ["marks"].mean())
print(df.groupby("name") ["marks"].sum())
df_marks = pd.DataFrame({
    "name" :["Amit","Manu","Priya"],
    "marks": [80,90,89]
})

df_attendance = pd.DataFrame({
    "name" : ("Amit", "Manu","Priya"),
    "attendance": (80,90,86)
})
marged = pd.merge(df_marks , df_attendance, on= "name")
print(marged)
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
