import pandas as pd


info={
    "name":["dagi","someone","yesssy"],
    "age":["21","24","27"],
    "city":["addis","abeba","bahirdar"]
        }
df=pd.DataFrame(info)
print(df)


df2=pd.read_csv("Data.csv")

#print(df2)
print(df2.head(1))
print(df2.tail(1))
print(df2.info())
print(df2[["City","Name"]],)
print(df2.loc[2,"City"])
total=0