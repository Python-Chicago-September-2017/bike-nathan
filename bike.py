class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display_info(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        self.miles += 10
        return self
    def reverse(self):
        if self.miles >= 5:
            self.miles -= 5
        return self

bike_1 = Bike(100, "25mph")
bike_2 = Bike(100, "25mph")
bike_3 = Bike(100, "25mph")

print "#1"
bike_1.ride().ride().ride().reverse().display_info()
print "#2"
bike_2.ride().ride().reverse().reverse().display_info()
print "#3"
bike_3.reverse().reverse().reverse().display_info()
