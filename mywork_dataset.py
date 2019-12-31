%matplotlib inline

import matplotlib.pyplot as plt
import pandas as pd
import random

# データサンプル数
SAMPLE_DATA = 10000

# 表示の設定
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def Shape(height, weight):
    height = height / 100
    BMI = weight / (height * height)
    if BMI < 18.5: return "THIN"
    elif BMI < 25: return "USUAL"
    else: return "FAT"

def Scatter(shape, color, df):
    df_loc = df.loc[shape]
    ax.scatter(df_loc["height"], df_loc["weight"], c=color, label=shape)
    
data_list = []

# 辞書型リストの作成
for i in range(SAMPLE_DATA):
    height = random.randint(120, 200)
    weight = random.randint(20, 120)
    data_list.append({"height":height, "weight":weight, "shape":Shape(height, weight)})
    
# 辞書型リストからデータフレームへの変換 + インデックスの付加
df = pd.DataFrame(data_list)
df_index = df.set_index("shape")


Scatter("FAT", "red", df_index) 
Scatter("USUAL", "purple", df_index)
Scatter("THIN", "blue", df_index)

ax.legend()
plt.savefig("bmi_test.png")
plt.show()