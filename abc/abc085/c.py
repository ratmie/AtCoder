def otoshidama():
	N, Y = map(int, input().split())
	a = b = c = -1
	for ai in range(0, N + 1):
		for bi in range(0, N + 1 - ai):
			if 10000 * ai + 5000 * bi + 1000 * (N - ai -bi) == Y:
				a = ai
				b = bi
				c = N - ai - bi
				break
		else:
			continue
		break
	print("{0} {1} {2}".format(a,b,c))

otoshidama()