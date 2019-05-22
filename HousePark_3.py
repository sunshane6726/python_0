#HousePark_3.py

# 클래스의 상속이라는 것에 대해 배워보자.

class HouseKim(HousePark):
    lastname = "김"
    def travel(self,where,day):
        print("%s, %s여행을 %d일 가면서 휴식을 가자 " % (self.fullname,where,day))