# Lijst om boeken op te slaan
books = []

def add_book(title, author, year):
    book = {"title": title, "author": author, "year": year}
    books.append(book)

def view_books():
    for i, book in enumerate(books):
        print(f"ID: {i}, Titel: {book['title']}, Auteur: {book['author']}, Jaar: {book['year']}")

def update_book(book_id, title, author, year):
    if 0 <= book_id < len(books):
        books[book_id] = {"title": title, "author": author, "year": year}
        print("Boek bijgewerkt!")
    else:
        print("Ongeldige ID")

def delete_book(book_id):
    if 0 <= book_id < len(books):
        books.pop(book_id)
        print("Boek verwijderd!")
    else:
        print("Ongeldige ID")

def main():
    while True:
        print("\nBoekbeheer Systeem")
        print("1. Boek Toevoegen")
        print("2. Boeken Bekijken")
        print("3. Boek Bijwerken")
        print("4. Boek Verwijderen")
        print("5. Afsluiten")

        keuze = input("Kies een optie: ")

        if keuze == '1':
            title = input("Titel: ")
            author = input("Auteur: ")
            year = input("Publicatiejaar: ")
            add_book(title, author, year)
            print("Boek toegevoegd!")
        elif keuze == '2':
            view_books()
        elif keuze == '3':
            book_id = int(input("ID van het boek: "))
            title = input("Nieuwe Titel: ")
            author = input("Nieuwe Auteur: ")
            year = input("Nieuw Publicatiejaar: ")
            update_book(book_id, title, author, year)
        elif keuze == '4':
            book_id = int(input("ID van het boek: "))
            delete_book(book_id)
        elif keuze == '5':
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()
