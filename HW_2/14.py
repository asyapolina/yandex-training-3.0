class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        return self.stack.append(x)

    def empty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[-1]

    def pop(self):
        self.stack.pop()


seq = Stack()
count = 0
N = int(input())
nums = list(map(int, input().split()))
for el in nums:
    seq.push(el)
    while not seq.empty() and seq.top() == count + 1:
        count += 1
        seq.pop()
if not seq.empty() or count != N:
    print('NO')
else:
    print('YES')

