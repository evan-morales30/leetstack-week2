class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            raise IndexError("getMin from empty stack")
        return self.min_stack[-1]


min_Stack = MinStack()

min_Stack.push(5)
print(f"push: {'correct' if min_Stack.stack == [5] and min_Stack.min_stack == [5] else 'incorrect'}")

min_Stack.push(2)
print(f"push: {'correct' if min_Stack.getMin() == 2 else 'incorrect'}")

min_Stack.push(7)
print(f"top: {'correct' if min_Stack.top() == 7 else 'incorrect'}")

min_Stack.push(1)
print(f"getMin: {'correct' if min_Stack.getMin() == 1 else 'incorrect'}")

min_Stack.pop()
print(f"pop: {'correct' if min_Stack.top() == 7 and min_Stack.getMin() == 2 else 'incorrect'}")
