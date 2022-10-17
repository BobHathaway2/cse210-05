from game.casting.actor import Actor

class Message(Actor):
    """
    A message that provides information to the cyclists
    
    The responsibility of message is to contain a message for the user and where it is to be printed on the screen.

    Attributes:
        Inherited from Actor:
            _text (string): contains the message text to be displayed
            _position (Point): The screen coordinates
    """

    def __init__(self):
        "Constructs a new actor called message"
        super().__init__()

    def set_position_and_text(self, position, text):
        "allows specification of where and what to put on the screen"
        self._position = position
        self._text = text