class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.checked_out = False

    def __str__(self):
        if self.checked_out:
            return f"{self.title} by {self.author} ({self.year_published}) - Checked out"
        else:
            return f"{self.title} by {self.author} ({self.year_published}) - Available"
    
    def check_out(self):
        self.checked_out = True
    
    def return_book(self):
        self.checked_out = False