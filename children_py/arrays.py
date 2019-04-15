# Generates a list of numbers
# print(list(range(10, 20)))

for x in range(0, 5):
	print('You number is %s' % (x + 1))


x = 45
y = 80

while x < 50 and y < 100:
	x = x + 1
	y = y + 1
	print(x, y)