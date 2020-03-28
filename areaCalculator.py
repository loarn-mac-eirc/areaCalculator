#area calculator

print('This is an area calculator')

def test_function(height, length, width):
	area = height * length * width
	return area

while True:
    print('Type Y to continue')
    ucontinue = input('>>').upper()
    if ucontinue == 'Y':
        user_height = (input('height:'))
        user_length = (input('length:'))
        user_width = (input('width:'))
        try:
            user_area = test_function(int(user_height),int( user_length),int(user_width))
            print('The area is %s' %user_area)
        except ValueError:
            print('OI! thats not a number!!')
    else:
	    break

print('game over')
 
