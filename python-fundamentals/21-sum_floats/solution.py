def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float) or 0
