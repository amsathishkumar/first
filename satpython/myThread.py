import threading
import time


def myFun(name):
    print(f'{name} Hello')
    time.sleep(1)
    print(f'Done {name}')


mythreads = []
for k in range(10):
    t = threading.Thread(target=myFun, args=['Sat'+str(k)])
    t.start()
    mythreads.append(t)

for mythread in mythreads:
    mythread.join()

print("The End")
