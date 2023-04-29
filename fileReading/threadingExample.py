import time as t
import threading
import pandas as pd
import math


def taskA():
    # code for the task to be executed concurrently
    df1 = pd.read_csv("data1.csv",  index_col=0)
    for i in df1["numbers"]:
        a = math.sqrt(i)

def taskB():
    # code for the task to be executed concurrently
    df2 = pd.read_csv("data2.csv",  index_col=0)
    for i in df2["numbers"]:
        a = math.sqrt(i+10001)

# create multiple threads
threadA = threading.Thread(target=taskA)
threadB = threading.Thread(target=taskB)

t1 = t.time()
# start the threads
threadA.start()
threadB.start()

# wait for threads to finish
threadA.join()
threadB.join()

t2 = t.time()

totalTime = t2-t1

print(f"Calculations done in {totalTime:.10f}s") # explanation: In this case, `.15` means to include 15 decimal places