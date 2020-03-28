print('this is an area calculator')
print('type stop, to stop'
)
def test_function(height, length, width):
	area = height * length * width
	return area

while True:
	print('Type Y to continue')
	ucontinue = input('>>').upper()
	if ucontinue == 'Y':
		user_height = int(input('height:'))
		user_length = int(input('length:'))
		user_width =int(input('width:'))
		user_area = test_function(user_height, user_length, user_width)
		print('The area is %s' % user_area)
	else:
		break
print('game over')
 
