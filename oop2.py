class Animal :
	def __init__(self,name,age,color,size) :
		self.name=name
		self.age=age
		self.color=color
		self.size=size
	def print_all(self):
		print(self.name)
		print(self.age)
		print(self.color)
		print(self.size)
	def eat(self,food):
		print("the animal "+self.name+" is eating "+food)

	
	

unicorn=Animal("sadek",22,"yellow","tiny")
lion=Animal("lolla",15,"gray","huge")



lion.eat("pizza")
