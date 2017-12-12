import xml.sax

class Handler(xml.sax.handler.ContentHandler):
	def __init__(self):
		xml.sax.ContentHandler.__init__(self)
	
	def startElement(self, name, attrribute):
		self.CurrentData = name
		print("Start tag: ", str(name))
	
	def endElement(self, name):
		self.CurrentData=""
		print("End tag: ", str(name))

	def characters(self, data):
		if(self.CurrentData == "kolor"):
			print("KOLOR: ", str(data))
		elif(self.CurrentData == "nazwa"):
			print("MARKA: ", str(data))
handler = Handler()
xml.sax.parse("pars.xml", handler)
