# Bird_1.py

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


for i, name, in enumerate(['body','foo','bar', 'send']):
    print(i,name)