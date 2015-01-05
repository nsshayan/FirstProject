
class Person():
	def __init__(self,name):
		self.name = name
	def say_hi(self):
		print "Hi my name is,", self.name
	

P = Person(6)
Q = Person('shayan')

P.say_hi()
Person.say_hi(Q)


