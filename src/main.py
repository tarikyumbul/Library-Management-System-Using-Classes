"""
Istanbul Sehir University
ENGR101 - Introduction to Programming
Mini Project 4 - Project Template
library Management System

Notes:
1. You have to use this template
2. You should fill the attributes and the methods
3. Please read the PDF carefully before starting
4. "TODO" statements will give you the general idea about each part
5. To have a clear understanding please use the attached executable file to test the project and check how it works
"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class MenuItem:
    """ This class initialises Item for a menu """

    def __init__(self, text, number):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below

        self.text = text
        self.number = number


    def display(self):
        """ This method displays item menu """
        #  TODO: implement the method to display the attributes in str type by returning them
        # write your code below
        number = 0
        return str(self.number) + ". " + self.text  # < Returns a menu option with the following pattern.
                                                    # 2. Add a book to my book list.

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class Menu:
    """ This class initialises a menu """

    number = 1  # < Initialization for the numbers of menu options.

    def __init__(self, header, menuItems):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below

        self.header = header
        self.menuItems = menuItems


    def display(self, display_header):
        """ This method displays menu instance """
        #  TODO: implement the method to print the menu items here with the header according to the flag
        # write your code below


        if display_header == "":
            print(self.menuItems.display())
        # ^ Doesn't display the header if the "display_header" parameter is an empty string. Displays only the menu
        # according to the "menuItems" attribute. Which is determined by the Admin or Student classes.

        elif display_header:
            print("\n" + self.header + "\n")
        # ^ Displays the header according to the "display_header" parameter value.

            number = 1
            for item in self.menuItems:
                print(MenuItem(item, number).display())
                number += 1
            # ^ Displays the menu according to the "menuItems" attribute.


    def add_menu_item(self):
        """ This method adds menu item """
        # TODO: implement the method to add menu items by creating an object of MenuItem class here and adding it to
        #  the list (instance level attribute "menuItems") of this class. At the end of this method return a string
        #  states that the menuitem has been successfully added write your code below
        pass
    # ^ I am not sure how to use this. Didn't need it.

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class User:
    """ This class initialises user instance """
    #  TODO: initialise the class level attributes here
    # write your code below

    menu_items = []  # < Stores menu items for every user type. Meant to be updated afterwards.
    menu = Menu("", menu_items)  # < A "Menu" object. Fills the "display_header" parameter with an empty string and the
                                 # "menuItems" with "menu_items" which will be filled with proper menu items afterwards.


    def __init__(self, name, password):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below

        self.name = name
        self.password = password


    def display(self):
        """ This method displays user instance """
        #  TODO: implement the method to display the attributes in str type by returning them
        # write your code below

        return "Username: " + self.name + ", Password: " + self.password
        # ^ Displays the "username" and the "password" with this pattern: "Username: admin, Password: 0000"


    def menu_builder(self):
        """ This method build the default menus for admin and student """
        # TODO: implement the method to build the menu here by using the class level attribute "menu" and its method
        #  "add_menu_item" write your code below

        return self.menu.display("")  # < Uses "menu" which is an object of "Menu" class to build and display the menu.

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class Admin(User):
    #  TODO: inherit the user class
    #  TODO: initialise the class level attributes here
    # write your code below

    menu_items = ["List Books", "Create a Book", "Delete a Book", "Search For a Book",
                  "Change Number of Copies of a Book", "Show Students Borrowed a Book by ID",
                  "List Users", "Create User", "Delete User", "Exit"]
    # ^ Overrides the "menu_items" attribute of "User" class to update it with the admin menu items.

    menu = Menu("Welcome to admin menu.", menu_items)  # < Overrides the "menu" attribute of "User" class to update the
                                                       # header with the admin header.

    role = "admin"  # < This is always admin and I have no idea what it is used for.


    def __init__(self, name, password):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below

        super().__init__(name, password)


    def menu_builder(self):
        return self.menu.display(True)
    # ^ Overrides "menu_builder" method of the "User" class and makes it possible to display the header.

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class Student(User):
    #  TODO: inherit the user class
    #  TODO: initialise the class level attributes here
    # write your code below

    menu_flag = False  # < Meant to prevent printing of the student menu more than once, I guess. I didn't use this and
                       # the program works well.

    menu_items = ["Search for a Book", "Add a Book to My Book List", "Delete a Book From My Book List",
                  "Show My Borrowed Books", "Exit"]
    # ^ Overrides the "menu_items" attribute of "User" class to update it with the student menu items.

    menu = Menu("Welcome to student menu.", menu_items)  # < Overrides the "menu" attribute of "User" class to update
                                                         # the header with the student header.

    role = "student"  # < This is always admin and I have no idea what it is used for.


    def __init__(self, name, password):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below

        super().__init__(name, password)


    def menu_builder(self):
        if not self.menu_flag:
            return self.menu.display(True)
        else:
            pass
    # ^ Returns the student menu with the header if "menu_flag" is False.

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class UsersDB:
    """ This class initialises the the DB for user instances """
    #  TODO: initialise the class level attributes here
    # write your code below

    example_users = {"admin": ["0000", "admin"], "Ahmet": ["1234", "student"], "Ayse": ["4321", "student"]}
    # ^ I used this as an all users dictionary. Stores the usernames as keys and a list of user properties which are
    # password and the role as values.

    user_objects = {"admin": Admin("admin", "0000"), "Ahmet": Student("Ahmet", "1234"), "Ayse": Student("Ayse", "4321")}
    # ^ A dictionary for storing usernames as keys and user objects of corresponding classes as values.

    def __init__(self, example_users_flag=True):
        #  TODO: implement the method to call the "create_example_users" function here according to the flag
        # write your code below

        self.example_users_flag = example_users_flag


    def create_example_users(self):
        """ This method creates example users to be used in this demo """
        # TODO: implement the method to add the example users by using "add_user" function and return a string that
        #  shows it has been added successfully write your code below
        # write your code below
        pass
    # ^ I didn't understand and need this method.


    def add_user(self, name, password):
        """ This method adds a user to users DB """
        #  TODO: implement the method to create Student/Admin object according to the role and add it the class level
        #   instance "users_objects and return a string that shows it has been added successfully
        # write your code below

        self.example_users[name] = [password, "student"]
        self.user_objects[name] = Student(name, password)
    # ^ Adds a user's credentials to corresponding places.


    def remove_user(self, name):
        """ This method removes a user from users DB """
        #  TODO: implement the method to remove a user by the name after listing all the users by "list_user" function
        # write your code below

        if name in self.example_users:
        # ^ Checks if the user exists in the library.
            self.example_users.pop(name)
            self.user_objects.pop(name)
            for (bid, borrower) in Library.borrowed_books.items():  # < Takes book ID and the borrower list as tuples.
                if name in borrower:
                    Library.borrowed_books[bid].remove(name)
                else:
                    pass
            # ^ Checks if the user currently holds a book. If so, removes it from there.
            print("\nUser '" + name + "' has been removed from the library.")

        else:
            print("\nInvalid username.")


    def list_user(self):
        """ This method list all users in the users db """
        # TODO: implement the method to list all student users and return a string that shows it has been added
        #  successfully write your code below
        # write your code below

        print("Username:Password")
        number = 1
        for (user, password) in self.example_users.items():
            if user != "admin":
                print(str(number) + "- " + user + ":" + password[0])
                number += 1
            else:
                pass
        # ^ Takes keys and values of "example_users" as tuples. Displays only student credentials. Since "password" is
        # actually a list of user properties, we want only "password[0]".


    def validate_user(self, uid, password):
        """ This method validate user credentials """
        # TODO: implement the method to check username and password and return the username in terms of correct
        #  credentials and False in terms of wrong credentials
        # write your code below

        if uid in self.example_users and password == self.example_users[uid][0]:
            return self.user_objects[uid]

        else:
            return False
    # ^ Checks if the user input for "Username" and "Password" are valid. If so, returns that particular user's
    # "Admin" or "Student" class object. If not, returns False.

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class Book:
    """ This class initialises the book instances """

    def __init__(self, bid, name, no_of_copies, list_of_authors):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below

        self.bid = bid
        self.name = name
        self.no_of_copies = no_of_copies
        self.list_of_authors = list_of_authors


    def display(self, number):
        """ This method displays book instances """
        #  TODO: implement the method to display the attributes in str type by returning them
        # write your code below

        print(str(number) + ". Book ID: " + self.bid + ", Book Name: " + self.name + ", Number of Copies: " + str(self.
        no_of_copies) + ", Book Author(s): " + str(self.list_of_authors))

    # ^ Prints a single book's properties with a number at the beginning.

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class Library:
    """ This class initialises the library system """
    #  TODO: initialise the class level attributes here
    # write your code below

    example_books = {"001": ["Biology", 2, ["Alice", "Bob"]], "002": ["Chemistry", 3, ["Alice"]]}
    # ^ I use this as an all books dictionary.

    book_properties = {"001": ["001", "Biology", 2, ["Alice", "Bob"]], "002": ["002", "Chemistry", 3, ["Alice"]]}
    # ^ Stores all properties of a book as a value. What is different is, it stores ID, too, as a value.

    author_to_books = {"Alice": [Book(book_properties["001"][0], book_properties["001"][1], book_properties["001"][2],
    book_properties["001"][3]), Book(book_properties["002"][0], book_properties["002"][1], book_properties["002"]
    [2], book_properties["002"][3])], "Bob": [Book(book_properties["001"][0], book_properties["001"][1], book_properties
    ["001"][2], book_properties["001"][3])]}
    # ^ Stores author names as keys and "Book" objects as values. I didn't want to write more to change a book's copy
    # amount, so I take every property from above dictionary, "book_properties".

    book_objects = {"001": Book(book_properties["001"][0], book_properties["001"][1], book_properties["001"][2],
    book_properties["001"][3]), "002": Book(book_properties["002"][0], book_properties["002"][1], book_properties
    ["002"][2], book_properties["002"][3])}
    # ^ Stores book IDs as keys and objects as values.

    borrowed_books = {"001": ["Ahmet", "Ayse"], "002": ["Ayse"]}
    # ^ Stores IDs of books as keys and a list of its borrowers as values.


    def __init__(self, example_books_flag=True):
        #  TODO: implement the method to call the function "create_example_books" according to the flag
        # write your code below

        self.example_books_flag = example_books_flag


    def create_example_books(self):
        """ This method creates example books to be used """
        # TODO: implement the method to create the example books by using "add_book" function and return a string
        #  that shows it has been created successfully
        # write your code below
        pass
    # ^ I didn't understand and need this method.


    def add_book(self, bid, name, copies, authors):
        """ This method adds book to the library """
        # TODO: implement the method to add book by creating Book class object and to add it to the class level
        #  attribute "book_objects" and return a string that shows it has been added successfully
        # write your code below

        self.example_books[bid] = [name, copies, [authors]]
        # ^ Adds the new book to the "example_books" aka "all_books" dictionary.

        self.book_properties[bid] = [bid, name, copies, [authors]]
        # ^ Adds the new book to the "book_properties" dictionary.

        for author in authors:
            if author in self.author_to_books:
                self.author_to_books[author].append(Book(self.book_properties[bid][0], self.book_properties[bid][1],
                self.book_properties[bid][2], self.book_properties[bid][3]))

            else:
                self.author_to_books[author] = [Book(self.book_properties[bid][0], self.book_properties[bid][1],
                self.book_properties[bid][2], self.book_properties[bid][3])]
        # ^ If the author of the book already exists in the library, adds the new book's "Book" object to the author's
        # book list. If not, adds the author to the library and then adds the new book's "Book" object to the author's
        # book list.

        self.book_objects[bid] = Book(self.book_properties[bid][0], self.book_properties[bid][1],
        self.book_properties[bid][2], self.book_properties[bid][3])
        # ^ Adds the new book's "Book" object to the "book_objects".


    def remove_book(self, bid):
        """ This method removes book from the library """
        # TODO: implement the method to remove book by its id after listing all the books by list_book function (dont
        #  forget to remove it from the author to books list) and return a string shows the status (deleted/not found)
        # write your code below

        self.example_books.pop(bid)

        for author in self.author_to_books:
            if self.book_objects[bid] in self.author_to_books[author]:
                self.author_to_books[author].pop(self.book_objects[bid])

            else:
                pass

            if self.author_to_books[author] == "":
                self.author_to_books.pop(author)

            else:
                pass
        # ^ Searches for the book in all the authors' book lists and if it finds the book, deletes it. And if an author
        # has no books in their list, it deletes that author.

        self.book_objects.pop(bid)

        if bid in self.borrowed_books:
            self.borrowed_books.pop(bid)

        else:
            pass
        # ^ If the book exists in the "borrowed_books" dictionary, deletes it.


    def list_book(self):
        """ This method lists all the library in the library """
        # TODO: implement the method to list all books and return a string shows that all books have been listed
        # write your code below

        number = 1
        for book in self.example_books:
            Book(book, self.example_books[book][0], str(self.example_books[book][1]), self.example_books[book][2]).\
            display(number)
            number += 1
        # ^ Iterates for every book in "example_books" dictionary. Uses "Book" class' "display()" method to print a
        # single book. And uses "number" to print a number before a single book.


    def search_book(self, search):
        """ This method searches the library for a specific book """
        # TODO: implement the method to search for a book by author name or book name and return a string shows the
        #  status (Matched books/No books)
        # write your code below

        nothing_found = 0
        book_author_amount = 0
        number = 1
        for book_id in self.example_books:
            book_author_amount += 1
            if search == self.example_books[book_id][0]:
                self.book_objects[book_id].display(number)
                number += 1

            else:
                nothing_found += 1
        # ^ Iterates for every book in the library and counts the amount of books. Searches the library for the book.
        # If it finds it, displays it and increases "number", which will be used to print a number before books, by one.

        for author in self.author_to_books:
            book_author_amount += 1
            if search == author:
                for book_object in self.author_to_books[author]:
                    book_object.display(number)
                    number += 1

            else:
                nothing_found += 1
        # ^ Iterates for every author in the library and adds the amount of authors to the amount of the books. Searches
        # the library for the book in authors' book lists. If it finds it, displays it and increases "number", which
        # will be used to print a number before books, by one.

        if nothing_found == book_author_amount:
            print("Nothing found.")

        else:
            pass
        # ^ To understand if anything found, it counts the number of books + authors and the iterations in which nothing
        # is found. If they are equal, it means nothing is found.


    def update_book_copies(self, bid, new_copies):
        """ This method updates the number of copies of a specific book """
        # TODO: implement the method to update the copies number of a book after listing all the books and return a
        #  string shows the status (book updated/no book with this id/new value smaller than the number of students
        #  holding the book)
        # write your code below

        if bid in self.borrowed_books:
            min_copies = 0
            for copy in self.borrowed_books[bid]:
                min_copies += 1

            if new_copies >= min_copies:
                self.example_books[bid][1] = new_copies
                self.book_properties[bid][2] = new_copies
                print("\nThe book has been successfully updated.")

            else:
                print("\nNew amount is less than borrowed copies.")
        # ^ If the book was ever borrowed before, it means we should check if the new amount of copies taken as an input
        # is less than the amount of currently borrowed copies or not.

        else:
            self.example_books[bid][1] = new_copies
            self.book_properties[bid][2] = new_copies
            print("\nThe book has been successfully updated.")
        # ^ If the book was never borrowed before, the admin is free to enter any amount they wish.


    def list_users_borrowed(self, bid):  # < Brand new method to list a book's borrowers.
        if bid in self.borrowed_books:
            print("\nUser(s) holding the book with ID '" + bid + "':")
            for user in self.borrowed_books[bid]:
                print("-" + user)
        # ^ If the book exists in "borrowed_books", it means it is currently borrowed by at lease 1 user. This part
        # prints the users borrowed the book.

        else:
            print("\nInvalid ID or this book currently isn't borrowed by anyone.")


    def add_to_book_list(self, bid, user):  # < Brand new method to add a book to a user's book list.
        if bid in self.borrowed_books:
            copies_in_hold = 0
            for borrower in self.borrowed_books[bid]:
                copies_in_hold += 1
            # ^ Counts the borrowers of the book, if any.

            if copies_in_hold + 1 <= self.book_properties[bid][2]:
                self.borrowed_books[bid].append(user)
                print("\nThe book has been successfully added to your list.")
            # ^ If the amount of copies left in the library is sufficient, the current user borrows the book and is
            # added to "borrowed_books".

            else:
                print("\nUnfortunately there are not enough copies.")

        else:
            self.borrowed_books[bid] = [user]
            print("\nThe book has been successfully added to your list.")
        # ^ If the book currently isn't borrowed by anyone, current user borrows the book and is added to
        # "borrowed_books.


    def remove_from_book_list(self, bid, user):  # < Brand new method to remove a book from a user's book list.
        if bid in self.borrowed_books:
            if user in self.borrowed_books[bid]:
                self.borrowed_books[bid].remove(user)
                if self.borrowed_books[bid] == []:
                    self.borrowed_books.pop(bid)
        # ^ If the book exists in "borrowed_books" and the current user is one of its borrowers, the user is deleted
        # from there. If the book has no borrowers left, it gets deleted, too, from "borrowed_books.

                else:
                    pass

            else:
                print("\nThis book is not in your list.")

        else:
            print("\nBook ID is invalid.")

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class Main:
    """ This class is the main class of the library management system """

    def __init__(self, current_user=None):
        #  TODO: implement the method to initialise the instance level attributes here
        # write your code below

        self.current_user = current_user


    def login(self):
        """ This method deals with the login process """
        # TODO: implement the method to deal with the login attempts by using validate_user function from userDB
        #  instance and printing the required messages. In terms of success attempt, the method should call
        #  show_student_menu or show_admin_menu
        # write your code below

        print(" _      __    __")
        print("| | /| / /__ / /______  __ _  ___ ")
        print("| |/ |/ / -_) / __/ _ \/  ' \/ -_)")
        print("|__/|__/\__/_/\__/\___/_/_/_/\__/")
        print("To the Library Management System")

        print("\nPlease enter your credentials below.")
        while True:
            username = input("\n> Username: ")
            password = input("> Password: ")
            if not UsersDB(True).validate_user(username, password):
                print("\nInvalid username or password.\n")

            else:
                self.current_user = UsersDB(True).validate_user(username, password)
                print("\nYou successfully logged in.")
                if username == "admin":
                    self.show_admin_menu()

                else:
                    self.show_student_menu(username)
            # ^ Checks if the credentials taken as input are valid. If so, equalizes "self.current_user" to the current
            # user's object in "UserDB.user_objects". And then calls the corresponding "Main" method according to the
            # username. If the credentials are invalid, it asks for the credentials again


    def show_admin_menu(self):
        """ This method shows the admin menu and do redirection """
        #  TODO: implement the method to welcome the admin and show the admin menu by using current_user value and do
        #   the redirection to the methods according to the choice with the required implementations
        # write your code below

        log_out = 0
        while log_out < 1:
        # ^ Ths loop iterates until the user wants to log out.
            self.current_user.menu_builder()
            choice = input("\n> Your choice: ")
            if choice == "1":
                print("\n<———List of Books———>\n")
                Library(True).list_book()

            elif choice == "2":
                print("\n<———Adding a Book———>\n")
                bid = input("> Book ID: ")
                if bid not in Library.example_books:
                    name = input("> Book name: ")
                    copies = input("> Number of Copies: ")
                    authors = input("> Author(s) of the Book: ")
                    Library(True).add_book(bid, name, copies, authors)
                    print("\nThe following book has been added to the library.")
                    Book(bid, name, copies, [authors]).display(1)

                else:
                    print("\nThe book ID is not unique.")
            # ^ Asks user for the properties of the new book. Checks the if the ID is unique first. If so, inputting
            # continues. Then it calls the corresponding book. Then it prints the added book.

            elif choice == "3":
                print("\n<———Removing a Book———>\n")
                Library(True).list_book()
                bid = input("\n> Book ID: ")
                if bid in Library.example_books:
                    Library(True).remove_book(bid)
                    print("\nThe book with ID '" + bid + "' has been removed from the library.")

                else:
                    print("\nInvalid ID.")
            # ^ Lists all the books and asks user to choose one. And then checks if the chosen book exists in the
            # library. If so, calls the corresponding method.

            elif choice == "4":
                print("\n<———Searching for a Book———>\n")
                search = str(input("> Book or Author Name: "))
                print()
                Library(True).search_book(search)
            # ^ Searches for the input in books and authors.

            elif choice == "5":
                print("\n<———Changing Copy Amount———>\n")
                bid = input("> Book ID: ")
                if bid in Library.example_books:
                    new_copies = int(input("> New Amount of Copies: "))
                    Library(True).update_book_copies(bid, new_copies)

                else:
                    print("\nInvalid ID.")
            # ^ Asks for a book ID, checks if the book exists, then calls the corresponding method.

            elif choice == "6":
                print("\n<———List Students Borrowed———>\n")
                Library(True).list_book()
                bid = input("\n> Book ID: ")
                Library(True).list_users_borrowed(bid)
            # ^ Lists all the books. Takes an ID as an input. Calls the corresponding method.

            elif choice == "7":
                print("\n<———List of Users———>\n")
                UsersDB(True).list_user()
            # ^ Calls a method to list all the users.

            elif choice == "8":
                print("\n<———Adding a User———>\n")
                nickname = input("> Username: ")
                if nickname not in UsersDB.example_users:
                    passw = input("> Password: ")
                    UsersDB(True).add_user(nickname, passw)

                else:
                    print("\nUsername is not unique.")
            # ^ Takes a username as an input and checks if it already exists. If not, asks for a password. Then calls
            # the corresponding method.

            elif choice == "9":
                print("\n<———Removing a User———>\n")
                UsersDB(True).list_user()
                name = input("\n> Name of the User: ")
                UsersDB(True).remove_user(name)
            # ^ Lists all the users. Asks for a username as an input. Then calls the corresponding method.

            elif choice == "10":
                print("\nYou successfully logged out.")
                log_out += 1
            # ^ Increases the "log_out" by 1 in order to stop the loop and go back to the login screen.

            else:
                print("\nInvalid input")


    def show_student_menu(self, username):
        """ This method shows the student menu and do redirection """
        #  TODO: implement the method to welcome the student and show the admin menu by using current_user value and do
        #   the redirection to the methods according to the choice with the required implementations
        # write your code below

        log_out = 0
        while log_out < 1:
        # ^ Ths loop iterates until the user wants to log out.
            self.current_user.menu_builder()
            choice = input("\n> Your choice: ")

            if choice == "1":
                print("\n<———Searching for a Book———>\n")
                search = str(input("> Book or Author Name: "))
                print()
                Library(True).search_book(search)
            # ^ Searches for the input in books and authors.

            elif choice == "2":
                print("\n<———Adding a Book to Book List———>\n")
                Library(True).list_book()
                bid = input("\nBook ID: ")
                Library(True).add_to_book_list(bid, username)
            # ^ Lists all the books. Takes an ID as an input. Then calls the corresponding method with the obtained
            # parameters.

            elif choice == "3":
                print("\n<———Removing a Book From Book List———>\n")
                borrowed_books = 0
                for (bid, borrower) in Library.borrowed_books.items():
                    if username in borrower:
                        Library(True).book_objects[bid].display(1)
                        borrowed_books += 1

                    else:
                        pass
                # ^ Displays and counts all the books the current user is holding, if there are any.

                if borrowed_books == 0:
                    print("\nYou have no books in your list.")

                else:
                    bid = input("\nBook ID: ")
                    if bid in Library.example_books:
                        if username in Library.borrowed_books[bid]:
                            Library(True).remove_from_book_list(bid, username)

                        else:
                            print("\nThis book is not in your list.")

                    else:
                        print("\nInvalid ID.")
                # ^ If there are any books the current user is holding, takes an ID as an input and checks if it exists
                # in the library. If so, then checks if the user is one of the book's borrowers. If so, calls the
                # corresponding method to delete the book from the current user's book list.

            elif choice == "4":
                print("\n<———Your Book List———>\n")
                borrowed_books = 0
                for (bid, borrower) in Library.borrowed_books.items():
                    if username in borrower:
                        Library(True).book_objects[bid].display(1)
                        borrowed_books += 1

                    else:
                        pass
                # ^ Calls the objects of the all books the current user has borrowed. And counts them.

                if borrowed_books == 0:
                    print("You have no borrowed books.")
                # ^ If no books are currently borrowed by the user.

                else:
                    pass


            elif choice == "5":
                print("\nYou successfully logged out.")
                log_out += 1
            # ^ Increases the "log_out" by 1 in order to stop the loop and go back to the login screen.

            else:
                print("\nInvalid input")

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

if __name__ == '__main__':
    main = Main()
    main.login()

# —————————————————————
# Hasan Tarık Yumbul  |
# ID: 219171247       |
# —————————————————————
