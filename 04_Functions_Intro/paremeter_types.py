# Python參數在函式中的排序規則
def func(pos_arg1, pos_arg2, *args, k, **kwargs):
    print("positional-or-keywords:...{}, {}".format(pos_arg1, pos_arg2))
    print("var-positional:...........{}".format(args))
    print("keyword:..................{}".format(k))
    print("var-keywords:.............{}".format(kwargs))
    
    
func(0, 1, 2, 3, 4, 5, 7, 9, k=11, key1=14, key2=16)
