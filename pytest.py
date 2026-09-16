class book:
    def __init__(self , title ,author):
        self.title = title
        self.author = author
        self.is_bowrrowed = False

    def borrow(self):
        if self.is_bowrrowed:
            print(f"sorry,'{self.title}'is already bowwrrowd")
        else:
            self.is_bowrrowed = True
            print(f"Success:")