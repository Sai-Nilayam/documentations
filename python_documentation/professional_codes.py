"""This Module focuses on how to write clean and professional Python codes.
"""


def my_func(name: str, age: int) -> str:
    """This fucntion takes input as name and age and reuturns
    the identificaiton.
    """
    new_age = age + 1
    return_str = 'My name is {} and my age is {}.'.format(name, new_age)
    return return_str


print(my_func('Keith', 23))

print(help(my_func))
