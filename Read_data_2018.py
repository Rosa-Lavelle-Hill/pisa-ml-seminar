# data checks:
import pandas as pd

df_students = pd.read_csv("Data/2018/Students/Countries/DEU.csv")
df_schools = pd.read_csv("Data/2018/School/Countries/DEU.csv")
df_teachers = pd.read_csv("Data/2018/Teachers/Countries/DEU.csv")

df_students_i = pd.read_csv("Data/2018/Students/Countries/IRL.csv")
df_schools_i = pd.read_csv("Data/2018/School/Countries/IRL.csv")
df_teachers_i = pd.read_csv("Data/2018/Teachers/Countries/IRL.csv")

print('done!')