#! python3


class Person:
    def __init__(self, name):
        self.name = name

        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name

        self.age = None

    def getLastName(self):
        return self.lastName

    def setAge(self, age):
        """
        :type age: an integer greter than 0
        """
        self.age = age

    def getAge(self):
        if self.age is None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name


class USResident(Person):
    """
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        super().__init__(name)

        if status not in ["citizen", "legal_resident", "illegal_resident"]:
            raise ValueError

        self.status = status

    def get_status(self):
        """
        Returns the status
        """
        return self.status
