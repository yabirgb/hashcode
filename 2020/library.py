class Library:

    def __init__(self, books: List[int], days:int, per_day:int, id_:int):

        self.books = list(books)
        self.registration = days
        self.per_day = per_day
        self.id_ = id_

    def __str__(self):
        return f'Library with id {self.id_} has {len(self.books)} books. {self.per_day} books per day. Registration of {self.registration}'
        

    def heuristic(self, remaining, scores, scanned):

        b=(remaining-self.registration)*self.per_day

        own_scores = [scores[i]*scanned[i] for i in self.books]
        own_scores.sort(reverse=True)

        h = 0

        for i in range(0, b):
            h+=own_scores[i]

        return h