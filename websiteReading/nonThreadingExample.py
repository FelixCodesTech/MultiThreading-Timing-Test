import time as t
import requests

url = "https://www.google.com"

t1 = t.time()

for i in range(100):
    # code for the task to be executed individually
    response = requests.get(url)

    #print(response.text)

t2 = t.time()

totalTime = t2-t1

print(f"Done in {totalTime:.10f}s") # explanation: In this case, `.15` means to include 15 decimal places