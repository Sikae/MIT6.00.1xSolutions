#! python3


class Person:
    def __init__(self, name):
        self.name = name

        try:
            first_blank = name.rindex(' ')
            self.last_name = name[first_blank + 1:]
        except:
            self.last_name = name

        self.age = None

    def get_last_name(self):
        return self.last_name

    def set_age(self, age):
        """
        :type age: an integer greater than 0
        """
        self.age = age

    def get_age(self):
        if self.age is None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        if self.last_name == other.lastName:
            return self.name < other.name
        return self.last_name < other.lastName

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
