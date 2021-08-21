# Creating a Class.
class Customer:
    # Class Attributes are constant for all of the objects created by the
    # class.
    CREATER = 'Sai Nilayam Sahu'

    # Instance Attributes are set by the __init__ method. These could be
    # different for different objects as per the parameters passed to it when
    # the object is instantiated.
    def __init__(self, name, age, gender, mobile=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile

        # self.mobile = self.Mobile()

    # A Rgular Method takes its first argument the object itself. A convention
    # used for the object itself is 'self'.
    def show_info(self, user_name):
        """This method returns the informationa about the customer with a 
        greeting to the user.
        """
        string_structure = 'Hi Dear {}! I am a customer. My name is {}. I am'\
            ' {} years old. I am a {}.'
        return_str = string_structure.format(
            user_name,
            self.name,
            self.age,
            self.gender
        )

        return return_str

    @classmethod
    def show_class_info(cls, username):
        string_structure = 'Hi Dear {}! The creater of this Class is Dear {}.'
        return_string = string_structure.format(
            username,
            cls.CREATER
        )

        return return_string

    # A Static Method does not take its first arguments the object itself.
    @staticmethod
    def a_static_method(username):
        string_structure = 'This is a static method. This method is called by'\
            ' user {}.'
        return_str = string_structure.format(username)

        return return_str

    # Defining an Inner Class means defining a blueprint for an Object that is
    # only used in the Outer Class's Object. So it is logically fit to group
    # the codes to create the inside Object inside the Outer Object creating
    # code.
    class Mobile:
        def __init__(self, brand, processor, ram):
            self.brand = brand
            self.processor = processor
            self.ram = ram

        def show_mobile_info(self):
            return 'This is a {} mobile with {} processor and {} GB ram.'\
                .format(self.brand, self.processor, self.ram)
