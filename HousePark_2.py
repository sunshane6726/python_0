## 박씨네 집으로 클래스를 구현해보다
#HousePark_2.py
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

pey = HousePark("응용")
pey.travel("태국")

