#! /usr/bin/python
"""house2.py -- Another house.
"""

class House(object):
	def __init__(self, number, rooms, garden):
		self.number = number
		self.rooms = rooms
		self.garden = garden

my_house = House(20, 1, 0)

print "My house is number", my_house.number
print "It has", my_house.rooms, "rooms"
if my_house.garden:
	garden_text = "has"
else:
	garden_text = "does not have"
print "It", garden_text, "a garden"
