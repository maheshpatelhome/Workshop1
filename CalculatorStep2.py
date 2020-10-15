def doCalc(operator, int1, int2):
    if operator.upper() == "X":
        return (int1 * int2)
    elif operator == "+":
        return (int1 + int2)
    elif operator == "-":
        return (int1 - int2)
    elif operator == "/":
        return (int1 / int2)
    elif operator =="^":
        return pow(int1, int2)     

with open("calc.txt", "r") as f:
    lines = f.read().splitlines()

runningTotal = 0
for line in lines:
    calc, operator, int1, int2 = line.split()
    calculatedValue = doCalc(operator, int(int1), int(int2))
    runningTotal +=  calculatedValue
    
print (runningTotal)
    