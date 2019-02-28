
class Photo:

    def __init__(self, pk, orientation, tags):
        
        self.pk=pk
        self.is_vertical=orientation=='V'
        self.tags=tags
