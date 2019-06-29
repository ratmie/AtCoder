def main():
	buttons = list(map(int, input().split()))
	aa = buttons[0] + (buttons[0] - 1)
	ab = buttons[0] + buttons[1]
	bb = buttons[1] + (buttons[1] - 1)
	print(max(aa, ab, bb))

main()


