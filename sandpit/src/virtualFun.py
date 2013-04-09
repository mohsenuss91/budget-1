class Base:
	def __init__(self):
		pass
		
	def fun(self):
		self.fun2()
		
	def fun2(self):
		print 'Base fun2'
		
class Derivered(Base):
	def __init__(self):
		Base.__init__(self)
		pass
		
	def fun2(self):
		print 'wow Derivered fun2'


dupa = Derivered()
dupa.fun()
