print("1. addition")        
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("choose an operation:")

operation =float(input("choose an operation:"))
if (operation  <1 or operation > 4):
    print("invalid operation")
    exit()
if (operation >= 1 and operation <= 4): 
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    if (operation == 1):
        print(num1 + num2)
    elif (operation == 2):
        print(num1 - num2)
    elif (operation == 3):
        print(num1 * num2)
    elif (operation == 4):
        if (num2 != 0):
         print(num1 / num2)
        else:
         print("division by zero is not allowed")
else:    
 print("invalid operation") 
 

