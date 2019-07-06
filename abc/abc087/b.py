def coins():
	a = int(input())
	b = int(input())
	c = int(input())
	x = int(input())
	count = 0
	for ai in range(0, a + 1):
		for bi in range(0, b + 1):
			for ci in range(0, c + 1):
				if (500 * ai + 100 * bi + 50 * ci) == x:
					count += 1
	print(count)

coins()
