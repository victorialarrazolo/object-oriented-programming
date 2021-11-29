#Victoria Larrazolo lesson 6 Hands On
#Part 1

class stadium:
    def __init__ (self, name, city_state, capacity, sport_played,seats_available):
     self.name = name
     self.city_state = city_state
     self.capacity =capacity
     self.sport_played = sport_played
     self.seats_available = seats_available
    def describe_stadium (self):
         print("The" + " " + self.name + " " + "is located in" + " " + self.city_state + ", and holds" + " " + self.capacity + " " + "fans." + " " + "The following sport is mainly played in this stadium:" + " " + self.sport_played + ", " + " " + "there are" + " " + self.seats_available + " " + "seats available for tonights game.")
""" create an instance of this class"""
stadium1 = stadium ("Mercedes Benz Arena", "Atlanta, GA", "70,000", "Football", "15,000")
"""Call the function"""
stadium1.describe_stadium()
