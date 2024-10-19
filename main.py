a = input("enter: ")

def main():
    b = a.split()
    if len(b) != 3 or b[1] not in ['+', '-', '*', '/']:
        return ("error, wrong input format")
    try:
        num1 = int(b[0])
        num2 = int(b[2])

        if num1 > 10 or num1 < 1 or num2 > 10 or num2 < 1:
            raise ValueError

    except Exception:
        return ("error, enter only numbers or nums > 10, < 1 !!!")

    if b[1] == "+":
        res = num1 + num2
    if b[1] == "-":
        res = num1 - num2
    if b[1] == "*":
        res = num1 * num2
    if b[1] == "/":
        res = num1 / num2
    print(res)

print(main())