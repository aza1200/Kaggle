import pandas as pd


df = pd.DataFrame()

print(str(type(df)))

if str(type(df)) == "<class 'pandas.core.frame.DataFrame'>":
    print("hi")