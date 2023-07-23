"""
Estimated time taken: 220 minutes
Actual time taken: ~300 minutes
"""
import datetime


class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def is_urgent(self):
        return self.priority <= 3

    def is_completed(self):
        return self.completion == 100
