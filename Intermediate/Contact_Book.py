print("Contact Book")
class Contact:
    book = []
    def contact_book():
      while True:  
        print("1) Add Contact")
        print("2) Display Contact")
        print("3) Search Contact")
        print("4) Delete Contact")
        opt = int(input("Choose any option = "))
        if opt == 1:
            Contact.add_cont()

        elif opt == 2:
            Contact.display_cont()

        elif opt == 3:
            Contact.search_cont()

        elif opt == 4:
            Contact.delete_cont()            
        
    def add_cont():
        name = input("Enter Name =")
        phone = int(input("Enter phone Number = "))
        cont_list = {'Name' : name, 'Phone' : phone}
        Contact.book.append(cont_list)
        print("Successfully add")

    def search_cont():
        pass


    def display_cont():
        print(Contact.book)

    def delete_cont():
        pass

Contact.contact_book()