class Library:

    def __init__(self, books: int, days:int, per_day:int, id_:int):

        self.books = list(books)
        self.registration = days
        self.per_day = per_day
        self.id_ = id_

        self.n = len(self.books)

        self.books_to_scan=[]

    def __str__(self):
        return f'Library with id {self.id_} has {len(self.books)} books. {self.per_day} books per day. Registration of {self.registration}'
        

    def heuristic(self, remaining, scores, scanned):
        b=min((remaining-self.registration)*self.per_day, self.n)

        own_scores = [scores[i]*scanned[i] for i in self.books]
        own_scores.sort(reverse=True)

        return sum (own_scores[:b])/self.registration**2

    def heuristic2(self, remaining, score, scanned):
        
        return min((remaining-self.registration)*self.per_day, self.n)/self.registration**2

    def heuristic3(self, remaining, score, scanned):
        
        return min((remaining-self.registration)**2 * self.per_day, self.n)/self.registration

    def heuristic4(self, remaining, score, scanned):
        
        return 1/self.registration

    def compute_books_to_scan(self, remaining, scores, scanned):

        b=min((remaining-self.registration)*self.per_day, self.n)

        own_scores = [scores[i]*scanned[i] for i in self.books]
        
        aux = zip(self.books, own_scores)

        aux = sorted(aux, key=lambda x:-x[1])


        self.books_to_scan=[]

        for i in range(0, b):
            self.books_to_scan.append(aux[i][0])
