import os

class BudgetGovernor:
    def __init__(self, max_allowed_cost: float = 0.50):
        self.max_cost = max_allowed_cost

    def evaluate_cost(self, estimated_cost: float) -> bool:
        if estimated_cost > self.max_cost:
            raise ValueError(f"Estimated cost ${estimated_cost} exceeds safety limit of ${self.max_cost}")
        return True
