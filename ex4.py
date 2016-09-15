# Assigns Int 100 to variable cars
cars = 100
# Assigns Floating Point 4.0 to space_in_a_car
# changing this value to 4 doesn't seem to change much, however,
# carpool_capacity is no longer a Floating Point number.
space_in_a_car = 4.0
# Assigns Int 30 to drivers
drivers = 30
# Assigns Int 90 to passengers
passengers = 90
# Assigns cars minus drivers to cars_not_driven
cars_not_driven = cars - drivers
# Assigns drivers to cars_driven
cars_driven = drivers
# Assigns cars_driven multiplied by space_in_a_car to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# Assigns passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
