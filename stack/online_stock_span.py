class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # Monotonic decreasing stack
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,span))
        print(self.stack)
        return span

        # Brute
        self.stack.append(price)
        ptr = len(self.stack)-1
        i = 0
        while self.stack[ptr] <= price and ptr >= 0:
            i+=1
            ptr -= 1
        return i