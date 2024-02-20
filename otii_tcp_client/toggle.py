from enum import Enum


class Toggle(Enum):
    """ An enumeration type that represents toggling, e.g., a channel for
    recording.
    """
    ON = True
    OFF = False