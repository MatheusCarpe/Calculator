def get_valid_input():
    while True:
        try:
            v1 = float(input('Now enter the first value: '))
            v2 = float(input('Second value: '))
            return v1, v2
        except ValueError:
            print("Please enter valid numeric values.")
