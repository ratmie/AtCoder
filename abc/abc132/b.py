# B - Ordinary Number

def main():
	n = int(input())
	p = list(map(int,input().split()))
	count = 0
	for i in range(1, n-1):
		if check(p, i):
			count += 1
	print(count)

def check(p, i):
	if ((p[i -1] < p[i]) and (p[i] < p[i + 1])) or ((p[i -1] > p[i]) and (p[i] > p[i + 1])):
		return True
	else:
		return False

main()