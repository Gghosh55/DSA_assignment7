def addStrings(num1, num2):
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    carry = 0
    result = ""

    while p1 >= 0 or p2 >= 0:
        digit1 = int(num1[p1]) if p1 >= 0 else 0
        digit2 = int(num2[p2]) if p2 >= 0 else 0

        digit_sum = digit1 + digit2 + carry
        carry = digit_sum // 10
        result += str(digit_sum % 10)

        p1 -= 1
        p2 -= 1

    if carry > 0:
        result += str(carry)

    return result[::-1]
num1 = "11"
num2 = "123"
print(addStrings(num1, num2))
