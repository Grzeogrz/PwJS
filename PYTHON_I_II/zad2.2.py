import math

class Complex(object):
	def __init__(complex, r, i):
		complex.real=r
		complex.imag=i

	def __add__(complex, c2):
		re=complex.real+c2.real
		im=complex.imag+c2.imag
		return Complex( re, im)

	def __sub__(complex, c2):
		re=complex.real-c2.real
		im=complex.imag-c2.imag
		return Complex(re, im)
	
	def __mul__(complex, c2):
		re=complex.real * c2.real - complex.imag*c2.imag
		im=complex.imag * c2.real + complex.real*c2.imag
		return Complex(re, im)
	def __abs__(complex):
		return math.sqrt(complex.real**2 + complex.imag**2)

	def __conj__(complex):
		return Complex(complex.real, -complex.imag)	

	def __neg__(complex):
		return Complex(-complex.real, -complex.imag)

	def print(complex):
		print(complex.real," + ", complex.imag, "j")
x=Complex(2,4)
y=Complex(2,3)
z=Complex(1,1)
z=x+y
a=z.__mul__(y)
(-z).print()
