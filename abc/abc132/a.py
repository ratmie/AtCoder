# A - Fifty-Fifty

def a():
	"""
	Examples
	>>> a() 
	>>> ASKA
	Yes
	"""
	S = input()
	isFF = checkFF(S)
	if isFF:
		print('Yes')
	else:
		print('No')

def checkFF(s):
	if len(s) != 4:
		return False
	if (s[0] == s[1]) and (s[2] == s[3]) and (s[0] != s[2]): 
		return True
	elif (s[0] == s[2]) and (s[1] == s[3]) and (s[0] != s[1]):
		return True
	elif (s[0] == s[3]) and (s[1] == s[2]) and (s[0] != s[1]):
		return True
	else:
		return False

if __name__ == '__main__':
    a()
	
	
