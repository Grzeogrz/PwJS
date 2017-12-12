import math
print("Podaj wspolczynniki rowania kwadratowego")
a=int(input("a="))
print(type(a))
b=int(input("b="))
c=int(input("c="))
print("Rownanie y=",a,"x^2+",b,"x+",c)

delta = b*b - 4*a*c

if delta == 0:
	print("Pierwiastek rownania:")
	print("x=",-b/(2*a))
elif delta > 0:
	print("Pierwsiatki rownania:")
	print("x1=",(-b-math.sqrt(b*b - 4*a*c))/(2*a))
	print("x2=",(-b+math.sqrt(b*b - 4*a*c))/(2*a))
else:
	print("Rownanie nie ma pierwiastkow rzeczywistych")
