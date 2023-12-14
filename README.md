Python Calculator

Overview

This Python project implements a simple calculator that performs basic mathematical operations such as addition, subtraction, multiplication, and division.
The calculator allows users to input two numeric values and select the desired operation.
The project is organized into multiple files for modularity and readability.

Files
1. calculator.py
This file serves as the main entry point for the calculator application. It provides a menu for users to select the desired mathematical operation. The available operations include addition, subtraction, multiplication, and division.

python
Copy code
import addition
import subtraction
import multiplication
import division

def select_operation():
    # ... (code for displaying menu and handling user input)

if __name__ == '__main__':
    select_operation()
2. numbers.py
This file contains a utility function get_valid_input() that prompts the user to enter two numeric values. It ensures that the input values are valid numeric entries.

python
Copy code
def get_valid_input():
    # ... (code for obtaining valid numeric input)
3. division.py
This file defines the division operation. It uses the get_valid_input() function from numbers.py to obtain valid numeric values for the division.

python
Copy code
from numbers import get_valid_input

def division():
    # ... (code for performing division operation)

if __name__ == '__main__':
    division()
4. multiplication.py
This file implements the multiplication operation. It also utilizes the get_valid_input() function to ensure valid input.

python
Copy code
from numbers import get_valid_input

def multiplication():
    # ... (code for performing multiplication operation)

if __name__ == '__main__':
    multiplication()
5. subtraction.py
This file contains the subtraction operation, leveraging the get_valid_input() function for valid numeric input.

python
Copy code
from numbers import get_valid_input

def subtraction():
    # ... (code for performing subtraction operation)

if __name__ == '__main__':
    subtraction()
6. addition.py
The file implements the addition operation, utilizing the get_valid_input() function for obtaining valid numeric values.

python
Copy code
from numbers import get_valid_input

def addition():
    # ... (code for performing addition operation)

if __name__ == '__main__':
    addition()
How to Use
Run the calculator.py file.
Select the desired mathematical operation by entering the corresponding number.
Enter the required numeric values when prompted.
View the calculated result.
Note: The calculator handles invalid numeric input gracefully, providing appropriate error messages.
