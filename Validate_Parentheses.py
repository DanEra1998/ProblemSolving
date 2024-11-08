stack = []
# always key to value
closetoOpen = {
    ")":"(",
    "}":"{",
    "]":"["
}
def validParenthesis():
    for c in s:
        if stack and c in closetoOpen:
            if stack[-1] == closetoOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
