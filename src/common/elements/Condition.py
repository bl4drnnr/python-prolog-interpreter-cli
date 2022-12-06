class Condition:
    def __init__(self, left_side, separator, right_side):
        self.type = "condition"
        self.right_side = right_side
        self.separator = separator
        self.left_side = left_side

    def __str__(self):
        return f"Condition - separator: {self.separator}, left side: {self.left_side}, right side: {self.right_side}"
