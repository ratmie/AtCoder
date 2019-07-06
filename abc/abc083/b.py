def someSums():
	n, a, b = map(int, input().split())
	count = 0
	for i in range(1, n + 1):
		sum = 0
		n = i
		while True:
			sum += n % 10
			if n >= 10:
				n = n // 10
			else:
				break
		if a <= sum and sum <= b:
			count += i
	print(count)

someSums()