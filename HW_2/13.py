class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        return self.stack.append(x)

    def top(self):
        return self.stack[-1]

    def pop(self):
        self.stack.pop() 

operandStack = Stack() #  Создаём пустой стек под названием operandStack.
string = input().split() #  Преобразовываем строку в список, используя строковый метод split
for i in string: #  Сканируем список токенов слева направо
    if i in ["+", "-", "*"]: #  Если токен является оператором *, /, + или -, то он нуждается в двух операндах. Производим выталкивание из operandStack дважды. Сначала вытолкнется второй операнд, а затем - первый. Выполняем арифметическую операцию и помещаем результат обратно в operandStack.
        a = operandStack.top() 
        operandStack.pop()
        b = operandStack.top()
        operandStack.pop()
        if i == "+":
            operandStack.push(b+a)
        elif i == "-":
            operandStack.push(b-a)
        elif i == "*":
            operandStack.push(b*a)
    else: # Если токен является операндом, то преобразовываем его из строки в целое число и помещаем значение в operandStack.
        operandStack.push(int(i))
print(operandStack.top())  # Когда входное выражение полностью обработано, его результат находится в стеке. Выталкиваем его из operandStack и возвращаем в качестве ответа.

