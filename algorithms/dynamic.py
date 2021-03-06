from algorithms.base import Results
from time import time
# import common_functions


class DynamicSolver:

    def __init__(self, weights, profits,  capacity):
        self.weights = weights
        self.profits = profits
        self.capacity = capacity

    def get_result_weight(self, indexes):
        weight = 0
        for i in range(len(self.profits)):
            if i in indexes:
                weight += self.weights[i]
        return weight

    def get_answers(self, indexes):
        answers = [0] * len(self.profits)
        for ind in indexes:
            answers[ind] = 1
        return answers

    def solve(self):
        result = Results()
        start_time = time()
        knapsack_values = [[0 for x in range(0, self.capacity + 1)] for y in range(0, len(self.profits) + 1)]
        for i in range(1, len(self.profits) + 1):
            current_weight = self.weights[i - 1]
            current_value = self.profits[i - 1]
            for c in range(0, self.capacity + 1):
                if current_weight > c:
                    knapsack_values[i][c] = knapsack_values[i - 1][c]
                else:
                    knapsack_values[i][c] = max(knapsack_values[i - 1][c],
                                                knapsack_values[i - 1][c - current_weight] + current_value)
        finish_time = time()
        result.time = round(finish_time - start_time, 4)
        indexes = self.get_knapsack_result_items(knapsack_values)
        result.weight = self.get_result_weight(indexes)
        result.answers = self.get_answers(indexes)
        result.profit = knapsack_values[-1][-1]

        return result

    def get_knapsack_result_items(self, knapsack_values):
        sequence = []
        i = len(knapsack_values) - 1
        c = len(knapsack_values[0]) - 1
        while i > 0:
            if knapsack_values[i][c] == knapsack_values[i - 1][c]:
                i -= 1
            else:
                sequence.append(i - 1)
                c -= self.weights[i - 1]
                i -= 1
            if c == 0:
                break
        return list(reversed(sequence))




