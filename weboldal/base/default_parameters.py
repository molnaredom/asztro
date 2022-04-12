def get_basic_parameters():
    return {
        "logging_level": "debug"
    }


# debug levels
# error -> printe()
# warning -> printw()
# debug -> printd()
# info -> printi()

def print_altalanos(level):
    logging_level = get_basic_parameters()["logging_level"]
    if logging_level == "info":
        if level == "e" or "w" or "i":
            return True
        else:
            return False
    elif logging_level == "debug":
        if level == "e" or "w" or "d" or "i":
            return True
        else:
            return False
    elif logging_level == "warning":
        if level == "e" or "w":
            return True
        else:
            return False
    elif logging_level == "error":
        if level == "e":
            return True
        else:
            return False


def printe(*args, problema):
    if print_altalanos("e"):
        print(f"E: [{problema}]: ",*args)


def printw(*args, problema):
    if print_altalanos("w"):
        print(f"W: [{problema}]: ",*args)


def printd(*args,problema=""):
    if print_altalanos("d"):
        print(f"D: [{problema}]",*args)


def printi(*args):
    if print_altalanos("i"):
        print(f"I: ",*args)
