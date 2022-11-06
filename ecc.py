def pow_mod(base, pwr, mod):
	res = 1
	pwr %= mod - 1
	t = base % mod
	while pwr > 0:
		if pwr & 1:
			res = (res * t) % mod

		t = (t * t) % mod
		pwr >>= 1

	return res


def inverse_mod(x, p):
	return pow_mod(x, p - 2, p)


class EllipticCurve:
	def __init__(self, a, b, p):
		# p > 3, p is prime
		self.p = p
		if (4*a**3 + 27*b**2) % self.p != 0:
			self.a = a
			self.b = b
		else:
			self.a = 1
			self.b = 0
		
		self.points_list = self.generate_points()
	
	def __contains__(self, p):
		x, y = p
		return (y**2) % self.p == self.apply(x)

	def apply(self, x):
		return (x**3 + self.a * x + self.b) % self.p

	def point_add(self, p1, p2):
		x1, y1 = p1
		x2, y2 = p2
		if p1 != p2:
			_lambda = ((y2 - y1) * inverse_mod(x2 - x1, self.p)) % self.p
		else:
			_lambda = ((3 * x1 ** 2 + self.a) * inverse_mod(2 * y1, self.p)) % self.p

		x = (_lambda ** 2 - x1 - x2) % self.p
		y = (_lambda * (x1 - x) - y1) % self.p
		return x, y

	def get_points_list(self):
		return self.points_list

	def generate_points(self):
		result = []
		sqrt_mod = {}
		
		for y in range(1, self.p // 2 + 1):
			sqrt_mod[(y ** 2) % self.p] = y
		for x in range(0, self.p):
			rhs = self.apply(x)
			if rhs in sqrt_mod:
				y = sqrt_mod[rhs]
				arr_x.append((x, y ))
				arr_y.append((x, self.p - y))
				result=arr_y+arr_x
				
		return result
	
	def __len__(self):
		return len(self.points_list) + 1


if __name__ == "__main__":	
	a=-2
	b=3
	arr_x=[]
	arr_y=[]
	ecc = EllipticCurve(a, b, 137)
	print(len(ecc))  # p = 2579 -> len = 2557 is a prime
	print ("1 O(Vô cực)")
	for i in range(0, len(ecc)):
		print(2*i+2, arr_x[i])
		print(2*i+3,arr_y[i])

	

	