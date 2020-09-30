import random

class Queue:

	def __init__(self):
		self.array = []
		self.front = 0
		self.back = 0

	def enqueue(self,data):
		self.back += 1
		self.array.insert(self.back,data)

	def dequeue(self):
		if (len(self.array) == 0):
			return None
		else:
			to_ret = self.array[self.front]
			self.back -= 1
			del self.array[self.front]
			return to_ret

	def __repr__(self):
		ret_str = ''
		for i in range(self.front,self.back):
			ret_str += '{},'.format(self.array[i])
		return ret_str


	def __len__(self):
		return len(self.array)

	def print(self):
		for i in range(self.front,self.back):
			print(self.array[i])

	def populate(self,size,low=0.0,high=1.0,fx=float):
		for i in range(0,size):
			self.enqueue(fx(random.uniform(low,high)))
		

	def peek(self):
		return self.array[self.front]



