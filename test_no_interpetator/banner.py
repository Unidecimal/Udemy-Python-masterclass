def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a string centered, with ** on either side of it.

    :param text: The string to print.
        An asterisk (*) will return a row of asteriks.
        The default will print a blank line, bordered by ** on each side.
    :param screen_width: The wished screen width to print the `text` in.
        ( including the space for ** on each side. ) The default is width
        is 80. 
    :raises ValueError: If `text` doesn't fit defined `screen_width`.
    """
    if len(text) > screen_width - 4:
        # print("EEK!!")
        # print("THE TEXT IS TO LONG TO FIT IN THE SPECIFIED WITH {}"
        #       .format(screen_width))
        # Instead of this message it is better to raise an exception
        raise ValueError("String: \"{0}\" is larger then specified "
                         "width {1}".format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", 60)
banner_text("Det finns en dålig del av landet", 60)
banner_text("som man lämnar om man kan det", 60)
banner_text("och den delen kallas 'landet'", 60)
banner_text("och den ligger här och var", 60)
banner_text(screen_width=60)
banner_text("Där har dom granbevuxna hagar,", 60)
banner_text("bidragstagare som jagar", 60)
banner_text("Där har mor och dotter samma karl till far", 60)
banner_text("*", 60)
