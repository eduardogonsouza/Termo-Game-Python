import survey


def inputLimited(limited, terminalSize):

    limit = limited

    def info(widget, name, info):
        result = widget.resolve()
        remain = limit - len(result)
        if remain < 0:
            raise survey.widgets.Abort("")
        return ""

    corretTerminalSize = (terminalSize - limited) - 5

    return survey.routines.input("".rjust(corretTerminalSize // 2), info=info).upper()
