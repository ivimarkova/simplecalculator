#Ivayla Markova, Simple Calculator, Paradigmen Task
import math

memory = 0
result = None
opr = None

def input_operation():
    global memory, result, opr
    while True:
        try:
            if result is None:
                num = float(input("Enter a number: "))
                result = num
            opr = input("Enter an operation (+, -, *, /, sqrt, recp, mc, mr, ms, m+, c, ce, =, exit): ")
            if opr in ["+", "-", "*", "/"]:
                if result is None:
                    print("Please enter a number first.")
                    continue
                num = float(input("Enter a number: "))
                if opr == "+":
                    result += num
                elif opr == "-":
                    result -= num
                elif opr == "*":
                    result *= num
                elif opr == "/":
                    if num == 0:
                        print("Cannot divide by zero.")
                        continue
                    result /= num
            elif opr == "sqrt":
                if result < 0:
                    print("Cannot take square root of a negative number.")
                    continue
                result = math.sqrt(result)
            elif opr == "recp":
                if result == 0:
                    print("Cannot take reciprocal of zero.")
                    continue
                result = 1 / result
            elif opr == "mc":
                memory = 0
            elif opr == "mr":
                if memory is not None:
                    result = memory
            elif opr == "ms":
                memory = result
            elif opr == "m+":
                memory += result
            elif opr == "c":
                result = None
                opr = None
            elif opr == "ce":
                result = None
            elif opr == "=":
                if result is None:
                    print("Please enter a number and an operation.")
                else:
                    if opr == "+":
                        result += num
                    elif opr == "-":
                        result -= num
                    elif opr == "*":
                        result *= num
                    elif opr == "/":
                        if num == 0:
                            print("Cannot divide by zero.")
                            continue
                        result /= num
                    memory = result
                    print("Result:", result)
                    result = None
                    opr = None
                    break
            elif opr == "exit":
                print("Exiting calculator...")
                exit()
            else:
                print("Please enter a valid operation.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

while True:
    input_operation()
    if memory != 0:
        print("Memory:", memory)
