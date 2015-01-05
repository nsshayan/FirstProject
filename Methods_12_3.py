
# self arguement is necessary in python. 
class Person: 
	def say_hi(self):
		print "Hi, How are you?"
	def say_bye(self):
		print "Bye, I am leaving."

P = Person () # creating an object

P.say_hi()
Person.say_bye(P)

