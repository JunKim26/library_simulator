# Author: Jun Kim
# Date:04/15/2020
# Description: Program of a simulation of a library involving multiple classes.


# define class LibraryItem
class LibraryItem:
    """Represents private values of a Library item object"""

    def __init__(self, library_item_id, title):
        """initialize the library item using library item ID and Title as parameters"""

        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = 0

    def set_library_item_id(self,id):
        """sets the library item id"""
        self._library_item_id = id

    def set_title(self,title):
        """sets the title"""
        self._title = title

    def set_location(self,location):
        """sets the location"""
        self._location = location

    def set_checked_out_by(self,patron):
        """sets the checked out date"""
        self._checked_out_by = patron

    def set_requested_by(self,patron):
        """sets the requested_by"""
        self._requested_by = patron

    def set_date_checked_out(self,day):
        """sets the date checked out"""
        self._date_checked_out = day

    def get_library_item_id(self):
        """Returns the library item id"""
        return self._library_item_id

    def get_title(self):
        """Returns the title"""
        return self._title

    def get_location(self):
        """Returns the location"""
        return self._location

    def get_checked_out_by(self):
        """Returns the patron who checked out item"""
        return self._checked_out_by

    def get_requested_by(self):
        """Returns the patron that is requesting the item"""
        return self._requested_by

    def get_date_checked_out(self):
        """Returns the date checked out"""
        return self._date_checked_out



# define class Book/Album/Movie inheriting from Library Item class
class Book(LibraryItem):
    """Represents private values of a book object, inherits from LibraryItem"""

    def __init__(self, library_item_id, title,author):
        """initialize the book item using library inheritence"""

        super().__init__(library_item_id,title)
        self._author = author

    def get_author(self):
        """Returns author"""
        return self._author

    def get_check_out_length(self):
        """Returns check out length"""
        return 21


class Album(LibraryItem):
    """Represents private values of an album object, inherits from LibraryItem"""

    def __init__(self, library_item_id,title,artist):
        """initialize the book item using library inheritence"""

        super().__init__(library_item_id,title)
        self._artist = artist

    def get_artist(self):
        """Returns artist"""
        return self._artist

    def get_check_out_length(self):
        """Returns check out length"""
        return 14

class Movie(LibraryItem):
    """Represents private values of a movie object, inherits from LibraryItem"""

    def __init__(self, library_item_id, title,director):
        """initialize the book item using library inheritence"""

        super().__init__(library_item_id,title)
        self._director = director

    def get_director(self):
        """Returns director"""
        return self._director

    def get_check_out_length(self):
        """Returns check out length"""
        return 7

# define class Patron
class Patron:
    """Represents private values of a patron object"""

    def __init__(self, patron_id, name):
        """initialize the library item using library item ID and Title as parameters"""

        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        """Returns fine amount"""
        return self._fine_amount

    def get_name(self):
        """Returns name"""
        return self._name

    def get_patron_id(self):
        """Returns patron_id"""
        return self._patron_id

    def add_checked_out_items(self,item):
        """sets checked_out_items"""
        self._checked_out_items.append(item)

    def get_checked_out_items(self):
        """Returns checked_out_items"""
        return self._checked_out_items

    def amend_fine(self,dollar):
        """amends fine by dollar amount"""
        self._fine_amount += dollar

    def add_library_item(self,item):
        """Adds library item to checked out list"""
        self._checked_out_items.append(item)

    def remove_library_item(self,item):
        """Removes library item from checked out list"""
        self._checked_out_items.remove(item)

# define class Library
class Library:
    """Represents a Library, which has collections of Library items and patrons. """

    def __init__(self):
        """initializes the Library holdings and members"""

        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_holdings(self):
        """Returns holdings list"""
        return self._holdings

    def get_members(self):
        """Returns members list"""
        return self._members

    def get_current_date(self):
        """Returns current date"""
        return self._current_date


    def add_library_item(self,libraryitem):
        """Adds library item into holdings list"""

        self._holdings.append(libraryitem)

    def add_patron(self, patron):
        """Adds patron into members list"""

        self._members.append(patron)

    def get_library_item_from_id(self,id):
        """Retrieves library item given id parameter"""

        for object in self._holdings:                               #cycles through every object in holdings list, if a match is made, return object

            if id == object.get_library_item_id():
                return object

        list_of_ids = []

        for object in self._holdings:                               #creating a list of ids to check if id does not match an object in holdings list
            list_of_ids.append(id)

        if id not in list_of_ids:
            return None

    def get_patron_from_id(self,id):
        """Retrieves patron item given id parameter"""

        for object in self._members:                                # cycles through every object in members list, if a match is made, return object

            if id == object.get_patron_id():
                return object

        list_of_members = []

        for object in self._members:                                # creating a list of members to check if id does not match an object in holdings list
            list_of_members.append(id)

        if id not in list_of_members:
            return None


    def check_out_library_item(self,patronID,itemID):
        """updates Patron's checked out items if itemID and patronID are valid and available"""

                                                                    #conditions for if the library item is not able to be checked out for various reasons

        item = self.get_library_item_from_id(itemID)
        patron = self.get_patron_from_id(patronID)

        if patron not in self._members:
            return "patron not found"

        if item not in self._holdings:
            return "item not found"

        if item.get_location() == "CHECKED_OUT":
            return "item already checked out"

        if item.get_location() == "ON_HOLD_SHELF":
            if patron != item.get_requested_by():
                return "item on hold by other patron"

            else:
                pass

                                                                    #If the library item is able to be checked out...

                                                                    # If the patron is someone who requested the item, then clear the patron's request for the item

        item.set_checked_out_by(patron)

        item.set_date_checked_out(self._current_date)

        item.set_location("CHECKED_OUT")

        patron.add_checked_out_items(item)

        return "check out successful"


    def return_library_item(self,itemID):
        """Returning a library item"""

        libraryitem = self.get_library_item_from_id(itemID)

        if libraryitem not in self._holdings:                       #if item is not in holdings list

            return "item not found"

        if libraryitem.get_location() != "CHECKED_OUT":

            return "item already in library"

                                                                    # update the Patron's checked_out_items by using Library item ID

        for patron in self._members:                                # find out which member checked out the library item

            if libraryitem in patron.get_checked_out_items():

                patron.remove_library_item(libraryitem)

        if libraryitem.get_requested_by() != None:                  # If item is requested put on hold shelf

            libraryitem.set_location("ON_HOLD_SHELF")

        else:                                                       #If item is not requested put on shelf

            libraryitem.set_location("ON_SHELF")

        libraryitem.set_checked_out_by(None)

        return "return successful"

    def request_library_item(self,patronID,itemID):
        """Requesting library item given patron and library item ID"""

        libraryitem = self.get_library_item_from_id(itemID)
        patron = self.get_patron_from_id(patronID)

        if patron not in self._members:
            return "patron not found"

        if libraryitem not in self._holdings:
            return "item not found"

        if libraryitem.get_requested_by() != None:
            return "item already on hold"

        libraryitem.set_requested_by(patron)                        # update item requested by status

        if libraryitem.get_location() == "ON_SHELF":
            libraryitem.set_location("ON_HOLD_SHELF")

        return "request successful"

    def pay_fine(self,patronID,dollars):                            # patron is paying the fine with dollar amount as parameter
        """amends the fine by reducing the fine on account by dollar amount"""

        patron = self.get_patron_from_id(patronID)

        if patron not in self._members:
            return "patron not found"

        patron.amend_fine(-dollars)

        return "payment successful"

    def increment_current_date(self):                               # charge patrons fine for overdue items
        """increase each Patron's fines by 10 cents for each overdue LibraryItem checked out"""

        self._current_date += 1

                                                                                 # for loop for every member
        for patron in self._members:                                             # for each patron, a for loop for their checked_out_list to check each item

            for item in patron.get_checked_out_items():                          #checks each item in patron's checked out list

                days_borrowed = self._current_date - item.get_date_checked_out() # how many each item was borrowed
                if days_borrowed > item.get_check_out_length():

                    patron.amend_fine(0.10)                                      # adds 10 cents to fine per item



#Example Usage
b1 = Book("345", "Phantom Tollbooth", "Juster")
a1 = Album("456", "...And His Orchestra", "The Fastbacks")
m1 = Movie("567", "Laputa", "Miyazaki")

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(a1)
lib.add_library_item(m1)
lib.add_patron(p1)
lib.add_patron(p2)

print(lib.request_library_item("abc", "456"))
print(a1.get_location())
print(lib.check_out_library_item("bcd", "456"))
print(lib.check_out_library_item("abc", "456"))
print(a1.get_location())


for i in range(57):
    lib.increment_current_date()  # 57 days pass

p1_fine = p1.get_fine_amount()
print(p1_fine)
print(lib.pay_fine("bcd", p1_fine))
print(lib.return_library_item("456"))
