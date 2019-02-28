from shuffle import shuffle
from individual import individual
from slide import slide

class Evolution:
	def __init__(self, population_size, photos):
		self.photos = photos
		self.population = self.initializePopulation(population_size)
	
	def initialize_population(self, population_size):
		self.population = []
		for i in range(population_size):
			self.population.append(self.random_indv())

	def random_indv():
		shuffled_photos = shuffle(self.photos)
		slides = []
		unpaired_photo = None
		for photo in shuffled_photos:
			if photo.is_vertical:
				if unpaired_photo:
					unpaired_photo = photo
				else:
					slides.append(slide(photo, unpaired_photo))
			else:
				slides.append(photo)

		return individual(slides)
