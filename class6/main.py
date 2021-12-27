from arg_parsing import args



def main_func():
    print("main function start")
    print("machine name", args.name[0])
    print("machine id", args.name[1])
    print("main function end")


main_func()