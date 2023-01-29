class FibonacciCalculator:
    @staticmethod
    def calculate(index, cache=dict()):
        if index in cache:
            return cache[index]

        if index == 0 or index == 1:
            return 1
        
        cache[index - 2] = FibonacciCalculator.calculate(index - 2, cache)

        return FibonacciCalculator.calculate(index - 1, cache) + cache[index - 2]