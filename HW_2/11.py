class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack)

    def push(self, x):
        """Добавляет в стек число x.
        Возвращает 'ok'.
        """
        self.stack.append(x)
        return 'ok'

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.stack)

    def clear(self):
        """Очищает стек и вывод ok.
        """
        self.stack = []
        return "ok"

    def back(self):
        """Возвращает значение последнего элемента, 
        не удаляя его из стека.
        """
        if self.empty() == 0:
            return "error"
        return self.stack[-1]

    def pop(self):
        """Удаляет из стека последний элемент.
        Возвращает значение этого элемента.
        """
        if self.empty() == 0 :
            return "error"
        last = self.stack[-1]
        self.stack = self.stack[:-1]
        return last


s = Stack()
string = input().split()

while string[0] != "exit":
    if len(string) == 1:
        if string[0] == "size":
            print(s.size())
        elif string[0] == "back":
            print(s.back())
        elif string[0] == "pop":
            print(s.pop())
        elif string[0] == "clear":
            print(s.clear())
    else:
        if string[0] == "push":
            print(s.push(string[1]))
    string = input().split()
else:
    print("bye")