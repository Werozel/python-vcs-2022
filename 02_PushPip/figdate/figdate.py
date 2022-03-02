import time
import pyfiglet


def date(format_str: str = "%Y %d %b, %A", font: str = "graceful") -> str:
    return pyfiglet.figlet_format(time.strftime(format_str), font=font)
