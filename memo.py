# 간단한 메모장 만들기_1.py
# C:\Users\이하영 이동욱\PycharmProjects\untitled1\memo.

# memo.py


# C:\PycharmProjects\untitled1> 를 사용했으니 알기를 바란다.

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)

