from random import randint
from slide import Slide

# shuffles a list
def Shuffle(l1):
    l=list(l1)
    for k in range(len(l)):
        i = randint(k, len(l)-1)
        l[k], l[i] = l[i], l[k]

    return l


def order_crossover(gen1, gen2, child1, child2, rt=None, rb=None):

    """
    Generates two childre from the parents provided using
    Order Cross 
    """

    # len(gen) = n
    # we need up to n-1
    # and we discard the last two
    # randint is include a <= x <= b

    size = len(gen)

    rand_top = rt or randint(3, size-3)
    rand_botton = rb or randint(0, rand_top-1)

    # set of 
    used1 = set()
    used2 = set()
    
    for i in range(rand_botton, rand_top+1):
        sld1 = gen1.slides[i]
        sld2 = get2.slides[i]

        child1.append(sld1)
        child2.append(sld2)

        used1.add(sld1.pk)
        used2.add(sld2.pk)

    lower_limit = (rand_top + 1) % size
    top_limit = rand_top
    
    pos = lower_limit

    while pos != top_limit:

        pos = (pos + 1) % size 

        if gen2.slides[pos].pk not in used1:
            child1.append(gen2.slides[pos])
            used1.add(gen2.slides[pos].pk)

        if gen1.slides[pos].pk not in used2:
            child2.append(gen1.slides[pos])
            used2.add(gen1.slides[pos].pk)

    if gen2.slides[rand_top].pk not in used1:
        child1.append(gen2.slides[rand_top])
    if gen1.slides[rand_top].pk not in used2:
        child2.append(gen1.slides[rand_top]) 

    return Slide(child1), Slide(child2)    