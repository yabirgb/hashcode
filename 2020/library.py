class Library:

    def __init__(self, books: List[int], days:int, per_day:int, id_:int):

        self.books = list(books)
        self.registration = days
        self.per_day = per_day
        self.id_ = id_

    def __str__(self):
        return f'Library with id {self.id_} has {len(self.books)} books. {self.per_day} books per day. Registration of {self.registration}'
        

    def heuristic(self, remaining, scores, scanned):

        b=min((remaining-self.registration)*self.per_day, len(self.books))

        own_scores = [scores[i]*scanned[i] for i in self.books]
        
        aux = zip(self.books, own_scores)

        aux = sorted(aux, key=lambda x:x[1])

        h = 0

        books_to_scan=[]

        for i in range(0, b):
            h+=aux[i][1]
            books_to_scan+=aux[i][0]

        return h, books_to_scan