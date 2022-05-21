"""

just some self practice of the list/append function
learning how to efficiently create lists rather than once at a time.

"""

lst = []
lst_bw = []
list_range = list((range(1, 11)))

for number in list_range:
    lst.append(f"hello {number}")

print(lst)

lst.append("goodbye")

print(lst)

list_range_bw = list((range(10, 0, -1)))

for number in list_range_bw:
    lst_bw.append(f"hello {number}")

print(lst_bw)

