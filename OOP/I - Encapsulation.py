# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside And Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------

class member:

    def __init__(self, name):

        self.name = name #public

one = member("Khaled")
print(one.name)    # Khaled
one.name = "yossif"
print(one.name)    # yossif

print("=" * 50)


class member:

    def __init__(self, name):

        self._name = name #protected

one = member("Khaled")

# it supposed that we can't access the property cuz it's protected
# but unfortunately we can
# Python use "_" just as a note for the coder to not use it out the class

print(one._name)     # Khaled
one._name = "yossif" # and you can change it to
print(one._name)     # yossif

print("=" * 50)


class member:

    def __init__(self, name):

        self.__name = name #private

    def hello(self):

        print(f"Hello, {self.__name}")

one = member("Khaled")
one.hello()  # Hello, Khaled
#print(one.__name) # AttributeError: 'member' object has no attribute '__name'

# But unfortunatuly you still can access the private attribute
# Python use "__" just as a note for the coder to not use it out the class

print(one._member__name)  # Khaled


