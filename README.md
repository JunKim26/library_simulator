# Library_Simulator


There are 3 classes: LibraryItem, Patron and Library classes, and the three other classes that inherit from LibraryItem (Book, Album and Movie).  All data members of each class are marked as *private*.

Here are descriptions of the three classes:

**LibraryItem:**
* library_item_id - a unique identifier for a LibraryItem - you can assume uniqueness, you don't have to enforce it
* title
* location - a LibraryItem can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
* checked_out_by - refers to the Patron who has it checked out (if any)
* requested_by - refers to the Patron who has requested it (if any); a LibraryItem can only be requested by one Patron at a time
* date_checked_out - when a LibraryItem is checked out
* init method
* get_location returns the Library Item's location
 
**Book/Album/Movie:**
* These three classes all inherit from LibraryItem.
* All three has a method called get_check_out_length that returns the number of days that type of library item may be checked out for.  For a Book it's 21 days, for an Album it's 14 days, and for a Movie it's 7 days.
* All three will have an additional field.  For Book, it's a string field called author.  For Album, it's a string field called artist.  For Movie, it's a string field called director.  There will also need to be get methods to return the values of these fields.
 
**Patron:**
* patron_id - a unique identifier for a Patron
* name 
* checked_out_items - a collection of LibraryItems that a Patron currently has checked out
* fine_amount - how much the Patron owes the Library in late fines (measured in dollars); this is allowed to go negative
* init method - takes a patron ID and name
* get_fine_amount - returns the fine_amount
* add_library_item - adds the specified LibraryItem to checked_out_items
* remove_library_item - removes the specified LibraryItem from checked_out_items
* amend_fine - a positive argument increases the fine_amount, a negative one decreases it; this is allowed to go negative
 
**Library:**
* holdings - a collection of the LibraryItems that belong to the Library
* members - a collection of the Patrons who are members of the Library
* current_date - stores the current date represented as an integer number of "days" since the Library object was created
* an init method that initializes the current_date to zero
* add_library_item - takes a LibraryItem object as a parameter and adds it to the holdings
* add_patron - takes a Patron object as a parameter and adds it to the members
* get_library_item_from_id - returns the LibraryItem object corresponding to the ID parameter, or None if no such LibraryItem is in the holdings
* get_patron_from_id - returns the Patron object corresponding to the ID parameter, or None if no such Patron is a member
* check_out_library_item
* return_library_item
* request_library_item
* pay_fine
* increment_current_date
 
Note - a LibraryItem can be on request without its location being the hold shelf (if another Patron has it checked out);
