# getTotalPage_1.py

def getTotalPage(m,n):
    return m // n + 1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))

def getTotalPage_1(m,n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage_1(5,10))
print(getTotalPage_1(15,10))
print(getTotalPage_1(25,10))
print(getTotalPage_1(30,10))