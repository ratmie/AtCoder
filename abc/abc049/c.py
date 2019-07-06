def daydream():
	S = input()
	flag = False
	while True:
		if len(S) == 0:
			flag = True
			break
		elif S.endswith('dreamer'):
			S = S[:-7]
		elif S.endswith('dream'):
			S = S[:-5]
		elif S.endswith('eraser'):
			S = S[:-6]
		elif S.endswith('erase'):
			S = S[:-5]
		else:
			break
	if flag:
		print('YES')
	else:
		print('NO')

daydream()