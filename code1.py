class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passanger(self, name):
        if not self.seats():
            return False
        self.passangers.append(name)
        return True

    def seats(self):
        return self.capacity - len(self.passangers)

a = ['aslan','isa','roma','salah']
c = Flight(3)
for i in a:
    succes = c.add_passanger(i)
    if succes:
        print(f'added {i} to flight successfully')
    else:
        print(f'No Available seats for {i}')