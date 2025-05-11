class mobile:
    def __init__(self):
        self.brand="samsung"
        self.cost=20000
    def on(self):
        self.ontime="3seconds"
m1=mobile()
print(m1.brand)
print(m1.cost)
m1.on()
print(m1.ontime)
m1.colour="black"
print(m1.colour)
