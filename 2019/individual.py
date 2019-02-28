from random import randint
from slide import Slide

class Individual:

    """
    Representation of a individual inside a generation.
    
    slides:list = List of slides of the individual
    score:int = Total score of the individual
    oriented:dict = Dictionary with to keys ('H', 'V') having
                    'V' a reference to a list of vertical slides 
    """

    def __init__(self, slides):

        """
        slides:list[Slide]
        """

        assert(slides)

        self.slides = slides
        self.total_score = 0

        for i in range(len(self.slides)-1):
            self.total_score+= self.score(i)

        self.vertical = [i for i, x in enumerate(self.slides) if x.is_vertical]

    def score(self, i): # score slide i, i+1

        assert(0 <= i and i < len(self.slides)-1)

        tags1=self.slides[i].tags
        tags2=self.slides[i+1].tags
        
        return min(len(tags1&tags2), len(tags1-tags2), len(tags2-tags1))

    def mutate_vertical(self):

        i = randint(0, len(self.vertical)-1)
        j = -1
        while j != i:
            j = randint(0, len(self.vertical)-1)

        if i > 0:
            self.total_score -= self.score(i-1)

        if i < len(slides)-1:
            self.total_score -= self.score(i)

        if j > 0 and j != i+1:
            self.total_score -= self.score(j-1)

        if j < len(slides)-1 and j != i-1:
            self.total_score -= self.score(j)

        photo1, photo2 = list(self.slides[i].photos)
        photo3, photo4 = list(self.slides[j].photos)
        
        self.slides[i] = Slide(photo1, photo3)
        self.slides[j] = Slide(photo2, photo4)

        if i > 0:
            self.total_score += self.score(i-1)

        if i < len(slides)-1:
            self.total_score += self.score(i)
            
        if j > 0 and j != i+1:
            self.total_score += self.score(j-1)

        if j < len(slides)-1 and j != i-1:
            self.total_score += self.score(j)


    def random_mutate(self):
        
        i = random(0, len(self.slides)-3)
        j = random(i+2, len(self.slides)-1)

        self.total_score -= self.score(i)
        self.total_score -= self.score(j-1)
        if j < len(self.slides)-1:
            self.total_score -= self.score(j)

        s = Slide(self.slides[j].photo1, self.slides[j].photo2)

        
        for k in range(j-1, i, -1):
            self.slides[k+1]=self.slides[k]
            
        self.slides[i+1]=s
        
        self.total_score += self.score(i)
        self.total_score += self.score(i+1)
        if j < len(self.slides)-1:
            self.total_score += self.score(j)

        self.vertical = [i for i, x in enumerate(self.slides) if x.is_vertical]
