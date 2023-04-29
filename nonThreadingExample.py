import time as t

t1 = t.time()


# code for the task to be executed individually
a = 123456789+987654321

# code for the task to be executed individually
b = 123456789+987654321-143602023

t2 = t.time()

totalTime = t2-t1

print(f"Calculations done in {totalTime:.10f}s") # explanation: In this case, `.15` means to include 15 decimal places