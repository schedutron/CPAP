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


def validate_arguments(func):
    def wrapped_func(n1, n2):
        if not validate_two_arguments(n1, n2):
            raise Exception("Arguments must be numbers!")
        return func(n1, n2)
    return wrapped_func


@validate_arguments
def add(n1, n2):
    return n1 + n2
