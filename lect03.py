import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/allatambov/PyReg25/refs/heads/main/hp25.csv")

### PART 01: GRAPHS ###

df["Age"].hist()
df["Age"].hist(color = "purple", edgecolor = "white")
df["Age"].plot.box()

### PART 02: SORTING ###

df.sort_values("Birth.year")
df.sort_values("Birth.year", ascending = False)
df.sort_values("Name")

df_full = df.dropna()
print(len(df_full))

df_full.sort_values(["House", "Wand.len"])
df_full.sort_values(["House", "Wand.len"], ascending = [True, False])

### PART 03: GROUPING ###

df_full.groupby("House").describe()
df_full.groupby("House")["Age"].describe()
df_full.groupby(["House", "Gender"])["Age"].describe()


