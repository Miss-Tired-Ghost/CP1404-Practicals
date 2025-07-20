"""
Time Estimate: 30 min
Work Time
"""


class Project:
    def __init__(self, name, start, priority, estimate, completion):
        self.name = name
        self.start = start
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def update(self, new_completion):
        self.completion = new_completion

    def __repr__(self):
        return f"{self.name}, start: {self.start}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"
