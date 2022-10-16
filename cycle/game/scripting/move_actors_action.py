from game.scripting.action import Action


class MoveActorsAction(Action):
    """An action that causes the actor to move. 
    
    The responsibility of MoveActorsAction is to move each actor in the cast to their next location

    Attributes:
        _actors (list): actors in the cast
    """

    def __init__(self):
        super().__init__()
        self._actors = []

    def execute(self, cast, script):
        self._actors = cast.get_all_actors()
        for _actor in self._actors:

            _actor.move_next()

