import numpy as np
import pandas as pd


filename = "datasets/alltimegreats.csv"
filename2 = "datasets/newseasons.csv"

df = pd.read_csv(filename)

df2 = pd.read_csv(filename2)

df.drop_duplicates(subset=df.columns[0], keep='first', inplace=True)

mask = df.iloc[:, 0].isin(df2.iloc[:, 0])

filtered = df[~mask]


filtered.to_csv("haha.csv", index = False)





