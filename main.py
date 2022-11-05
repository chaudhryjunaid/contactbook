from contactbook import contactbook, contactcard

if __name__ == '__main__':
    cbook = contactbook.ContactBook()
    cmd = "__init__"
    while cmd != "quit" or cmd != "exit":
        cmd = input(">> ")
        if cmd == "add":
            name = input("name? ")
            email = input("email? ")
            phone = input("phone? ")
            cbook += contactcard.ContactCard(name, email, phone)
            cbook.list()
        elif cmd == "list":
            cbook.list()
        elif cmd == "delete":
            raise NotImplementedError
