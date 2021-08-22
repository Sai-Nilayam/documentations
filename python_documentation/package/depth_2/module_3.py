WHAT_MODULE = 'This is module 3.'

# Crating a Class
class Person:
    # Here the documentation is. This is a comment. So this text will not be 
    # shown by the help fucntion while showing the documentation of the class.
    """This is a Person Class that takes mandatory argumes as the name of the
    person and his/her age.
    """
    def __init__(self, name, age):
        """Here the __init__() funciton goes. This funciton is called when 
        an object of this class is institiated.
        """
        self.name = name 
        self.age = age 
    
    def show_info(self):
        """This fucntion shows the information of the object. 
        """
        return 'My name is {} and my age is {}.'.format(self.name, self.age)
