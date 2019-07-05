def placingMarbles():
	s = map(int,list(input()))
	count = 0
	for i in s:
		if i == 1:
			count += 1
	print(count)

placingMarbles()