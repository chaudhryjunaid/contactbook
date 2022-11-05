class ContactCard:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f'<ContactCard "{self.name}">'

    def __str__(self):
        return f'[{self.name}]: {self.email}, {self.phone}'

    def __eq__(self, other):
        return self.name == other.name and self.phone == other.phone and self.email == other.email


if __name__ == "__main__":
    billy = ContactCard("bill nottingham", "b.notingham@xyz.com", "+123456789")
    print(f'str billy: {billy!s}')
    print(f'repr billy: {billy!r}')
