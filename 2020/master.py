from typing import List
from library import Library

class Master:

    def __init__(self, total_days:int, scores:int, libraries:List[Library]):

        self.current_day = 0
        self.total_days = total_days
        self.scores = scores
        self.libraries = libraries
        self.planning_today = []

        # active libraries in the system
        self.active = []

        # 0 is scanned
        self.scanned = [1 for s in scores]

        # next available day for activation
        self.next_available_day = 0
        self.currently_activating = None

    @property
    def remaining_days(self) ->int:
        return total_days-current_day

    def advance_days(self, number_of_days:int=1) -> int:
        self.current_day += number_of_days
        return self.remaining_days

    def step(self):

        # decide wich libraries to activate in this step

        if self.next_available_day == self.current_day:
            
            if self.currently_activating != None:
                for book in self.libraries[self.currently_activating].books_to_scan:
                    self.scanned[book] = 0
                    
                self.active.append(self.currently_activating)
            
            best_score, best_lib = 0, None
            
            for lib in libraries:
                # library is currently not activated
                if lib.id_ not in self.active:
                    s = lib.heuristic(self.remaining_days,
                                      self.scores,
                                      self.scanned)

                    if s > best_score:
                        best_score = s
                        best_lib = lib.id_
            self.currently_activating = best_lib
            self.next_available_day += self.libraries[best_lib].registration
        
        # decide the books to register this step for each librarie active
        # store the books scanned today
        # step

        self.advance_days(1)

    def format_output(self):

        nlib = sum([1 for x in self.active if x == True])
        lib_books = []
        
        for lib in self.active:
            l = self.libraries[lib]
            lib_books.append((l.id_, l.books_to_scan))

        return nlib, lib_books
            

