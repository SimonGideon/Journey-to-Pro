class P:
    def __init__(self, title, author):
        self.title = title
        self.setAuthor(author)
    def get_author(self):
        return self.author
    def set_author(self, author):
        if not author:
            self.author = "Unknown"
        else:
            self.author = author

book = P(title="Ancient Manuscript", author="Some Guy")
print(book.author = "")