def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """Print a string centred, with ** either side.

    Args:
        text (str, optional): The string to print. 
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
        screen_width (int, optional): The overall width to print within
        (including the 4 spaces for the ** either side).

    Raises:
        ValueError: if the supplied string is too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String '{}' has exceeded the limit length"
                         .format(text))
        
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)
        

text_len = 60
banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!", text_len)
banner_text("And that's to laugh and smile and dance and sing,", text_len)
banner_text(screen_width=50)
banner_text("When you're feeling in the dumps,", text_len)
banner_text("Don't be silly chumps,", text_len)
banner_text("Just purse your lips and whistle - that's the thing!", text_len)
banner_text("And... always look on the bright side of life...", text_len)
banner_text("*", text_len)