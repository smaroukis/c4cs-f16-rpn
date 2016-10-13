import operator

def add(a,b):
	return a + b

def sub(a,b):
	return a - b

def mul(a,b):
	return a*b


operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,

}


def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
			raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		calculate(raw_input("rpn calc> ")) # use just 'input' for python3
 
if __name__=="__main__":
	main()	
