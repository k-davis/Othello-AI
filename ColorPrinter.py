
F_BLACK = '\u001b[30m'
F_RED = '\u001b[31m'
F_GREEN = '\u001b[32m'
F_YELLOW = '\u001b[33m'
F_BLUE = '\u001b[34m'
F_MAGENTA = '\u001b[35m'
F_CYAN = '\u001b[36m'
F_WHITE = '\u001b[37m'

BK_BLACK = '\u001b[40m'
BK_RED = '\u001b[41m'
BK_GREEN = '\u001b[42m'
BK_YELLOW = '\u001b[43m'
BK_BLUE = '\u001b[44m'
BK_MAGENTA = '\u001b[45m'
BK_CYAN = '\u001b[46m'
BK_WHITE = '\u001b[47m'


RESET = '\u001b[0m'




def cprint(color, text):
	print(color + text + RESET)

def cprint(background_color, text_color, text):
	print(background_color + text_color + text + RESET)


	
