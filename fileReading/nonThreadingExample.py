import time as t
import pandas as pd
import math

t1 = t.time()


# code for the task to be executed individually
df1 = pd.read_csv("data1.csv",  index_col=0)
for i in df1["numbers"]:
    a = math.sqrt(i)

df2 = pd.read_csv("data2.csv",  index_col=0)
for i in df2["numbers"]:
    a = math.sqrt(i+10001)

# code for the task to be executed individually
df2 = pd.read_csv("data2.csv")

t2 = t.time()

totalTime = t2-t1

print(f"Calculations done in {totalTime:.10f}s") # explanation: In this case, `.15` means to include 15 decimal places