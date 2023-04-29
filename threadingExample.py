import time as t
import threading


def taskA():
    # code for the task to be executed concurrently
    a = 123456789+987654321

def taskB():
    # code for the task to be executed concurrently
    b = 123456789+987654321-143602023

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