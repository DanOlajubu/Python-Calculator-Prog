#Project 1 - Create a simple Calculator Program
#You need to have a way to input data into the program from the user input
#2 nums to be created (num1 & num2) and a choice (to be selected by user)
#Might be easier to create functions that we can call
#Think about using the IF, ELIF, & ELSE Statement
#Find out why else isn't executing

print("------------------------------------------------------------------")
# define functions

def add(x, y):  
   return x + y 
def subtract(x, y): 
   return x - y 
def multiply(x, y): 
   return x * y 
def divide(x, y): 
   return x / y
def exponent(x, y): 
   return x ** y


# take input from the user  
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")
print("5.Exponent")
  
choice = input("Enter any of the choices(1/2/3/4/5): ")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == "1":  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == "2":  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == "3":  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == "4":  
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == "5":  
   print(num1,"**",num2,"=", exponent(num1,num2))  
else: 
   print("Invalid input! something went wrong - make sure to use only numbers and symbols!")  
