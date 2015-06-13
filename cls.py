# class Avenger:
# 	avengerscount=0

# 	def __init__(self, name, power):
# 		Avenger.avengerscount += 1
# 		self.name = name
# 		self.power = power

# 	def howmany():
# 	    print("total Avengers %d" % Avenger.avengerscount)

# 	def getname(self):
# 	    print("Avenger name:"+name+" have power"+power)


# hulk=Avenger("Hulk","Angryness")
# ironman=Avenger("ironman","suite")

# print("avengerscount: ",Avenger.avengerscount)    










class Avenger:
	avengerscount=0

	def __init__(self, name, power):
		self.avengerscount += 1
		self.name = name
		self.power = power

	def howmany():
	    print("total Avengers %d" % Avenger.avengerscount)

	def getname(self):
	    print("Avenger name:"+name+" have power"+power)


hulk=Avenger("Hulk","Angryness")
ironman=Avenger("ironman","suite")

print("avengerscount: ",hulk.avengerscount,ironman.avengerscount)    



# class Avenger:
# 	avengerscount=0

# 	def __init__(self, name, power):
# 		Avenger.avengerscount += 1
# 		self.name = name
# 		self.power = power

# 	def howmany():
# 	    print("total Avengers %d" % Avenger.avengerscount)

# 	def getname(self):
# 	    print("Avenger name:"+name+" have power"+power)


# hulk=Avenger("Hulk","Angryness")
# print(hulk.name)
# print(hulk.power)
# ironman=Avenger("ironman","suite")
# print(ironman.name)
# print(ironman.power)

# print("avengerscount: ",Avenger.avengerscount)   





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
del hulk.name   #we can delet also the attributes of object
print(hulk.name)