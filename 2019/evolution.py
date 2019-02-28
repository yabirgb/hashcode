from random import sample

from shuffle import order_crossover
from shuffle import shuffle
from Individual import individual
from Slide import slide

class Evolution:
	def __init__(self, population_size, photos):
		self.photos = photos
		self.population = sorted(self.initializePopulation(population_size), key=lambda a: a.total_score, reverse=True)
		self.best_ever = self.population[0]
		 
	
	def init_params(self, vertical_mutation_percentage, random_mutation_percentage, parent_percentage):
		self.v_m_percent = vertical_mutation_percentage
		self.r_m_percent = random_mutation_percentage
		self.parent_percent = child_percentage


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

	def run_generation(self):
		assert self.parent_percent, "Call init_params"
		parents = self.selection()
		children = self.cross(parents)
		self.random_mutation(children)
		self.vertical_mutation(children)
		population = self.replacement(children, len(population))
		self.best_ever = self.population[0]

	def replacement(self, offspring, total_pop):
		return sorted((self.population + offspring), key=lambda a: a.total_score, reverse=True)[:total_pop]

	def random_mutation(self, offspring):
		n_mut = int(self.r_m_percent * len(offspring))
		chosen = sample(offspring, n_mut)
		for indv in chosen:
			indv.mutate_random()

	def vertical_mutation(self, offspring):
		n_mut = int(self.v_m_percent * len(offspring))
		chosen = sample(offspring, n_mut)
		for indv in chosen:
			indv.mutate_vertical()

	def selection(self):
        parents = []
        n_parents = int(len(self.population) * self.parent_percent * 2)
        for i in range(n_parents):
            candidate_1, candidate_2 = sample(self.population, 2)
            parents.append(min(candidate_1, candidate_2, key=lambda x: x.total_score))
        return parents

    def cross(self, parents):
    	children = []
    	for i in range(0, len(parents), 2):
    		child1, child2 = order_crossover(parents[i], parents[i+1])
    		children.append(child1)
    		children.append(child2)

    	return children

    def best_ever(self):
    	return self.best_ever