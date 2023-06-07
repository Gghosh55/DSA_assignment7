def buildString(s):
    stack = []

    for c in s:
        if c != '#':
            stack.append(c)
        elif stack:
            stack.pop()

    return ''.join(stack)


def backspaceCompare(s, t):
    return buildString(s) == buildString(t)
s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))
