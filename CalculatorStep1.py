operator = input("Please Enter operator (X, +, -, /) ")
int1 = int(input("Please enter integer 1 "))
int2 = int(input("Please enter integer 2 "))

if operator.upper() == "X":
    print (int1 * int2)
elif operator == "+":
    print (int1 + int2)
elif operator == "-":
    print (int1 - int2)
elif operator == "/":
    print (int1 / int2)