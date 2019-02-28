class Slide:

    """
    Combination of images represented as a slide

    List of attributes:

    - photos:list = list of photos the second being None if is a horizontal pic
    - is_vertical:bool = True if the slide is composed by two vertical images
    - tags:set = set being the union of both set of images


    """

    def __init__(self, photo1, photo2 = None):

        """
        photo1: Photo
        photo2: Photo (only if we have two vertical photos)
        """

        # Check that the photo is vertical
        assert(photo2.is_vertical)

        # List of the photos
        self.photos = [photo1, photo2]

        
        self.is_vertical = photo1 and photo2
    
    @property
    def tags(self):
        
        result = set()

        for photo in self.photos:
            result.union(photo.tags)

        return result