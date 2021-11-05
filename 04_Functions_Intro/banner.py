def banner_text(text:str=" ", screen_width:int=80):
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