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


s = Stack()
n = int(input())
nprices = list(map(int,input().split()))
res = [-1] * n
for i in range(n):
    while not s.empty() and nprices[i] < nprices[s.top()]:
        res[s.top()] = i
        s.pop()
    s.push(i)
print(*res)