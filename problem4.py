class MultipleCounter:
    def __init__(self, numbers):
        self.numbers = numbers
        self.divisors = list(range(1, 10))
    def count_multiples(self):
        result = {}
        for d in self.divisors:
            count = sum(1 for n in self.numbers if n % d == 0)
            result[d] = count
        return result
user_input = input("Enter the numbers: ")
nums = list(map(int, user_input.split()))
counter = MultipleCounter(nums)
print(counter.count_multiples())

