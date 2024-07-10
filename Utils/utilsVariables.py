import os, sys

CLEAR_RIGHT = "\033[K"
PREV_LINE = "\033[F"


terminalSize = int(os.get_terminal_size().columns)
