"""
Time Estimate: 30 min
Work Time: 10 min
Code by: Miss Ghost/April First
"""

import datetime


class Project:
    def __init__(self, name, start: datetime, priority, estimate, completion):
        self.name = name
        self.start = start
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __repr__(self):
        return (f"{self.name}, "
                f"start: {self.start}, "
                f"priority {self.priority}, "
                f"estimate: ${self.estimate:.2f}, "
                f"completion: {self.completion}%".replace("-", "/"))

    def update(self, new_completion, new_priority):
        if new_completion:  # runs when not empty
            self.completion = new_completion
        if new_priority:  # runs when not empty
            self.priority = new_priority
