class Time_Machine:
 def __init__(self):
  self.year = 2023
  self.month = 12
  self.day = 31

 def travel_to(self, year, month=None, day=None):
  self.year = year
  if month: self.month = month
  if day: self.day = day
  print(f"Time machine traveled to {self.year}-{self.month}-{self.day}")
