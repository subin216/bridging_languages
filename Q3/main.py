import sys
import subprocess

operators = ["+", "/", "*", "-"]
mathThings = ["(", ")", operators]

def evalPos(num1, num2):
    command = "/code/Q3/add " + str(num1) + " " + str(num2)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

def evalNeg(num1, num2):
    command = "/code/Q3/sub " + str(num1) + " " + str(num2)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

def evalDiv(num1, num2):
    command = "/code/Q3/div " + str(num1) + " " + str(num2)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

def evalMul(num1, num2):
    command = "/code/Q3/mul " + str(num1) + " " + str(num2)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

def applyOperator(operator, num1, num2):
    switcher = {
        "+": evalPos,
        "-": evalNeg,
        "/": evalDiv,
        "*": evalMul
    }
    func = switcher.get(operator, lambda: "Invalid operator")
    return func(num1, num2)

def dumpReplace(equation):
    mathThings = ["(", ")", "+", "-", "/", "*"]
    for mathThing in mathThings:
        equation = equation.replace(mathThing, " " + mathThing + " ")
    return equation

def remove_at(i, s):
    return s[:i] + s[i+1:]

def evaluate( expression ):
    num1Neg = False
    num2Neg = False

    if expression[0] == "-":
        expression = remove_at(0, expression)
        num1Neg = True
    firstOperator = -1
    for operator in operators:
        firstOperator = expression.find(operator)
        if firstOperator >= 0:
            break
    if firstOperator >= 0:
        if expression[firstOperator+1] == "-":
            expression = remove_at(firstOperator+1, expression)
            num2Neg = True    

    for operator in operators:
        if operator in expression:
            expression = expression.split(operator)
            if num1Neg:
                expression[0] = float(expression[0]) * -1.0
            if num2Neg:
                expression[1] = float(expression[1]) * -1.0
            output = applyOperator(operator, float(expression[0]), float(expression[1]))  
            return output
    return expression

### MAIN ###

if len(sys.argv) != 2:
    print("Make better input pls")
    sys.exit()

f = open(str(sys.argv[1]), "r")
equation = f.readline()
equation = dumpReplace(equation).split()

stack = []
result = 0.0
for item in equation:
    if item == "(":
        stack.append(item)
    elif item == ")":
        current = stack.pop()
        result = evaluate(current.replace("(", ""))
        if (len(stack) > 0):
            stack[-1] = stack[-1] + result
    else:
        if (len(stack) > 0):
            stack[-1] = stack[-1] + item
        else:
            print("Input equation should start with a ( character")

sys.stdout.write( result + "\n" )
