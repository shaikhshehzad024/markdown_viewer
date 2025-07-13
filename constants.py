import shutil

BOLD = '\033[1m'
BOLD_ = '\033[22m'
ITALIC = '\033[3m'
ITALIC_ = '\033[23m'
UNDERLINE = '\033[4m'
UNDERLINE_ = '\033[24m'
STRIKETHROUGH = '\033[9m'
STRIKETHROUGH_ = '\033[29m'
CODE = '\033[38;5;246m'
LINK = '\033[34m'
RESETCOLOR = '\033[39m'
RESET = '\033[0m'
QUOTE = '\033[90m'
LIST = '\033[92m'


BLUE = "\033[34m"
CYAN = "\033[36m"
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"

HEADER_COLORS = [
    '\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m',
    RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN
]

columns = shutil.get_terminal_size().columns
HLINE_CHARS = {'*', '-', '_'}
