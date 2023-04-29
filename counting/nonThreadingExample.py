import time as t

t1 = t.time()


# code for the task to be executed individually
a = 0
for i in range(100000):
    a += 1
    print("a")

# code for the task to be executed individually
b = 0
for i in range(100000):
    b += 1
    print("b")

t2 = t.time()

totalTime = t2-t1

print(f"Calculations done in {totalTime:.10f}s") # explanation: In this case, `.15` means to include 15 decimal places