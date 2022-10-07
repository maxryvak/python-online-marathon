def logger(func):
    def inner(*args, **kwargs):
        f = func(*args, **kwargs)
        string = [str(i) for i in args]
        for i in kwargs.values():
            string.append(str(i))
        print("Executing of function " + func.__name__ + " with arguments " + ", ".join(string) + "...")
        return f
    return inner

@logger
def concat(*args, **kwargs):
    string = [str(i) for i in args]
    for i in kwargs.values():
        string.append(str(i))
    return "".join(string)


@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)
