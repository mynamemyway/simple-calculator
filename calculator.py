num_1, num_2, op = int(input()), int(input()), input()
if op == "+":
    print(num_1 + num_2)
elif op == "-":
    print(num_1 - num_2)
elif op == "*":
    print(num_1 * num_2)
elif op == "/":
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print("На ноль делить нельзя!")
else:
    print("Неверная операция")
