from numbers import get_valid_input

def division():
    try:
        v1, v2 = get_valid_input()
    except ValueError:
        return

    if v2 == 0:
        print("Attention...Cannot divide numbers by zero")

    else:
        total = v1 / v2
        print("Result = {:.2f}".format(total))

if(__name__ == '__main__'):
    division()