def cardGameForTwo():
	N = int(input())
	a = list(map(int, input().split()))
	a.sort(reverse=True)
	diffPoint = 0 
	for index in range(0, N):
		if index % 2 == 0:
			diffPoint += a[index]
		else:
			diffPoint -= a[index]
	print(diffPoint)

cardGameForTwo()