# while1.py

i = 0
while True:
    i += 1 # while문 수행 시 1씩중가
    if i > 5: break # i 값이 5이상이면 while문을 벗어난다.
    print('*'*i) # while문을 수행할때마다 i 값을 증가시킨다. 별 모양을 5번 출력해야 하므로 i 값이 5이상일 경우 while문을 벗어나도록 한다
                 # 별 모양을 i 값 만큼 출력하기위해서는 문자열 곱하기 기능을 이용한다.
    