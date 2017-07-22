def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def validate_two_arguments(n1, n2):
    if not (is_number(n1) and is_number(n2)):
        return False
    return True


def convert_arguments(func):
    def _wrapped_func(*args):
        new_args = [float(arg) for arg in args]
        return func(*new_args)
    return _wrapped_func


def validate_arguments(func):
    def wrapped_func(*args):
        for arg in args:
            if not is_number(arg):
                raise Exception("Arguments must be numbers!")
        if len(args) < 2:
            raise Exception("Must specify at least 2 arguments!")

        return func(*args)
    return wrapped_func


@validate_arguments
def add(*args):
    return sum(args)


@validate_arguments
@convert_arguments
def divide_n(*args):
    cumu = args[0]
    for arg in args[1:]:
        cumu /= arg
    return cumu
