
# class Fantastic4:
# 	fantasticcount=0

# 	def __init__(self, name, power):
# 		Fantastic4.fantasticcount += 1
# 		self.name = name
# 		self.power = power

# 	def howmany():
# 	    print("total Fantastic %d" % Fantastic4.fantasticcount)

# 	def getname(self):
# 	    print("Fantastic name:"+self.name+" have power "+self.power)


# richard=Fantastic4("Richard","melting")
# print(richard.name)
# print(richard.power)
# richard.getname()
# Fantastic4.howmany()
# print("++++++++++++++++++++")
# ivan=Fantastic4("Ivan","fire in built")
# ivan.getname()
# Fantastic4.howmany()
# print(ivan.name)
# print(ivan.power)
# print("___________________________")

# print("fantasticcount: ",Fantastic4.fantasticcount)  





class Avenger:
	avengerscount=0

	def __init__(self, name, power):
		Avenger.avengerscount += 1
		self.name = name
		self.power = power

	def howmany():
	    print("total Avengers %d" % Avenger.avengerscount)

	def getname(self):
	    print("Avenger name:"+self.name+" have power "+self.power)


hulk=Avenger("Hulk","Angryness")
print(hulk.name)
print(hulk.power)
hulk.getname()
Avenger.howmany()
print("++++++++++++++++++++")
ironman=Avenger("ironman","suite")
ironman.getname()
Avenger.howmany()
print(ironman.name)
print(ironman.power)
print("___________________________")

print("avengerscount: ",Avenger.avengerscount)  
hulk.size="very big"
print("very big")

print(getattr(hulk,"name"))
setattr(hulk,"name","Bada hulk")
print(getattr(hulk,"name"))

