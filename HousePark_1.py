# HousePark.py

## 박씨네 집으로 클래스를 구현해보다
"""

더이상 그런말을 하지말자 클래스를 통안 연습을 잘해보자
"""
class HousePark:
    lastname = "박"
    def setname(self,name):
        self.fullname = self.lastname + name
    def travel(self,where):
        print("%s, %s여행을 가자 " % (self.fullname,where))

pey = HousePark()
pey.setname("")
pey.setname("응용")
pey.travel("부산")


