import pandas as pd

Result =[]
grade = []
hp =[]
df = pd.read_excel("StudentRecord.xlsx")
for x in range(len(df)):
    hp.append((int((sum(df.iloc[x][2:]))/6)))

for x in hp :
    if int(x) >= 40:
	    Result.append("Passed")
    else:Result.append("Failed")
for x in hp :
    if int(x) >= 70:
        grade.append("Distinction")
    elif int(x) >=60:
        grade.append("First Class")
    elif 60 >= int(x) >= 50:
        grade.append("Second Class")
    elif 50 >= int(x) >= 40:
        grade.append("Pass")
    else:
        grade.append("Failed")

df['Precentage'] = hp
df['Result'] = Result
df['Grades'] = grade

df.to_excel("test11.xlsx",index=False)
