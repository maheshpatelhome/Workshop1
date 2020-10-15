def doCalc(operator, int1, int2):
    if operator.upper() == "X":
        return (int1 * int2)
    elif operator == "+":
        return (int1 + int2)
    elif operator == "-":
        return (int1 - int2)
    elif operator == "/":
        return (int1 / int2)

def processCommand(operation, lines):
    processed.append(line)
    ## check if command exists, if it does then return that number
    if (processed.index)

    if operation[1].upper() == "CALC":
        lineNumber = doCalc(operation[2], operation[3], operation[4])
    else:
        lineNumber = int(operation[1])
        
    newLine = lines[lineNumber]
    nextOperation = newLine.split()
    processCommand(nextOperation, lines)



with open("goto.txt", "r") as f:
    lines = f.read().splitlines()

processed = []
for line in lines:
    operation = line.split()
    processCommand(operation, lines)
