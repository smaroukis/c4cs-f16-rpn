#!/Users/Spencer/Distributions_et_al/anaconda/envs/pandahacks/bin python

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		if token == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		elif token == '-':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 - arg2
			stack.append(result)
		elif token == '*':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 * arg2
			stack.append(result)	
		elif token == '/':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 / arg2
			stack.append(result)
		else:
			stack.append(int(token))
		print(stack)
	if len(stack) != 1:
			raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		calculate(raw_input("rpn calc> ")) # use just 'input' for python3
 
if __name__=="__main__":
	main()	
