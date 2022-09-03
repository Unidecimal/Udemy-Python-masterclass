def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(text):
    left_margin = (80 - len(str(text))) // 2
    print(" " * left_margin, text)


def centre_text_arg(*args, sep=' ', end='\n', file=None, flush=False):
    text = str()
    for index, arg in enumerate(args):
        if len(args)-1 != index:
            text += str(arg) + sep
        else:
            text += str(arg) + ""
    left_margin = (80 - len(str(text))) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


def centre_text_arg_return(*args, sep=' '):
    text = str()
    for index, arg in enumerate(args):
        if len(args)-1 != index:
            text += str(arg) + sep
        else:
            text += str(arg) + ""
    left_margin = (80 - len(str(text))) // 2
    return " " * left_margin + text

python_food()
centre_text("Jazzkillen")
centre_text(80)
centre_text([125, 444, 88])

with open("centerd", mode='w') as centre_file:
    centre_text_arg("Jazzkillen", file=centre_file)
    centre_text_arg(80, file=centre_file)
    centre_text_arg([125, 444, 88], file=centre_file)
    centre_text_arg("first", "fortytwo", 42, "spam", sep="*", file=centre_file)

print(centre_text_arg_return("Jazzkillen"))
print(centre_text_arg_return(80))
print(centre_text_arg_return([125, 444, 88]))
print(centre_text_arg_return("first", "fortytwo", 42, "spam", sep="*"))

with open("menu", "w") as menu:
    print(centre_text_arg_return("Jazzkillen"), file=menu)
    print(centre_text_arg_return(80), file=menu)
    print(centre_text_arg_return([125, 444, 88]), file=menu)
    print(centre_text_arg_return("first", "fortytwo", 42, "spam", sep="*"), file=menu)
