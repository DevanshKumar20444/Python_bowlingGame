class BowlingGame:
    """A class to represent a game of 10-pin bowling."""

    def __init__(self):
        """Initialize a new game."""
        self.rolls = []

    def roll(self, pins):
        """Record a roll in the game.

        Args:
            pins (int): The number of pins knocked down in the roll.
        """
        self.rolls.append(pins)

    def score(self):
        """Calculate the score of the game.

        Returns:
            int: The total score of the game.
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """Check if a roll is a strike.

        Args:
            rollIndex (int): The index of the roll to check.

        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10

    # Other methods follow with appropriate docstrings
