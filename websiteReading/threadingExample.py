import time as t
import threading
import requests

url = "https://www.google.com"

def task():
    # code for the task to be executed concurrently
    response = requests.get(url)

    #print(response.text)  

t1 = t.time()

num_threads = 100

# create and start threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=task)
    thread.start()
    threads.append(thread)

# wait for threads to finish
for thread in threads:
    thread.join()

t2 = t.time()

totalTime = t2-t1

print(f"Done in {totalTime:.10f}s") # explanation: In this case, `.15` means to include 15 decimal places