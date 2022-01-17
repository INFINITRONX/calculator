def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

# take input from the user
print("DARK CYBER WEAPON CALCULATOR")
print("  ____    _    _     ____ _   _ _        _  _____ ___  ____")
print(" / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \ ")
print("| |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) |")
print("| |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ < ")
print(" \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_\ ")
print("                                       ")
print("                                        ")
print("DARK CYBER WEAPON CALCULATOR..###ASANKA###")
print("                    ")
print("                      ")
print("DON'T COPY THIS SCRIPT..   I'M DARK CYBER WEAPON")
print("              ")
print("            ")
print("SELECT YOUR OPERATION.")
print(" ")
print("1.Add")
print(" ")
print("2.Subtract")
print(" ")
print("3.Multiply")
print(" ")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
