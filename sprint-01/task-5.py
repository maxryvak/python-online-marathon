def toPostFixExpression(e):
    operator = ['+', '-', '*', '/', '%', '(', ')']
    parenthesis = ['(', ')']
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    res = []
    stack = []
    for i in e:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()
        elif i not in (operator + parenthesis):
            res.append(i)
        elif i in operator:
            while stack and stack[-1] != '(' and priority[i] <= priority[stack[-1]]:
                res.append(stack.pop())
            stack.append(i)
    while stack:
        res.append(stack.pop())
    return res
