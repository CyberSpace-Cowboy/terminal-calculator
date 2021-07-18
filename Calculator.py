#Python Terminal Calculator

print("				   Basic Terminal Calculator")
menu = """						Menu:
			To add: +
			To subtract: -
			To multiply: *
			To devide: /
			To raise to the power: ^

			To exit the program type: stop/exit + [Enter] 
"""

print(menu)

def Calculate():
	while(True):
		oper = input("Type in the operation: ")

		#To exit the program
		if "stop" in oper or "exit" in oper:
			exit()
		

		#Implementing Basic Operations: add, subtract, multiply, devide 
		if "+" in oper:
			upd1 = oper.split("+")
			res = int(upd1[0]) + int(upd1[1])
		elif "-" in oper:
			upd1 = oper.split("-")
			res = int(upd1[0]) - int(upd1[1])
		elif "*" in oper:
			upd1 = oper.split("*")
			res = int(upd1[0]) * int(upd1[1])
		elif "/" in oper:
			upd1 = oper.split("/")
			res = int(upd1[0]) / int(upd1[1])
		#Implementing More Advanced Operations e.g. Exponentiation
		elif "^" in oper:
			upd1 = oper.split("^")
			res = int(upd1[0]) ** int(upd1[1])

		print(res)


if __name__ == '__main__':
      
    # main method for executing
    # the functions
    Calculate()