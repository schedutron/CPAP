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

def convert_arguments_to(to_type=float):
    def _wrapper(func):
        def _wrapped_func(*args):
            new_args = [to_type(arg) for arg in args]
            return func(*new_args)
        return _wrapped_func
    return _wrapper


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
def divide_n(*args):
    cumu = args[0]
    for arg in args[1:]:
        cumu /= arg
    return cumu

# Both of the functions below will give the same result because Python3 doesn't
# do integer division by default.
@convert_arguments_to(to_type=float)
def divide_n_as_floats(*args):
    return divide_n(*args)


@convert_arguments_to(to_type=int)
def divide_n_as_integers(*args):
    return divide_n(*args)
