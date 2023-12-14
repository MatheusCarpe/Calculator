from numbers import get_valid_input

def multiplication():
    total = float
    try:
        v1, v2 = get_valid_input()
    except ValueError:
        return

    total = v1 * v2
    print("Result = {:.2f}".format(total))

if(__name__ == '__main__'):
    multiplication()