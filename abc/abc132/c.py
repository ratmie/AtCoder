# C - Divide the Problems
import math
def main():
	N = int(input())
	d = list(map(int,input().split()))
	d.sort()
	K = list(range(d[math.floor(N/2) - 1] + 1, d[math.floor(N/2)] + 1))
	print(len(K))

main()