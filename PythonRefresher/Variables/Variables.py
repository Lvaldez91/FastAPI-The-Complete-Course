"""
Variables
"""

first_name = "Lucero"
print(first_name)
first_name = "Juan"
print(first_name)

def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))