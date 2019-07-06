def kagamiMochi():
	N = int(input())
	d = []
	for _ in range(0, N):
		d.append(int(input()))
	d.sort()
	count = 1
	for j in range(1, N):
		if d[j] != d[j-1]:
			count += 1
	print(count)

kagamiMochi()