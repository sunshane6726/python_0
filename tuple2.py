# tuple2.py

a = (1,2,3)
print(id(a)) # a의 고유 주소값 출력

a = a + (4,)
print(a)
print(id(a)) # (4,) 값이 더해 진후 a의 고유 주소값 출력