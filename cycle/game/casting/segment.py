from game.casting.actor import Actor

class Segment(Actor):
    """
    All the segments of the cycle from head to the last trailing toxic cloud
    
    The responsibility of the segment is to know what it looks like, where it is, and how it's moving

    Attributes:
        Inherited from Actor:
            _text (string): contains the message text to be displayed
            _position (Point): The screen coordinates
            _velocity (Point): The velocity x and y components
    """

    def __init__(self):
        "Constructs a new actor segment"
        super().__init__()
