class Subway:
  fare = 2.4
  def __init__(self):
    self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
    self.current_stop= "Alewife"
    self.direction = "south"
    self.passengers = 0
    self.total_fares = 0

  def board(self, boarding):
    self.passengers += boarding
    self.total_fares += boarding * Subway.fare

  def disembark(self, exiting):
    if exiting > self.passengers:
      self.passengers = 0
    else:
      self.passengers -= exiting

  def advance(self, direction):
    self.direction = direction
    stop = self.current_stop
    if self.direction == 'south' and stop != 'Kendall':
      self.current_stop = self.stops[self.stops.index(stop) + 1]
    elif self.direction == 'north' and stop != 'Alewife':
      self.current_stop = self.stops[self.stops.index(stop) - 1]
    elif self.direction == 'south' and stop == 'Kendall':
      self.direction = 'north'
      self.current_stop = 'Central'
    elif self.direction == 'north' and stop == 'Alewife':
      self.direction = 'south'
      self.current_stop = 'Davis'

  def distance(self, stop):
    return abs((self.stops.index(self.current_stop) + 1) - (self.stops.index(stop) + 1))

  @classmethod
  def change_fare(cls, new_fare):
    Subway.fare = new_fare

  def calculate_fares(self, boarding):
    total_fares = boarding * Subway.fare
    self.total_fares += total_fares

'''
train1 = Subway()
train1.advance('south')
print(train1.current_stop)
train1.advance('south')
print(train1.current_stop)
train1.advance('south')
print(train1.current_stop)
train1.advance('south')
print(train1.current_stop)
train1.advance('south')
print(train1.current_stop)

train1.board(100)
train1.calculate_fares(100)
print(train1.passengers, train1.total_fares)

print(Subway.fare)
train1.change_fare(3.5)
print(Subway.fare)

train1.disembark(50)
print(train1.passengers)

print(train1.distance('Alewife'))
'''