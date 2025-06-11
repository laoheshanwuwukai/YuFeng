
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': ['x', 'y', 'z']
})

print(df.loc[0])    # 按标签访问行
print(df.iloc[0])   # 按位置访问行
# print(df[df['B'] > 15])  # 条件访问
