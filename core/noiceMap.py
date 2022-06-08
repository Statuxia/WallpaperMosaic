import random


def adjacent_min(noise):
    output = []
    for i in range(len(noise) - 1):
        output.append(min(noise[i], noise[i + 1]))
    return output


def create_maps():
    maps = []
    for i in range(5):
        random.seed(i)
        noise = [random.randint(0, 10) for i in range(10)]
        maps.append(adjacent_min(noise))

    return maps
