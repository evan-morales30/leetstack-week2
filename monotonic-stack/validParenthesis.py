def validParenthesis(s):
    stack = []
    pairs = {")" : "(", "}" : "{", "]" : "["}
    for par in s:
        if par in "([{":
            stack.append(par)
        elif not stack or stack.pop() != pairs[par]:
            return False

    return not stack



print("Should return True: ", validParenthesis("()[]{[]}"))
print("Should return False: ", validParenthesis("(]"))
print("Should return False: ", validParenthesis("{[()]"))
print("Should return True: ", validParenthesis("({[]})"))
