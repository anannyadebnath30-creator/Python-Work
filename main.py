# Q5. Demonstrating user-defined modules and packages
# Run this file from the Q5_modules_packages folder.

import arithmetic_module.arithmetic as arithmetic
from arithmetic_module import add, multiply
from student import display_details, display_result

print("Module import (whole module):", arithmetic.subtract(15, 4))
print("Selected import - addition:", add(10, 5))
print("Selected import - multiplication:", multiply(6, 3))
print("Division:", arithmetic.divide(20, 4))

display_details("Riya", "101", "MCA")
display_result([78, 82, 91])
