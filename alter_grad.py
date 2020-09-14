import numpy as np

#SDG
class SDG():
	def __init__(self, lr=0.1):
		self.lr = lr
	def update(self, params, grads):
		for key in params.keys():
			params[key] -= self.lr*grads[key]

#Momentum
class Momentum():
	def __init__(self, lr=0.1, momentum=0.9):
		self.lr = lr
		self.momentum = momentum
		self.v = None
	def update(self, params, grads):
		if self.v is None:
			self.v = {}
			for key, val in params.items():
				self.v[key] = np.zeros_like(val)
		for key in params.keys():
			self.v[key] = self.momentum*self.v[key] - self.lr*grads[key]
			params[key] += self.v[key]

#Adagrad
class Adagrad():
	def __init__(self, lr=0.1):
		self.lr = lr
		self.h = None
	def update(self, params, grads):
		if self.h is None:
			self.h = {}
			for key, val in params.items():
				self.h[key] = np.zeros_like(val)
		for key in params.keys():
			self.h[key] += grads[key]*grads[key]
			params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key])+1e-7)
