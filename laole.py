def laole():

    active = True
    while active:
        things = input("请输入牢乐干的抽象事： (输入quit以退出)")
        if things == 'quit':
            break
        else:
            print("不是，就，铁要" + things + "的，你真不急吗哥们？")


laole()