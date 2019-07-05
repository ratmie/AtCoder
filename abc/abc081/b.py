def shiftOnly():
	n = int(input())
	A = list(map(int,input().split()))
	count = 0
	while True:
		for a in A:
			flag = True
			if a % 2 != 0:
				flag = False
				break
		if flag:
			count += 1
			A = [a/2 for a in A]
		else:
			break
	print(count)

shiftOnly()
#線形探索でもできる？