import random

class TebakAngka:
	def  _init_(self):
		self.tebakan = 0
		self.jawaban = random.randint(1,10)
		
	def cek(self):
		if self.jawaban  == self.tebakan:
			return True
			return  False