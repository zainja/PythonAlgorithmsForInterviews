from stack import Stack


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ''
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str


print(reverse_string(Stack(), 'Hello'))
