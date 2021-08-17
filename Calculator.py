#Python Terminal Calculator
import shutil
columns = shutil.get_terminal_size().columns

print("\n" + "BASIC TERMINAL CALCULATOR".center(columns) + "\n")

print("To add: +".center(columns))
print("To subtract: -".center(columns))
print("To multiply: *".center(columns))
print("To devide: /".center(columns))
print("To raise to the power: ^".center(columns) + "\n")


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