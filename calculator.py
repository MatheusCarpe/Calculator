import addition
import subtraction
import multiplication
import division

def select_operation():
    while True:
        print('-' * 11)
        print('CALCULATOR')
        print('-' * 11)

        print('*' * 25)
        print('1 FOR (+) ADDITION')
        print('2 FOR (-) SUBTRACTION')
        print('3 FOR (*) MULTIPLICATION')
        print('4 FOR (/) DIVISION')
        print('0 TO EXIT')
        print('*' * 25)

        operation = int(input('Enter the desired mathematical operation: '))

        if (operation == 0):
            print('Exiting calculator. Goodbye!')
            break

        elif (operation == 1):
            print("Selected operation... ADDITION")
            addition.addition()

        elif (operation == 2):
            print("Selected operation... SUBTRACTION")
            subtraction.subtraction()

        elif (operation == 3):
            print('Selected operation... MULTIPLICATION')
            multiplication.multiplication()

        elif (operation == 4):
            print('Selected operation... DIVISION')
            division.division()

        else:
            print('Select a valid option')

if(__name__ == '__main__'):
    select_operation()

