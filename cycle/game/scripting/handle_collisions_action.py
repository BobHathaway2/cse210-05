from pickle import FALSE
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
    
        if not self._is_game_over:
            # self._handle_food_collision(cast)
            self._handle_cycle_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_cycle_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        head = []
        segments = []
        cycles = cast.get_actors("cycles")
        for i in range(len(cycles)):
            head.append(cycles[i].get_segments()[0])
            segments.append(cycles[i].get_segments())   # get all segments to account for head-on collisions
        
        for segment in segments[0]:
            if head[1].get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in segments[1]:
            if head[0].get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        segments = []
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            for i in range(len(cycles)):
                segments.append(cycles[i].get_segments())
            # food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for i in range(len(cycles)):
                for segment in segments[i]:
                    segment.set_color(constants.WHITE)
                # food.set_color(constants.WHITE)