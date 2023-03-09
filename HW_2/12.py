class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, x):
        return self.stack.append(x)

    def pop(self):
        self.stack.pop()


seq = input()
s = Stack()
valid_seq = True
brackets = {'(':')', '[':']', '{':'}'}
for el in seq:
    if el in brackets:
        s.push(el)
    elif not s.empty() and el == brackets[s.top()]:
        s.pop()
    else:
        valid_seq = False
        break
print('yes') if s.empty() and valid_seq else print('no')
