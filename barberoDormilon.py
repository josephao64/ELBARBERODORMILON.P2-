#joseph isaac asencio ortiz 
from threading import Thread, Lock, Event
import time, random

mutex = Lock()# creamos la bariable mutex con la clase lock para que no se pueda acceder a la barberia mientras se esta cortando el pelo .

# almacenamos los Intervalos en segundos en estas variables
customerIntervalMin = 1
customerIntervalMax = 2
haircutDurationMin = 1
haircutDurationMax = 2

class BarberShop:
	waitingCustomers = []

	def __init__(self, barber, numerodebarberos):  #definimos las funciones y variables
		self.barber = barber
		self.numerodebarberos = numerodebarberos
		print ('barbería iniciada con {0} barbero'.format(numerodebarberos))
		print ('Mínimo intervalo de Clientes {0}'.format(customerIntervalMin))
		print ('Máximo intervalo de Clientes {0}'.format(customerIntervalMax))
		print ('Tiempo mínimo de corte de pelo {0}'.format(haircutDurationMin))
		print ('Tiempo máximo de corte de pelo {0}'.format(customerIntervalMax))
		print ('---------------------------------------')

	def openShop(self):
		print ('>>>>> La barbería está abierta<<<<< ')
		workingThread = Thread(target = self.barberGoToWork)#declaramos un hilo para que el barbero trabaje
		workingThread.start()#iniciamos el hilo del barbero

	def barberGoToWork(self):
		while True:
			mutex.acquire()#bloqueamos hasta que suceda el release

			if len(self.waitingCustomers) > 0:
				c = self.waitingCustomers[0]#cogemos al primer cliente y lo eliminamos de la lista
				del self.waitingCustomers[0]
				mutex.release()
				self.barber.cutHair(c)#hacemos que el barbero le corte el pelo al cliente escogido
			else:
				mutex.release()
				print ('ya termine me voy dormir ZzzzzZ')
				barber.sleep()
				print ('El barbero se desperto')

	def enterBarberShop(self, customer):
		mutex.acquire()
		print ('>> {0} entró a la barbería'.format(customer.name))

		if len(self.waitingCustomers) == self.numerodebarberos:
			print ('La sala de espera está llena, {0} se va a marchar.'.format(customer.name))
			mutex.release()
		else:
			print ('{0} se ha sentado en la sala de espera'.format(customer.name))
			self.waitingCustomers.append(c)
			mutex.release()
			barber.wakeUp()#Despertamos al barbero

class Customer:
	def __init__(self, name):
		self.name = name#Creamos un Cliente que solo necesita su nombre

class Barber:
	barberWorkingEvent = Event()#El barbero se crea un evento que es cuando está trabajando

	def sleep(self):
		self.barberWorkingEvent.wait()#Definimos que si se duerme entonces el evento se para

	def wakeUp(self):
		self.barberWorkingEvent.set()#Definimos que si se despierta entonces el evento se activa

	def cutHair(self, customer):
		#Set barber as busy
		self.barberWorkingEvent.clear()#Se limpia el evento

		print ('A {0} le están cortando el pelo'.format(customer.name))

		randomHairCuttingTime = random.randrange(haircutDurationMin, haircutDurationMax+1)
		time.sleep(randomHairCuttingTime)#ponemos un tiempo aleatorio que tardará en cortar el pelo
		print ('{0} ha terminado'.format(customer.name))


if __name__ == '__main__':                      #creamos un bloque en esta var para que se ejecute cuando sea llamado  aqui almacenamoslas las funciones y clases de los nombres de los clientes 
	customers = []
	customers.append(Customer('angel'))
	customers.append(Customer('isaac'))
	customers.append(Customer('Marío'))
	customers.append(Customer('Alex'))
	customers.append(Customer('Andres'))
	customers.append(Customer('pablo'))


	barber = Barber()

	barberShop = BarberShop(barber, numerodebarberos=1)
	barberShop.openShop()

	while len(customers) > 0:
		c = customers.pop()#agaramos  un cliente y lo eliminamos de la lista


		#cuando un cliente nuevo entra en la barberia 
		barberShop.enterBarberShop(c)#el cliente c entra a la barbería
		customerInterval = random.randrange(customerIntervalMin,customerIntervalMax+1)
		time.sleep(customerInterval)
print(">>>>> La barbería está cerrada <<<<<")
