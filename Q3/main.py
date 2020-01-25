import sys

operators = ["+", "-", "/", "*"]
mathThings = ["(", ")", operators]


def evalPos(num1, num2):
    print("plus")

def evalNeg(num1, num2):
    print("neg")

def evalDiv(num1, num2):
    print("div")

def evalMul(num1, num2):
    print("mul")

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

def evaluate( expression ):
    print(expression)
    for operator in operators:
        if operator in expression:
            applyOperator(operator, 1, 1)  
            return str(123.0)
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
