import pyreadstat
import pandas as pd

# 读取 .sav 文件
df, meta = pyreadstat.read_sav('1.sav')

# 将 DataFrame 保存为 CSV 文件
df.to_csv('output_file.csv', index=False)

print("文件已成功转换为 CSV 格式！")
