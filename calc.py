#Pick what operation you want to use and the number you want to calculate
operator = input("Enter an operator (+ - * /): ")
num1 = float (input("Enter 1st Number: ")) #Float command makes it so they are  type casted into another data type.
num2 = float(input("Enter 2nd Number: "))


#This is how to make it so the numbers are rounded up when calculated with round .
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
    
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
    
elif operator == "*":
    result = num1 * num2
    print(round(result,3 ))
    
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
    
else:
    print(f"{operator} is not a valid operator to use.")
