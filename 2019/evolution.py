from shuffle import shuffle
from Individual import individual
from Slide import slide

class Evolution:
	def __init__(self, population_size, photos):
		self.photos = photos
		self.population = self.initializePopulation(population_size)
	
	def init_params(self, vertical_mutation_percentage, random_mutation_percentage, child_percentage):
		self.v_m_percent = vertical_mutation_percentage
		self.r_m_percent = random_mutation_percentage
		self.child_percent = child_percentage


	def initialize_population(self, population_size):
		self.population = []
		for i in range(population_size):
			self.population.append(self.random_indv())

	def random_indv(self):
		shuffled_photos = shuffle(self.photos)
		slides = []
		unpaired_photo = None
		for photo in shuffled_photos:
			if photo.is_vertical:
				if unpaired_photo:
					unpaired_photo = photo
				else:
					slides.append(Slide(photo, unpaired_photo))
			else:
				slides.append(photo)

		return Individual(slides)

	def runGeneration(self):
		assert self.child_percent, "Call init_params"
		parents = self.selection()
		children = self.cross(parents)
		self.random_mutation(children)
		self.vertical_mutation(children)
		population = self.replacement(children, len(population))

	def replacement(self, offspring, total_pop):
		return sorted((self.population + offspring), key=lambda a: a.total_score, reverse=False)[:total_pop]

