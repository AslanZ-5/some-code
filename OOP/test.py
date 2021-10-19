class C2:
    a = 32


class C3:
    b = 44


class C1(C2,C3):
    def setname(self,who):
        self.name = who

i1= C1()
i2 = C1()
i1.setname('aslan')
i2.setname('shamil')
print(i1.name)

