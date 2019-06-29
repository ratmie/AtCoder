def main():
	N = int(input())
	HeightList = list(map(int, input().split()))

	numOfOceanView = 1
	max = HeightList[0] # 0origin
	for i in range(1, N):
		if max < HeightList[i]:
			max = HeightList[i]
			numOfOceanView += 1
	print(numOfOceanView)

main()