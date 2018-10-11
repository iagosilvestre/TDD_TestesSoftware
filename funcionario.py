class Funcionario(object):
	def __init__(self, nome):
		self.nome = nome

	def __del__(self):
		return 1

