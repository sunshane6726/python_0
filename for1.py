# for1.py

A = [70, 60, 55, 75, 95, 90, 80, 85, 100]
total = 0
for score in A:
    # A학급의 점수를 모두 더한다.
    total += score
    average = total/len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
    print(average) # 평균 79.0이 출력된다.
    # for문을 이용하여 먼저 총 점수를 구한 후 총 점수를 총 학생수로 나눙 평균점수로 구한다.