class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.id_number = roll_no
        self.scores = []

    def add_score(self, score):
        """Add a student's score after validating it."""
        if score < 0:
            raise ValueError("Score cannot be negative")

        self.scores.append(score)
