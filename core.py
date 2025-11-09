from collections import UserDict


class InvalidPhoneFormatError(Exception):
    """Custom exception for invalid phone format."""

    def __init__(self, message="Invalid phone format: must be 10 ASCII digits."):
        super().__init__(message)


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        if isinstance(other, Field):
            return self.value == other.value
        return NotImplemented


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value: str):
        """Raises InvalidPhoneFormatError for invalid phone format"""
        value = value.strip()
        if len(value) != 10 or not (value.isascii() and value.isdigit()):
            raise InvalidPhoneFormatError
        self.value = value


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, value: str):
        """Raises InvalidPhoneFormatError for invalid phone format"""
        self.phones.append(Phone(value))

    def remove_phone(self, value: str):
        """Raises ValueError for value lookup and IndexError for delete"""
        del self.phones[self.phones.index(value)]

    def edit_phone(self, old_value: str, new_value: str):
        """Raises ValueError for value lookup and IndexError for change"""
        """Raises InvalidPhoneFormatError for invalid phone format"""
        self.phones[self.phones.index(old_value)] = Phone(new_value)

    def find_phone(self, value: str) -> Phone:
        """Raises ValueError for value lookup and IndexError for read"""
        return self.phones[self.phones.index(value)]


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def delete(self, name: str):
        """Raises KeyError for key lookup"""
        del self.data[name]

    def find(self, name: str) -> Record:
        """Raises KeyError for key lookup"""
        return self.data.get(name)
