#Class_Student_2.py



class Service:
    secret = "영구는 배곱이 두개다."
    def setname(self,name):
        self.name = name
    def sum(self,a,b):
        result = a + b
        print("%s님 %s + %s =%s입니다." % (self.name,a,b,result))
