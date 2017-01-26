

def fizzBuzz(number):
	toReturn = ""
	if number % 3 == 0:
		toReturn+="Fizz"
	if number % 5 == 0:
		toReturn+="Buzz"
	if len(toReturn) is 0:
		toReturn = number
	
	return toReturn


def allFizzBuzz():
	for i in range(1,101):
		print fizzBuzz(i)

allFizzBuzz()
