import pandas as pd

df_students = pd.read_csv("Data/2012/Students/Countries/Germany.csv", index_col=[0])
df_parents = pd.read_csv("Data/2012/Parents/Countries/Germany.csv", index_col=[0])
df_school = pd.read_csv("Data/2012/School/Countries/Germany.csv", index_col=[0])

print(df_students.shape)
print(df_parents.shape)
print(df_school.shape)
print('done!')