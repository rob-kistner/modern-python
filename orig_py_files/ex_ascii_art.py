from pyfiglet import figlet_format
from termcolor import colored


def run_fig(msg, color="white"):
    """
    Prints out pyfiglet text in a specified color.
    """
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")
    if color not in valid_colors:
        color = "white"
    print(colored(figlet_format(msg), color=color))


run_fig("Hi from PyFiglet!", "cyan")
run_fig("There are none", "blue")
run_fig("FIGLETS")
