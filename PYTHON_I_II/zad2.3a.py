import xml.dom.minidom

DOM = xml.dom.minidom.parse("pars.xml")

print(DOM.toxml())

nodes = DOM.childNodes

for i in nodes[0].getElementsByTagName("auto"):
	print("Nazwa taga: ", i.getElementsByTagName("nazwa")[0].nodeName)
	
	print("Wartość taga: ", i.getElementsByTagName("nazwa")[0].childNodes[0].toxml())

	print("Wartość atrybutu: ", i.getElementsByTagName("nazwa")[0].getAttribute("foo"))
