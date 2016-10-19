class Tiburio(object):
	def __init__(self,ch_totales, precio_entrada=200):
		self.precio_entrada=precio_entrada
		self.mayoria_edad=10
		self.chicas_totales=ch_totales

	def getMorra(self,cantidad=1):
		print("Mesa que mas aplauda! ahi te va!",cantidad)

class Morra(object):
	def __init__(self, edad=18, altura=1.70,nacion="Mexicana"):
		self.edad=edad
		self.altura=altura
		self.nacionanlidad=nacion
		self.ganacias=0

	def getPrivado(self):
		print("asi papi?")
		self.setPropina()

	def setPropina(self,cantidad=100):
		self.ganacias+=cantidad		
										