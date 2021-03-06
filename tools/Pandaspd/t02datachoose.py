import pandas as pd
import numpy as np

dates = pd.date_range('20200217', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
'''
             A   B   C   D
2020-02-17   0   1   2   3
2020-02-18   4   5   6   7
2020-02-19   8   9  10  11
2020-02-20  12  13  14  15
2020-02-21  16  17  18  19
2020-02-22  20  21  22  23
'''

# 获取某行
# 见下面通过切片获取和通过标签获取
print(df['20200218':'20200218'])  # 含首也含尾
#             A  B  C  D
# 2020-02-18  4  5  6  7
print(df[1:2])  # 含首不含尾
#             A  B  C  D
# 2020-02-18  4  5  6  7


# 获取某列
print(df['A'])
# 或
print(df.A)
'''
2020-02-17     0
2020-02-18     4
2020-02-19     8
2020-02-20    12
2020-02-21    16
2020-02-22    20
Freq: D, Name: A, dtype: int32
'''

# 对行进行切片
## 按数字索引
print(df[0:3])  # 含首不含尾
'''
            A  B   C   D
2020-02-17  0  1   2   3
2020-02-18  4  5   6   7
2020-02-19  8  9  10  11
'''

## 按索引名称
print(df['20200217':'20200219'])  # 含首也含尾
'''
            A  B   C   D
2020-02-17  0  1   2   3
2020-02-18  4  5   6   7
2020-02-19  8  9  10  11
'''

# 获取索引名称（loc）获取Dataframe子数据
## 取某一行（只能传一行）
print(df.loc['20200218'])
'''
A    4
B    5
C    6
D    7
Name: 2020-02-18 00:00:00, dtype: int32
'''

## 取某行的若干个属性（列）
print(df.loc['20200218', ['A', 'C', 'D']])
'''
A    4
C    6
D    7
Name: 2020-02-18 00:00:00, dtype: int32
'''

## 获取所有行的若干属性（列）
print(df.loc[:,['A','B']])
#              A   B
# 2020-02-17   0   1
# 2020-02-18   4   5
# 2020-02-19   8   9
# 2020-02-20  12  13
# 2020-02-21  16  17
# 2020-02-22  20  21


# 获取序数索引（iloc）获取Dataframe子数据
print(df.iloc[3,1])     # 获取索引行3列1的值
# 13
print('-------------------------------------------')
print(df.iloc[3:5,1:3])
# 含首不含尾，其中单一个冒号（:）表示去这一维的所有；-1表示这一维的最后一项；（:3）表示从0到3；（3:）表示从3到最后一项（含）
'''
             B   C
2020-02-20  13  14
2020-02-21  17  18
'''

# 离散切取
print(df.iloc[[1,3,5],1:3])
'''
             B   C
2020-02-18   5   6
2020-02-20  13  14
2020-02-22  21  22
'''

# 还可以通过删选切取
print(df[df.A>8])
'''
             A   B   C   D
2020-02-20  12  13  14  15
2020-02-21  16  17  18  19
2020-02-22  20  21  22  23
'''