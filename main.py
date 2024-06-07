from stack import Stack

good_string1 = '(((([{}]))))'
good_string2 = '[([])((([[[]]])))]{()}'
good_string3 = '{{[()]}}'

bad_string1 = '}{}'
bad_string2 = '{{[(])]}}'
bad_string3 = '[[{())}]'

pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}

stack = Stack()

test_string = good_string2
balanced = True
# print(test_string)

for char in test_string:
    char_is_open = char == '(' or char == '[' or char == '{'
    char_is_close = char == ')' or char == ']' or char == '}'

    if char_is_open:
        stack.push(char)

    if char_is_close:
        if not stack.isEmpty():
            if pairs[stack.peek()] == char:
                stack.pop()
            else:
                balanced = False
        else:
            balanced = False
    print(stack.stack, balanced, char)

if not stack.isEmpty():
    balanced = False

print('balanced:', balanced)