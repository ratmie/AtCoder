def traveling():
	N = int(input())
	t = [0] * (N + 1)
	x = [0] * (N + 1)
	y = [0] * (N + 1)
	for i in range(1, N + 1):
		t[i], x[i], y[i] = map(int, input().split())
	
	flag = True
	for i in range(1, N + 1):
		dt = t[i] - t[i - 1]
		dist = abs(x[i] - x[i - 1]) + abs(y[i] - y[i - 1])
		if dist > dt:
			flag = False
		if dist % 2 != dt % 2:
			flag = False
		
	
	if flag:
		print('Yes')
	else:
		print('No')

traveling()