import contactcard


class ContactBook:
    def __init__(self, contactcards = []):
        self.contactcards = contactcards

    def __repr__(self):
        return f'<ContactBook contacts={len(self.contactcards)}>'

    def __str__(self):
        return f"ContactBook({len(self.contactcards)} ContactCards)"

    def __iadd__(self, other):
        if type(other) == "ContactBook":
            self.contactcards += other.contactcards
            return self
        elif type(other) == "ContactCard":
            self.contactcards.append(other)
            return self

    def __add__(self, other):
        if type(other) == "ContactBook":
            return ContactBook(self.contactcards + other.contactcards)
        elif type(other) == "ContactCard":
            return ContactBook(self.contactcards + [other])

    def __len__(self):
        return len(self.contactcards)

    def add_card(self, card):
        if isinstance(card, contactcard.ContactCard):
            self.contactcards.append(card)
        else:
            raise ValueError

    def list(self):
        print(f'There are {len(self)} cards in this contact book. A chronological listing follows:')
        for cc in self.contactcards:
            print(cc)


if __name__ == '__main__':
    cb = ContactBook()
    cb.add_card(contactcard.ContactCard("Bill Joy", "bjoy@att.com", "+123456789"))
    print("str cb:" + str(cb))
    print("repr cb:" + repr(cb))
    cb.list()
