"""practice importing modules"""

import random
import module

random_int = random.randint(1, 15)
print(random_int)

random_flt = random.random()
rounded = float(round(random_flt, 2))
print(rounded)

print(module.pi)  # seing how I can pull from another file or module