def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    s_concat = s + s

    if goal in s_concat:
        return True

    return False
s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))