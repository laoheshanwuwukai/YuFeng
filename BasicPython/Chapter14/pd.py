
import pandas as pd


a = pd.Series(range(1, 10))
print(a)
b = pd.DataFrame([[1, 2], [6, 7]], columns=[3, 4])
print(b)
print(b[3].sum())
