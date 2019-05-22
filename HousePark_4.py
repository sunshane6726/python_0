
#HousePark_4.py
"""

더이상 그런말을 하지말자 클래스를 통안 연습을 잘해보자
"""
# __init)) 메서드로 초기값을 설정한다.

class HousePark:
    lastname = "박"
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self,where):
        print("%s, %s여행을 가자 " % (self.fullname,where))
    def love(self,other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname,other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼을 했네" % (self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "김"
    def travel(self,where,day):
        print("%s, %s여행을 %d일 가면서 휴식을 가자 " % (self.fullname,where,day))
pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.love(juliet)
pey + juliet

