class Car:
    def __init__(self, engine, velocity, colour, doors, valves:6):

      self.velocity = velocity
      self.engine = engine
      self.valves = valves
      self.colour = colour
      self.doors = doors
      
#METHODS
    def check_engine(self, engine):
      return self.engine

    def increase_valve(self, new_valve):
      self.valves = self.valves + new_valve
      return self.valves

    def get_distance_covered(self, time):
      return self.velocity * time

    def change_colour(self):
      return self.colour
    
    def get_number_of_doors(self):
      return self.doors  

# METHODS PRINT      
#Mercedes_Benz

My_benz =Car("internal combustion", 6, "navy blue", 4, 6)

print("my new benz engine is", My_benz.engine)
print("the number of valves are", My_benz.valves)
#To increase valves
print("I have increased my valves to", My_benz.increase_valve(2))
print("The color of my benz is", My_benz.colour)
print("The maximum distance that can be covered by my benz in 4 hours is", My_benz.get_distance_covered(65), "km")
print("The number of doors my benz has is", My_benz.doors)
