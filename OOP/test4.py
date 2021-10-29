class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager:
    def __init__(self,name,pay):
        self.person = Person(name,'mgr',pay)
    def giveRaise(self,percent,bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person,attr)

    def __repr__(self):
        return str(self.person)

if __name__ == "__main__":
    bob = Person('bob Smith',pay=10000)
    print(bob.name)
    tom = Manager('Ton Jones',54324)
    print(tom)



