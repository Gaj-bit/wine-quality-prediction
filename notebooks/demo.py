import pandas as pd

df = pd.read_csv("winequality.csv")

numeric_feature = [feature for feature in df.columns]

print(numeric_feature)

print(df[numeric_feature[0]].dtype == "object")
