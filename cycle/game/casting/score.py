from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = []
        self.points[0] = 0
        self.points[1] = 0
        self.add_points(0, 0)
        self.add_points(0, 1)


    def add_points(self, points, cycle_index):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points[cycle_index] += points
        for i in range(len(self._points)):
            self.set_text(f"Player 1 Score: {self._points[0]}          Player 2 Score: {self._points[1]}")
            