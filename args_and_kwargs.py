def my_args_exapmle(*args):
    print(args)
    for arg in args:
        print(arg)

    #*args means we can pass a varible number of values to a function
def my_kwargs_example(**kwargs):
    print(kwargs)
    for kwarg_key, kwargs_val in kwargs.item():
        print(f"{kwarg_key}: {kwargs_val}")


if __name__ =="__main__":
    my_args_exapmle(1, 2, 3, 4)
    my_kwargs_example(name="klins, ")