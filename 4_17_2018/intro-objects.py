class Whip:
	"""Whip class represetns and manipulates x,y coordinates of cars."""

	def __init__(self,x=0,y=0,speed=0):
		"""Create a new car at the origin."""
		self.x = x
		self.y = y
		self.speed = speed

	def status(self):
		print self.x, self.y, self.speed

	def fuse(self,other):
		new_x =  self.x + other.x
		new_y =  self.y + other.y
		new_speed =  self.speed + other.speed
		return Whip(new_x,new_y,new_speed)

example = Whip(3,1,5)
example.status()

sample = Whip(2,4,9)
sample.status()

baby = example.fuse(sample)
baby.status()