class Library:

    def __init__(self, books: List[int], days:int, per_day:int, id_:int):

        self.books = list(books)
        self.scanned = []
        self.registration = days
        self.per_day = per_day
        self.id_ = id_

    def __str__(self):
        return f'Library with id {self.id_} has {len(self.books)} books. {self.per_day} books per day. Registration of {self.registration}'
        
