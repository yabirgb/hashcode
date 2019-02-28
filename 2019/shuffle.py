from random import randint

# shuffles a list
def shuffle(l):

    for k in range(len(l)):
        i = randint(k, len(l)-1)
        l[k], l[i] = l[i], l[k]

    return l
