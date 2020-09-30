import random

class Stack:
	
	def __init__(self,size=0,low=0.0,high=1.0,fx = float):
		self.array = []
		self.fill(size,low,high,fx)
		

	def pop(self):
		if (len(self.array) != 0):
			return self.array.pop( len(self) - 1 )
		else:
			return None

	def peek(self):
		if (len(self.array) !=0 ):
			return self.array[-1]
		else:
			return None

	def push(self,data):
		self.array.append(data)

	def __repr__(self):
		repr_str = ''
		for item in self.array[::-1]:
			repr_str += '{},'.format(item)
		return repr_str
	
	def print(self):
		for item in self.array[::-1]:
			print(item)

	def fill(self,size,low=0.0,high=1.0,fx=float):
		if (size==0):
			return None
		for i in range(0,size):
			self.push(fx(random.uniform(low,high)))


	def __len__(self):
		return len(self.array)

