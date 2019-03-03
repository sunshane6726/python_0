# Threading1.py

import threading   #컴퓨터 동작하고 있는 프로세스라고 한다. 보통 1개의 프로세스는 1간지 일만 하지만 ,스레드를 이용하면 한 프로세스

import time        #내에서 2가지 또는 그 이상의 일을 동시에 수행하ㅔ 할 수 있다. 간단한 예제로 설명을 대신하겠다.
def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you', 'need', 'python']:
    t = threading.Thread(target = say, args = (msg,))
    t.daemon = True
    t.start()
for i in range(100):
    time.sleep(0.1)
    print(i)