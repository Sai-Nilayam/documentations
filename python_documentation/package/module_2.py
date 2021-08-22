# %%
import sys 
import_path = '/home/sai-nilayam/z_sai_nilayam_2021_04_12/developments/'\
    'project_1/python_documentation'
sys.path.append(import_path)

# for i, path in enumerate(sys.path):
#     print('{}.'.format(i), path, end='\n\n')

import module_1

# Sub Class is a Class that has all the attributes and methods of the Super 
# Class with some extra Features. 
class MaleCustomer(module_1.Customer):
    CREATER = 'Keith Galli'

    def __init__(self, name, age, gender='Male'):
        super().__init__(name, age, gender)
        # Attribute Overiding means simply overiding Class Attribute or 
        # Instance Attribute with another object.
        self.gender = 'Male'
    
    def say_male_voice(self):
        return 'Males are best.'

    # Method Overriding means Overriding a Regular Method or a Class Method
    # or a Static Method with another Method. Only you need to specify the 
    # a new Method with the same name of that previous in order to Override 
    # the previous Super Class method.
    def show_class_info(self):
        return 'This is a method of Class MaleCustomer.'

    @staticmethod
    def a_static_method():
        return 'This is a Static Method in Class MaleCustomer.'

    # Special Methods are used in a Class for special perposes. You could get
    # list of differnt Special Methods and their default funcitonalities in 
    # Python documentaion.
    def __str__(self):
        return 'This is a MaleCustomer\'s Object.'