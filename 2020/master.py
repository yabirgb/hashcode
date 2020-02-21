from typing import List
from library import Library
import logging

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

        #self.i = int(len(self.libraries)/2)
        self.i = 0
        self.total = set()

        self.libraries.sort(key = lambda x:len(set(x.books)-self.total))
        
    @property
    def remaining_days(self) ->int:
        return self.total_days-self.current_day

    def advance_days(self, number_of_days:int=1) -> int:
        self.current_day += number_of_days
        return self.remaining_days

    def step_d(self):


        # decide wich libraries to activate in this step

        if self.next_available_day == self.current_day:
            
            if self.currently_activating != None:
                for book in self.libraries[self.currently_activating].books_to_scan:
                    self.scanned[book] = 0
                    
                self.active.append(self.currently_activating)
            
            best_score, best_lib = 0, self.i
            self.i += 1

            if best_lib != None and self.i < len(self.libraries):
                self.currently_activating = best_lib
                self.next_available_day += self.libraries[best_lib].registration

                self.libraries[best_lib].compute_books_to_scan(
                    self.remaining_days,
                    self.scores,
                    self.scanned)

        
        # decide the books to register this step for each librarie active
        # store the books scanned today
        # step


        return self.advance_days(1)


    def step(self):

        # decide wich libraries to activate in this step

        if self.next_available_day == self.current_day:
            
            if self.currently_activating != None:
                for book in self.libraries[self.currently_activating].books_to_scan:
                    self.scanned[book] = 0
                    
                self.active.append(self.currently_activating)
            
            best_score, best_lib = 0, None
            
            for lib in self.libraries:
                # library is currently not activated
                if lib.id_ not in self.active:
                    s = lib.heuristic4(self.remaining_days,
                                      self.scores,
                                      self.scanned)

                    if s > best_score:
                        best_score = s
                        best_lib = lib.id_

            if best_lib != None:
                self.currently_activating = best_lib
                self.next_available_day += self.libraries[best_lib].registration

                self.libraries[best_lib].compute_books_to_scan(
                    self.remaining_days,
                    self.scores,
                    self.scanned)

        
        # decide the books to register this step for each librarie active
        # store the books scanned today
        # step

        logging.info(self.remaining_days)
        return self.advance_days(1)

        
    def format_output(self):

        nlib = len(self.active)
        lib_books = []
        
        for lib in self.active:
            l = self.libraries[lib]
            lib_books.append((l.id_, l.books_to_scan))

        return nlib, lib_books
            

