#! /usr/bin/python
"""person.py -- A person example.
"""
class Person(object):
	def __init__(self, age, house_number):
		self.age = age
		self.house_number = house_number

alex = []
for i in range(5):
	obj = Person(i, i)
	alex.append(obj)

print "Alex[3] age is", alex[3].age
print

for alexsub in alex:
	print "Age is", alexsub.age
	print "House number is", alexsub.house_number
