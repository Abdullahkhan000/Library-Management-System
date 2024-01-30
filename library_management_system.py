class Library:
    def __init__(self):
        self.books = []
        self.number_of_books = 0
        self.load_books()

    def load_books(self):
        try:
            with open("library.txt", 'r') as f:
                lines = f.readlines()
                for line in lines[:-1]:
                    _, book_info = line.split(":", 1)
                    self.books.append(book_info.strip())
                self.number_of_books = int(lines[-1].split()[-1]) if lines else 0
        except FileNotFoundError:
            # File doesn't exist yet
            pass

    def add_new_books(self, b):
        self.books.append(b)
        self.number_of_books = len(self.books)
        self.save_books()

    def save_books(self):
        with open("library.txt", 'w') as f:
            for i, book in enumerate(self.books, start=1):
                ordinal_suffix = "th" if 11 <= i <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(i % 10, "th")
                f.write(f"The {i}{ordinal_suffix} book is: {book}\n")
            f.write(f"The Total Number Of Books are {self.number_of_books}\n")

    def total_books(self):
        for i, book in enumerate(self.books, start=1):
            ordinal_suffix = "th" if 11 <= i <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(i % 10, "th")
            print(f"The {i}{ordinal_suffix} book is: {book}")

q = Library()

while True:
    new_book = input("Enter the name of a new book (or type 'stop' to finish the code): ")
    if new_book.lower() == 'stop':
        break
    q.add_new_books(new_book)

q.total_books()

print(f"The Total Number Of Books Which Are Presented In This Libraray Is {q.number_of_books}")