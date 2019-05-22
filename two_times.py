# two_times.py

def two_times(numberList):
    result = []
    for number in numberList: # map(f,iterable)은 함수(f)와 반복가능한 자료형을 입력으로 받는다.
        result.append(number*2)
    return result

a = two_times([1,2,3,4])
print(a)
