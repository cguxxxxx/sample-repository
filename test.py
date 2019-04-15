from pandas import Series, DataFrame
import pandas as pd

df = pd.DataFrame(
    [[4,5,6],
    [5,8,11],
    [6,9,12]],
    index = [1,2,3],
    columns = ['a','b','c']
)
print(df)