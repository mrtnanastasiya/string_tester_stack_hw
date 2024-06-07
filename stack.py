class Stack:

    def __init__(self, initial_items:list=[]):
        self.stack = initial_items

    # Проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        return False if len(self.stack) > 0 else True

    # Добавляет новый элемент на вершину стека (в конец списка). Метод ничего не возвращает.
    def push(self, item:str):
        self.stack.append(item)

    # Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека.
    def pop(self):
        return self.stack.pop()

    # Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.stack[-1]

    # Возвращает количество элементов в стеке.
    def size(self):
        return len(self.stack)