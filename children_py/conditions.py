car = 0
spaces = ' ' * 25

if car > 80:
	print('Good collection')
elif car < 80 and car > 0:
	print('You don\'t have enough cars')
	if car == 10:
		message = ('%s I gues, you have %s')
		print(message % (spaces, car))
else:
	print('So cool having a car')
