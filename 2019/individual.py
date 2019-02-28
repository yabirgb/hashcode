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
        self.score = 0

        self.oriented = {
            'V': [x for x in slides if x.is_vertical]
        }

    