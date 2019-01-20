def GuGu(n):
    result = []
    result.append(n * 1)
    result.append(n * 2 )
    result.append(n * 3)
    result.append(n * 4)
    result.append(n * 5)
    result.append(n * 6)
    result.append(n * 7)
    result.append(n * 8)
    result.append(n * 9)
    return result
print(GuGu(2))

i = 1
while i < 10:
    print(i)
    i = i + 1

def GuGu_1(n):
    result_1 = []
    i= 1
    while i < 10:
        result_1.append(n*i)
        i = i + 1
    return result_1  #근해야 머리가 덜 아프다는 것을 기억하자. 자 # 이제 다양한 예제들은 접해 보며 여러분 나름대로 멋진 생각들을 해보기 바란다
print(GuGu_1(2))

#그래야지 말이 된다 ##
result = 1
for n in range(1,200):
    if n % 3 == 0 or n % 5 == 0: # 15와 같이 3의 배수도 되고 5의 배수도 되는 값이 이중으로 더 해지지 않기 위해 or 연산자 사용
        result +=  n
print(result)

