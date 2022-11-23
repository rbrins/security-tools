# TODO: learn about the inspect library to get parent functions and line numbers, then this is pretty much automated
import inspect

# Modify verbsoity in the debugger functions to match the verbose arguments in the main function
def debugger_func(lineNum, verbosity=True):
    def wrapper(func):
        if(verbosity):
            print("[D-{:03d}] {}() started.".format(lineNum, func.__name__))
        func()
        if(verbosity):
            print("[D-{:03d}] {}() finished.".format(lineNum, func.__name__))
    return wrapper

# Modify verbsoity in the debugger functions to match the verbose arguments in the main function
def debugger_inline(lineNum, funcName, message="debugging line encountered.", verbosity=True):
    if(verbosity):
        print("[D-{:03d} {} {}".format(lineNum, funcName, message))
    return


@debugger_func(lineNum=11)
def demo_function():
    functionName = "demo_function()"
    print("Executing task!")
    debugger_inline(lineNum=21, funcName = functionName)
    print("Task completed!")

