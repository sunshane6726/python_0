# program_inputoutput1.py

def fib(n): # 재귀호출을 이용하면 피보나치 함수를 다음과 같이 간단하게 작성 할 수 있다.
    if n == 0: return 0 # n이 0일 때는 0을 리턴
    if n == 1: return 1 # n이 1일 때는 1을 리턴
    return fib(n-2) + fib(n-1) # n이 2 이상일 때는 그 이전의 두 값을 더하여 리턴

for i in range(10):
    print(fib(i))
    

