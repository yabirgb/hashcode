class Individual:

    """
    Representation of a individual inside a generation.
    
    slides:list = List of slides of the individual
    scores:list = List of the scores between consecutive elements
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
        self.scores = list()
        self.total_score = 0

        for i in range(len(slides)-1):
            s=score(i)
            self.scores.append(s)
            self.total_score+=s

        self.oriented = {
            'V': [x for x in slides if x.is_vertical]
        }

    def score(self, i): # score slide i, i+1

        assert(0 <= i and i < len(self.slides)-1)

        tags1=self.slides[i].tags
        tags2=self.slides[i+1].tags
        
        return min(len(tags1&tags2), len(tags1-tags2), len(tags2-tags1))

    
