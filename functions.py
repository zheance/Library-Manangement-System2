#This is the Main Library. It's a list containing dictionaries.
#Im planning on making 2 more lists for "AVAILABLE" and "ISSUED" categories
import time
book_list = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "available": False},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "available": True},
    {"title": "The Diary of a Young Girl", "author": "Anne Frank", "available": False}
]

def display_menu():
    print("------------------------")
    print("Library Management System")
    print("------------------------")
    print("1. Display all books")
    print("2. Display all available books")
    print("3. Display all issued books")
    print("4. Search for a book")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Add book(s) info")
    print("8. Delete book(s) info ")
    print("9. Exit")
    choice = int(input("Enter your choice (1-5): "))
    return choice
    #it'll assign the value to the variable if call the func using a variable
    #pretty cool trick if you ask me eh?

def display_all_books():

    print("\nAll Books:")
    print("-----------------------------")
    for index, book in enumerate(book_list):
        #enumerate func makes the loop value go in 2
        #"index" is getting "0,1,2..." and "book" is getting the items in book_list
        availability = "Available" if book["available"] else "Not Available"
        print(f"{index + 1}. {book['title']} by {book['author']} ({availability})")
    print("-----------------------------")

def search_for_book():
    title = input("Enter the title of the book you want to search for: ")
    for book in book_list:
        if book["title"].lower() == title.lower():
            availability = "Available" if book["available"] else "Not Available"
            print(f"{book['title']} by {book['author']} ({availability})")
            break
    else:
        print(f"No book was found with the title '{title}'.")

def borrow_book():
    title = input("Enter the title of the book you want to borrow: ")
    for book in book_list:
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            print(f"You have successfully borrowed '{book['title']}'.")
            break
    else:
        print(f"The book '{title}' is not available for borrowing.")

def return_book():
    title = input("Enter the title of the book you want to return: ")
    for book in book_list:
        if book["title"].lower() == title.lower() and not book["available"]:
            book["available"] = True
            print(f"You have successfully returned '{book['title']}'.")
            break
    else:
        print(f"No book was found with the title '{title}'.")

def addbook():
    no = int(input("Enter How many Books you want to Add : "))
    for i in range(no):
        x = {"title": "", "author": "", "available": True}
        x["title"] = input("Enter Title : ")
        x["author"] = input("Enter Author's Name : ")
        book_list.append(x)
        print(x["title"],"By",x["author"],"was added to the list")
        print("-----------------------------")

def delete_book():
    no = int(input("How many Book Info You Want To Delete? : "))
    for i in range(no):
        title = input("Enter the title of the book you want to delete: ")
        c = 0
        for book in book_list:
            time.sleep(6)
            if book["title"].lower() == title.lower():
                del book_list[c]
                print("----")
                print(title,"was Deleted From Library")
                print("----")
                break
            c += 1
        else:
            print(f"No book was found with the title '{title}'.")

def availbooks():
    print("-----------------------------")
    for book in book_list:
        if book["available"]is True:
            print(f"{book['title']} by {book['author']}")
    else:
        print(f"No available books in lib info")
    print("-----------------------------")

def issuedbooks():
    print("-----------------------------")
    for book in book_list:
        if book["available"]is False:
            print(f"{book['title']} by {book['author']}")
    else:
        print("No Issued Books in Lib Info")
    print("-----------------------------")


# main program
def mainpy():
    while True:
        choice = display_menu()
        if choice == 1:
            display_all_books()
            time.sleep(3)
        elif choice == 2:
            availbooks()
            time.sleep(3)
        elif choice == 3:
            issuedbooks()
            time.sleep(3)
        elif choice == 4:
            search_for_book()
            time.sleep(2)
        elif choice == 5:
            borrow_book()
            time.sleep(2)
        elif choice == 6:
            return_book()
            time.sleep(2)
        elif choice == 7:
            addbook()
            time.sleep(2)
        elif choice == 8:
            delete_book()
            time.sleep(2)
        elif choice == 9:
            print("Logging You Out...")
            break
        else:
            print("Invalid choice. Try again.")

