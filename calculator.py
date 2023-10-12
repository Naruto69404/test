num = int(input("give me a number: "))
num2 = int(input("give me a second number: "))
operation = input("what do you want to do with this: ")

if operation == "+":
    plus = num + num2
    print(plus)
elif operation == "-":
    minus = num - num2
    print(minus)
elif operation == "*":
    multiply = num * num2
    print(multiply)
elif operation == "/":
    divide = num / num2
    print(divide)
else:
    print("idk what do you want to do")
